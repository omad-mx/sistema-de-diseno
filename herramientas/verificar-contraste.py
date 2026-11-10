#!/usr/bin/env python3
"""
verificar-contraste.py — OMAD
Calcula la razón de contraste WCAG 2.x de cada par del contrato y reporta
si cumple AA texto (4.5:1) o AA texto grande y no textual (3:1).

El contrato está escrito con los tokens semánticos (capa 2), que son los que
usan los componentes. Cada par se mide dos veces, en tema claro y en tema
oscuro, siguiendo cada token hasta su primitiva (capa 1). Los colores se leen
de tokens/omad-tokens.css; aquí solo vive el contrato.

Además de los pares, el script falla si:
  - un token de color de la capa 2 no apunta a una primitiva con var();
  - los dos bloques del tema oscuro (el de la preferencia del sistema y el
    del atributo data-tema) no son idénticos;
  - un token de color de la capa 2 no aparece en ningún par del contrato ni
    en la lista de exentos.

Uso:  python3 verificar-contraste.py
      python3 verificar-contraste.py --csv > contrastes.csv

Fórmula: WCAG 2.2, Understanding SC 1.4.3 (luminancia relativa sRGB).
No sustituye la verificación manual con lector de pantalla ni la revisión
de contraste en estados de foco sobre fondos reales.
"""

import itertools
import re
import sys
from pathlib import Path


def hex_a_rgb(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def luminancia(h):
    def canal(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = (canal(v) for v in hex_a_rgb(h))
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contraste(a, b):
    la, lb = luminancia(a), luminancia(b)
    claro, oscuro = max(la, lb), min(la, lb)
    return (claro + 0.05) / (oscuro + 0.05)


def veredicto(ratio):
    if ratio >= 7:
        return "AAA texto"
    if ratio >= 4.5:
        return "AA texto"
    if ratio >= 3:
        return "AA texto grande / no textual"
    return "NO CUMPLE"


# ---------------------------------------------------------------------------
# Paleta OMAD. Se lee de la capa 1 de tokens/omad-tokens.css: ahí se edita.
# ---------------------------------------------------------------------------

RUTA_TOKENS = Path(__file__).resolve().parent.parent / "tokens" / "omad-tokens.css"


def leer_paleta(ruta=RUTA_TOKENS):
    css = ruta.read_text(encoding="utf-8")
    inicio, fin = css.find("CAPA 1 ·"), css.find("CAPA 2 ·")
    if inicio < 0 or fin < inicio:
        sys.exit(f"No encontré la capa 1 en {ruta}.")
    capa_1 = re.sub(r"/\*.*?\*/", "", css[inicio:fin], flags=re.S)
    declaraciones = re.findall(r"--omad-([\w-]+)\s*:\s*([^;]+);", capa_1)
    if not declaraciones:
        sys.exit(f"La capa 1 de {ruta} no tiene colores.")
    for nombre, valor in declaraciones:
        if not re.fullmatch(r"#(?:[0-9a-fA-F]{3}|[0-9a-fA-F]{6})", valor.strip()):
            sys.exit(f"--omad-{nombre}: «{valor.strip()}» no es un hexadecimal; el script no puede medirlo.")
    return {nombre: valor.strip() for nombre, valor in declaraciones}


PALETA = leer_paleta()


# ---------------------------------------------------------------------------
# Capa 2. Cada token semántico apunta a una primitiva, una vez por tema.
# ---------------------------------------------------------------------------

def leer_semanticos(ruta=RUTA_TOKENS):
    """Devuelve {'claro': {token: primitiva}, 'oscuro': {token: primitiva}}."""
    css = ruta.read_text(encoding="utf-8")
    inicio, fin = css.find("CAPA 2 ·"), css.find("TIPOGRAFÍA")
    if inicio < 0 or fin < inicio:
        sys.exit(f"No encontré la capa 2 en {ruta}.")
    # Los dos rótulos están dentro de comentarios: se corta al cerrar el primero
    # y antes de abrir el segundo.
    inicio, fin = css.find("*/", inicio) + 2, css.rfind("/*", inicio, fin)
    capa_2 = re.sub(r"/\*.*?\*/", "", css[inicio:fin], flags=re.S)

    bloques = {}
    for selector, cuerpo in re.findall(r"([^{}]+)\{([^{}]*)\}", capa_2):
        selector = selector.split("{")[-1].strip()
        tokens = {}
        for nombre, valor in re.findall(r"--omad-([\w-]+)\s*:\s*([^;]+);", cuerpo):
            apunta = re.fullmatch(r"var\(--omad-([\w-]+)\)", valor.strip())
            if not apunta:
                sys.exit(f"--omad-{nombre}: «{valor.strip()}» no apunta a una primitiva. "
                         "En la capa 2 no se escriben colores a mano.")
            if apunta.group(1) not in PALETA:
                sys.exit(f"--omad-{nombre} apunta a «{apunta.group(1)}», que no existe en la capa 1.")
            tokens[nombre] = apunta.group(1)
        bloques[selector] = tokens

    esperados = {
        "claro": ":root",
        "oscuro por preferencia del sistema": ":root:not([data-tema='claro'])",
        "oscuro por atributo": ":root[data-tema='oscuro']",
    }
    for cual, selector in esperados.items():
        if selector not in bloques:
            sys.exit(f"No encontré el bloque del tema {cual} ({selector}) en la capa 2.")
    claro = bloques[":root"]
    oscuro = bloques[":root[data-tema='oscuro']"]
    if bloques[":root:not([data-tema='claro'])"] != oscuro:
        sys.exit("Los dos bloques del tema oscuro no son idénticos. "
                 "Lo que cambie en uno tiene que cambiar en el otro.")
    if set(claro) != set(oscuro):
        distintos = sorted(set(claro) ^ set(oscuro))
        sys.exit(f"Estos tokens existen en un tema y no en el otro: {', '.join(distintos)}.")
    return {"claro": claro, "oscuro": oscuro}


SEMANTICOS = leer_semanticos()

# ---------------------------------------------------------------------------
# El contrato. Pares que el sistema promete que cumplen, en los dos temas.
# Si uno falla, el build debe fallar.
# ---------------------------------------------------------------------------

TEXTO, NO_TEXTUAL = 4.5, 3.0

# Las tres superficies sobre las que puede ir cualquier cosa.
FONDOS = ["fondo", "superficie", "superficie-alta"]

# (token, mínimo exigido, para qué). Cada uno se mide sobre los tres fondos.
SOBRE_FONDOS = [
    ("texto",            TEXTO, "texto principal"),
    ("texto-secundario", TEXTO, "texto secundario"),
    ("texto-terciario",  TEXTO, "texto terciario"),
    ("enlace",           TEXTO, "enlace"),
    ("enlace-visitado",  TEXTO, "enlace visitado"),
    ("completo",         TEXTO, "marca de completó"),
    ("no-completo",      TEXTO, "marca de no completó"),
    ("bloqueante",       TEXTO, "etiqueta bloqueante"),
    ("severa",           TEXTO, "etiqueta severa"),
    ("moderada",         TEXTO, "etiqueta moderada"),
    ("menor",            TEXTO, "etiqueta menor"),
    ("foco",             NO_TEXTUAL, "anillo de foco"),
    ("borde-fuerte",     NO_TEXTUAL, "borde de control"),
    ("accion-fondo",     NO_TEXTUAL, "contorno del botón"),
]

# (primer plano, fondo, mínimo exigido, para qué). Pares con fondo propio.
PARES_PROPIOS = [
    ("accion-texto",     "accion-fondo",     TEXTO, "texto del botón"),
    ("accion-texto",     "accion-hover",     TEXTO, "texto del botón con el puntero encima"),
    ("accion-texto",     "accion-activo",    TEXTO, "texto del botón al presionarlo"),
    ("enlace",           "resalte",          TEXTO, "texto del botón secundario con el puntero encima"),
    ("accion-fondo",     "resalte",          NO_TEXTUAL, "contorno del botón secundario con el puntero encima"),
    ("accion-activo",    "resalte",          NO_TEXTUAL, "contorno del botón secundario al presionarlo"),
    ("texto-invertido",  "texto",            TEXTO, "texto invertido"),
    ("foco",             "foco-contorno",    NO_TEXTUAL, "las dos capas del anillo de foco"),
    ("bloqueante-texto", "bloqueante-fondo", TEXTO, "distintivo bloqueante"),
    ("severa-texto",     "severa-fondo",     TEXTO, "distintivo severa"),
    ("moderada-texto",   "moderada-fondo",   TEXTO, "distintivo moderada"),
    ("menor-texto",      "menor-fondo",      TEXTO, "distintivo menor"),
]

# Tokens de color que no entran al contrato, cada uno con su razón. Un token
# nuevo que no esté en un par ni aquí hace fallar el script.
EXENTOS = {
    "borde": "línea divisoria decorativa; nunca es lo único que delimita un control ni carga información",
}

CONTRATO = [
    (token, fondo, minimo, f"{para} sobre {fondo.replace('-', ' ')}")
    for token, minimo, para in SOBRE_FONDOS
    for fondo in FONDOS
] + PARES_PROPIOS


def resolver(token, tema):
    if token not in SEMANTICOS[tema]:
        sys.exit(f"El contrato usa «{token}», que no existe en la capa 2 de los tokens.")
    return PALETA[SEMANTICOS[tema][token]]


def tokens_sin_medir():
    medidos = {t for par in CONTRATO for t in par[:2]}
    return sorted(set(SEMANTICOS["claro"]) - medidos - set(EXENTOS))


def probar_contrato():
    fallas = []
    print(f"{'par':<40}{'para':<50}{'claro':>9}{'oscuro':>10}  exigido")
    print("-" * 119)
    for fg, bg, minimo, para in CONTRATO:
        medidas = {}
        for tema in ("claro", "oscuro"):
            medidas[tema] = contraste(resolver(fg, tema), resolver(bg, tema))
            if medidas[tema] < minimo:
                fallas.append((fg, bg, tema, medidas[tema], minimo))
        marca = "" if all(m >= minimo for m in medidas.values()) else "  <-- FALLA"
        print(f"{fg + ' / ' + bg:<40}{para:<50}"
              f"{medidas['claro']:>7.2f}:1{medidas['oscuro']:>8.2f}:1  {minimo}:1{marca}")
    print()

    sin_medir = tokens_sin_medir()
    for token in sin_medir:
        print(f"--omad-{token} no está en ningún par del contrato ni en la lista de exentos.")
    for token, razon in EXENTOS.items():
        print(f"Exento: --omad-{token} ({razon}).")
    print()

    if fallas or sin_medir:
        if fallas:
            print(f"{len(fallas)} medida(s) incumplen el contrato del sistema.")
        if sin_medir:
            print(f"{len(sin_medir)} token(s) de color sin medir.")
        return 1
    print(f"Los {len(CONTRATO)} pares del contrato cumplen en tema claro y en tema oscuro.")
    return 0


def volcar_csv():
    print("color_a,color_b,hex_a,hex_b,ratio,veredicto")
    for a, b in itertools.combinations(PALETA, 2):
        r = contraste(PALETA[a], PALETA[b])
        print(f"{a},{b},{PALETA[a]},{PALETA[b]},{r:.2f},{veredicto(r)}")


if __name__ == "__main__":
    if "--csv" in sys.argv:
        volcar_csv()
    else:
        sys.exit(probar_contrato())
