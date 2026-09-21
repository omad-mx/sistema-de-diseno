#!/usr/bin/env python3
"""
paleta-direccion-b.py — OMAD
Deriva la paleta de la dirección B («cálida y divulgativa») que usa la maqueta
de docs/maqueta-direccion-visual.html, para que el consejo compare A y B
(issue #1) sin que B sea un dibujo a mano.

Regla de derivación: cada color de B toma el mismo L y el mismo C (OKLCH) que
su equivalente de la 0.1 y solo cambia el tono. El neutro pasa de ~226° (frío)
a 70° (cálido); la marca pasa de ~215° (petróleo) a 350° (vino). Así la única
diferencia entre A y B es la temperatura, no el peso ni la legibilidad.

Por qué 350° y no un naranja o un terracota: la marca también es el color de
«completó» y tiene que separarse de bloqueante (#7C1D06) bajo simulación de
protanopia, deuteranopia y tritanopia. El barrido de tono con el L y C de
petróleo-600 da menos de 21 ΔE76 en todo el arco 30°–160° (naranjas, ocres,
oliva y verdes) y solo vuelve a superar el umbral en el arco 160°–10°. El vino
es el tono más cálido que sobrevive.

Uso:  python3 herramientas/paleta-direccion-b.py        # reporte + CSS
      python3 herramientas/paleta-direccion-b.py --css  # solo el bloque CSS

Simulación de visión cromática: matrices de Machado, Oliveira y Fernandes
(2009) con severidad 1.0, en RGB lineal. ΔE76 en CIELAB D65. No es la misma
implementación con la que se calcularon las tablas de la sección 4 del
documento; las cifras de este script se comparan entre sí, no con aquellas.
"""

import math
import sys
import os

# La fórmula de contraste es la del script del contrato, no una copia.
import importlib.util as _iu
_ruta = os.path.join(os.path.dirname(os.path.abspath(__file__)), "verificar-contraste.py")
_spec = _iu.spec_from_file_location("verificar_contraste", _ruta)
_vc = _iu.module_from_spec(_spec)
_spec.loader.exec_module(_vc)
contraste = _vc.contraste

TONO_NEUTRO_B = 70
TONO_MARCA_B = 350
UMBRAL_DE = 21.0  # el peor par que la 0.1 se exige a sí misma (sección 4)

TINTA_A = {
    "950": "#080F13", "900": "#0E1A1F", "800": "#16262D", "700": "#22363F",
    "600": "#334A55", "500": "#4C646F", "400": "#6B838E", "300": "#94A8B1",
    "200": "#BDCBD1", "100": "#DCE4E7", "50": "#EDF1F2", "0": "#FBFCFC",
}
PETROLEO_A = {
    "900": "#03282F", "800": "#053A45", "700": "#074C5B", "600": "#0B5563",
    "500": "#0E6B7D", "400": "#2C8A9C", "300": "#5FAEBD", "200": "#9BCED8",
    "100": "#CDE7EC", "50": "#E9F4F6",
}
BLOQUEANTE_600 = "#7C1D06"
BLOQUEANTE_300 = "#E9A088"


# --- color ------------------------------------------------------------------

def hex_a_rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def rgb_a_hex(rgb):
    return "#%02X%02X%02X" % tuple(max(0, min(255, round(c * 255))) for c in rgb)


def lineal(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def no_lineal(c):
    c = max(0.0, min(1.0, c))
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def rgb_a_oklab(rgb):
    r, g, b = (lineal(c) for c in rgb)
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l, m, s = l ** (1 / 3), m ** (1 / 3), s ** (1 / 3)
    return (0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s,
            1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s,
            0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s)


def oklab_a_rgb(L, a, b):
    l = L + 0.3963377774 * a + 0.2158037573 * b
    m = L - 0.1055613458 * a - 0.0638541728 * b
    s = L - 0.0894841775 * a - 1.2914855480 * b
    l, m, s = l ** 3, m ** 3, s ** 3
    return tuple(no_lineal(c) for c in (
        4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s,
        -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s,
        -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s))


def oklch(h):
    L, a, b = rgb_a_oklab(hex_a_rgb(h))
    return L, math.hypot(a, b), math.degrees(math.atan2(b, a)) % 360


def desde_oklch(L, C, H):
    return rgb_a_hex(oklab_a_rgb(L, C * math.cos(math.radians(H)),
                                 C * math.sin(math.radians(H))))


def girar_tono(h, tono):
    L, C, _ = oklch(h)
    return desde_oklch(L, C, tono)


def lab(h):
    r, g, b = (lineal(c) for c in hex_a_rgb(h))
    X = (0.4124564 * r + 0.3575761 * g + 0.1804375 * b) / 0.95047
    Y = (0.2126729 * r + 0.7151522 * g + 0.0721750 * b) / 1.0
    Z = (0.0193339 * r + 0.1191920 * g + 0.9503041 * b) / 1.08883
    f = lambda t: t ** (1 / 3) if t > 0.008856 else 7.787 * t + 16 / 116
    fx, fy, fz = f(X), f(Y), f(Z)
    return (116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz))


def delta_e(a, b):
    return math.dist(lab(a), lab(b))


SIMULACIONES = {
    "protanopia": [[0.152286, 1.052583, -0.204868],
                   [0.114503, 0.786281, 0.099216],
                   [-0.003882, -0.048116, 1.051998]],
    "deuteranopia": [[0.367322, 0.860646, -0.227968],
                     [0.280085, 0.672501, 0.047413],
                     [-0.011820, 0.042940, 0.968881]],
    "tritanopia": [[1.255528, -0.076749, -0.178779],
                   [-0.078411, 0.930809, 0.147602],
                   [0.004733, 0.691367, 0.303900]],
}


def simular(h, tipo):
    r = [lineal(c) for c in hex_a_rgb(h)]
    m = SIMULACIONES[tipo]
    return rgb_a_hex(tuple(no_lineal(sum(m[i][j] * r[j] for j in range(3)))
                           for i in range(3)))


def peor_delta(a, b):
    return min(delta_e(simular(a, t), simular(b, t)) for t in SIMULACIONES)


# --- derivación ---------------------------------------------------------------

TINTA_B = {k: girar_tono(v, TONO_NEUTRO_B) for k, v in TINTA_A.items()}
VINO_B = {k: girar_tono(v, TONO_MARCA_B) for k, v in PETROLEO_A.items()}

# Los mismos pares del contrato de la 0.1 que tocan neutro o marca, con los
# valores de B. Si B no cumple lo mismo que A, no es una alternativa justa.
CONTRATO_B = [
    ("tinta-900", "tinta-0", 4.5, "texto principal en claro"),
    ("tinta-700", "tinta-0", 4.5, "texto secundario en claro"),
    ("tinta-600", "tinta-0", 4.5, "texto terciario en claro"),
    ("tinta-900", "tinta-50", 4.5, "texto sobre superficie clara"),
    ("tinta-700", "tinta-50", 4.5, "texto secundario sobre superficie"),
    ("vino-600", "tinta-0", 4.5, "enlace en claro"),
    ("vino-700", "tinta-50", 4.5, "enlace sobre superficie clara"),
    ("tinta-0", "vino-600", 4.5, "texto en botón primario"),
    ("vino-600", "tinta-0", 3.0, "anillo de foco en claro"),
    ("tinta-50", "tinta-900", 4.5, "texto principal en oscuro"),
    ("tinta-200", "tinta-900", 4.5, "texto secundario en oscuro"),
    ("tinta-300", "tinta-900", 4.5, "texto terciario en oscuro"),
    ("tinta-50", "tinta-800", 4.5, "texto sobre superficie oscura"),
    ("vino-300", "tinta-900", 4.5, "enlace en oscuro"),
    ("vino-200", "tinta-900", 3.0, "anillo de foco en oscuro"),
    ("tinta-900", "vino-300", 4.5, "texto en botón primario (oscuro)"),
]


def resolver(nombre):
    familia, paso = nombre.split("-")
    return {"tinta": TINTA_B, "vino": VINO_B}[familia][paso]


def bloque_css():
    t, v = TINTA_B, VINO_B
    return f"""/* Generado por herramientas/paleta-direccion-b.py. No editar a mano:
   cada valor es el equivalente de la 0.1 con el tono girado en OKLCH. */
.especimen[data-neutro="calido"] {{
  --omad-fondo:            {t["0"]};
  --omad-superficie:       {t["50"]};
  --omad-superficie-alta:  #FFFFFF;
  --omad-borde:            {t["200"]};
  --omad-borde-fuerte:     {t["400"]};
  --omad-texto:            {t["900"]};
  --omad-texto-secundario: {t["700"]};
  --omad-texto-terciario:  {t["600"]};
  --omad-texto-invertido:  {t["0"]};
}}
.especimen[data-marca="vino"] {{
  --omad-enlace:           {v["600"]};
  --omad-enlace-visitado:  {v["800"]};
  --omad-accion-fondo:     {v["600"]};
  --omad-accion-hover:     {v["700"]};
  --omad-foco:             {v["600"]};
  --omad-completo:         {v["600"]};
  --omad-resalte:          {v["100"]};
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-tema='claro']) .especimen[data-neutro="calido"] {{
    --omad-fondo:            {t["900"]};
    --omad-superficie:       {t["800"]};
    --omad-superficie-alta:  {t["700"]};
    --omad-borde:            {t["600"]};
    --omad-borde-fuerte:     {t["400"]};
    --omad-texto:            {t["50"]};
    --omad-texto-secundario: {t["200"]};
    --omad-texto-terciario:  {t["300"]};
    --omad-texto-invertido:  {t["900"]};
  }}
  :root:not([data-tema='claro']) .especimen[data-marca="vino"] {{
    --omad-enlace:           {v["300"]};
    --omad-enlace-visitado:  {v["200"]};
    --omad-accion-fondo:     {v["300"]};
    --omad-accion-hover:     {v["200"]};
    --omad-foco:             {v["200"]};
    --omad-completo:         {v["300"]};
    --omad-resalte:          {v["900"]};
  }}
}}
:root[data-tema='oscuro'] .especimen[data-neutro="calido"] {{
  --omad-fondo:            {t["900"]};
  --omad-superficie:       {t["800"]};
  --omad-superficie-alta:  {t["700"]};
  --omad-borde:            {t["600"]};
  --omad-borde-fuerte:     {t["400"]};
  --omad-texto:            {t["50"]};
  --omad-texto-secundario: {t["200"]};
  --omad-texto-terciario:  {t["300"]};
  --omad-texto-invertido:  {t["900"]};
}}
:root[data-tema='oscuro'] .especimen[data-marca="vino"] {{
  --omad-enlace:           {v["300"]};
  --omad-enlace-visitado:  {v["200"]};
  --omad-accion-fondo:     {v["300"]};
  --omad-accion-hover:     {v["200"]};
  --omad-foco:             {v["200"]};
  --omad-completo:         {v["300"]};
  --omad-resalte:          {v["900"]};
}}"""


def reporte():
    print(f"Neutro B: tono {TONO_NEUTRO_B}°   Marca B (vino): tono {TONO_MARCA_B}°")
    print()
    print(f"{'paso':<6}{'tinta A':<10}{'tinta B':<10}   {'petróleo A':<12}{'vino B':<10}")
    print("-" * 52)
    pasos = list(TINTA_A)
    for p in pasos:
        pa = PETROLEO_A.get(p, "")
        vb = VINO_B.get(p, "")
        print(f"{p:<6}{TINTA_A[p]:<10}{TINTA_B[p]:<10}   {pa:<12}{vb:<10}")
    print()
    print("Contrato de contraste con los valores de B:")
    fallas = 0
    for fg, bg, minimo, para in CONTRATO_B:
        r = contraste(resolver(fg), resolver(bg))
        marca = "" if r >= minimo else "  <-- FALLA"
        fallas += r < minimo
        print(f"  {fg + ' / ' + bg:<26}{para:<38}{r:>6.2f}:1  {minimo}:1{marca}")
    print()
    print("Separación marca / bloqueante (peor de tres simulaciones, ΔE76):")
    for etiqueta, a, b in (
        ("petróleo-600 / bloqueante-600 (A, claro)", PETROLEO_A["600"], BLOQUEANTE_600),
        (f"vino-600 / bloqueante-600 (B, claro)", VINO_B["600"], BLOQUEANTE_600),
        ("petróleo-300 / bloqueante-300 (A, oscuro)", PETROLEO_A["300"], BLOQUEANTE_300),
        (f"vino-300 / bloqueante-300 (B, oscuro)", VINO_B["300"], BLOQUEANTE_300),
    ):
        d = peor_delta(a, b)
        aviso = "" if d >= UMBRAL_DE else f"  <-- por debajo de {UMBRAL_DE}"
        print(f"  {etiqueta:<44}{d:>6.1f}{aviso}")
    print()
    print("Barrido de tono para la marca (L y C de petróleo-600), ΔE mínimo vs bloqueante-600:")
    L, C, _ = oklch(PETROLEO_A["600"])
    fila = []
    for tono in range(0, 360, 10):
        d = peor_delta(desde_oklch(L, C, tono), BLOQUEANTE_600)
        fila.append(f"{tono:3d}°:{d:4.1f}{'' if d >= UMBRAL_DE else '*'}")
    for i in range(0, len(fila), 6):
        print("  " + "   ".join(fila[i:i + 6]))
    print(f"  (* = por debajo de {UMBRAL_DE})")
    return 1 if fallas else 0


if __name__ == "__main__":
    if "--css" in sys.argv:
        print(bloque_css())
    else:
        codigo = reporte()
        print()
        print(bloque_css())
        sys.exit(codigo)
