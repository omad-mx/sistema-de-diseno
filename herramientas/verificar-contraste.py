#!/usr/bin/env python3
"""
verificar-contraste.py — OMAD
Calcula la razón de contraste WCAG 2.x de cada par de la paleta y reporta
si cumple AA texto (4.5:1), AA texto grande (3:1) y AA no-textual (3:1).

Uso:  python3 verificar-contraste.py
      python3 verificar-contraste.py --csv > contrastes.csv

Fórmula: WCAG 2.2, Understanding SC 1.4.3 (luminancia relativa sRGB).
No sustituye la verificación manual con lector de pantalla ni la revisión
de contraste en estados de foco sobre fondos reales.
"""

import sys
import itertools


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
# Paleta OMAD. Editar aquí y volver a correr el script.
# ---------------------------------------------------------------------------

TINTA = {
    "tinta-950": "#080F13",
    "tinta-900": "#0E1A1F",
    "tinta-800": "#16262D",
    "tinta-700": "#22363F",
    "tinta-600": "#334A55",
    "tinta-500": "#4C646F",
    "tinta-400": "#6B838E",
    "tinta-300": "#94A8B1",
    "tinta-200": "#BDCBD1",
    "tinta-100": "#DCE4E7",
    "tinta-50":  "#EDF1F2",
    "tinta-0":   "#FBFCFC",
}

PETROLEO = {
    "petroleo-900": "#03282F",
    "petroleo-800": "#053A45",
    "petroleo-700": "#074C5B",
    "petroleo-600": "#0B5563",
    "petroleo-500": "#0E6B7D",
    "petroleo-400": "#2C8A9C",
    "petroleo-300": "#5FAEBD",
    "petroleo-200": "#9BCED8",
    "petroleo-100": "#CDE7EC",
    "petroleo-50":  "#E9F4F6",
}

GRAVEDAD = {
    "bloqueante-900": "#4A1004",
    "bloqueante-700": "#631705",
    "bloqueante-600": "#7C1D06",
    "bloqueante-300": "#E9A088",
    "bloqueante-100": "#F7E0D8",
    "severa-700":     "#8A4A00",
    "severa-600":     "#9F5500",
    "severa-300":     "#F0BE7A",
    "severa-100":     "#FAEBD6",
    "moderada-700":   "#4F4739",
    "moderada-600":   "#63594A",
    "moderada-300":   "#C9BFAE",
    "moderada-100":   "#EFEAE2",
    "menor-700":      "#334654",
    "menor-600":      "#41586B",
    "menor-300":      "#A9BAC7",
    "menor-100":      "#E3E9EE",
}

PALETA = {**TINTA, **PETROLEO, **GRAVEDAD}

# Superficies contra las que se debe verificar todo color de texto o de icono.
SUPERFICIES_CLARO = {"fondo": "#FBFCFC", "superficie": "#EDF1F2", "elevada": "#FFFFFF"}
SUPERFICIES_OSCURO = {"fondo": "#0E1A1F", "superficie": "#16262D", "elevada": "#22363F"}

# Pares que el sistema promete que cumplen. Si uno falla, el build debe fallar.
CONTRATO = [
    # (primer plano, fondo, mínimo exigido, para qué)
    ("tinta-900", "tinta-0",   4.5, "texto principal en claro"),
    ("tinta-700", "tinta-0",   4.5, "texto secundario en claro"),
    ("tinta-600", "tinta-0",   4.5, "texto terciario en claro"),
    ("tinta-900", "tinta-50",  4.5, "texto sobre superficie clara"),
    ("tinta-700", "tinta-50",  4.5, "texto secundario sobre superficie"),
    ("petroleo-600", "tinta-0",  4.5, "enlace en claro"),
    ("petroleo-700", "tinta-50", 4.5, "enlace sobre superficie clara"),
    ("tinta-0", "petroleo-600",  4.5, "texto en botón primario"),
    ("petroleo-600", "tinta-0",  3.0, "anillo de foco en claro"),
    ("tinta-50",  "tinta-900",   4.5, "texto principal en oscuro"),
    ("tinta-200", "tinta-900",   4.5, "texto secundario en oscuro"),
    ("tinta-300", "tinta-900",   4.5, "texto terciario en oscuro"),
    ("tinta-50",  "tinta-800",   4.5, "texto sobre superficie oscura"),
    ("petroleo-300", "tinta-900", 4.5, "enlace en oscuro"),
    ("petroleo-200", "tinta-900", 3.0, "anillo de foco en oscuro"),
    ("bloqueante-600", "tinta-0",   4.5, "etiqueta bloqueante en claro"),
    ("severa-600",     "tinta-0",   4.5, "etiqueta severa en claro"),
    ("moderada-600",   "tinta-0",   4.5, "etiqueta moderada en claro"),
    ("menor-600",      "tinta-0",   4.5, "etiqueta menor en claro"),
    ("bloqueante-600", "tinta-50",  4.5, "etiqueta bloqueante sobre superficie"),
    ("severa-600",     "tinta-50",  4.5, "etiqueta severa sobre superficie"),
    ("bloqueante-300", "tinta-900", 4.5, "etiqueta bloqueante en oscuro"),
    ("severa-300",     "tinta-900", 4.5, "etiqueta severa en oscuro"),
    ("moderada-300",   "tinta-900", 4.5, "etiqueta moderada en oscuro"),
    ("menor-300",      "tinta-900", 4.5, "etiqueta menor en oscuro"),
    ("bloqueante-700", "bloqueante-100", 4.5, "texto sobre distintivo bloqueante"),
    ("severa-700",     "severa-100",     4.5, "texto sobre distintivo severa"),
    ("moderada-700",   "moderada-100",   4.5, "texto sobre distintivo moderada"),
    ("menor-700",      "menor-100",      4.5, "texto sobre distintivo menor"),
    ("bloqueante-300", "tinta-800",  4.5, "etiqueta bloqueante sobre superficie oscura"),
    ("severa-300",     "tinta-800",  4.5, "etiqueta severa sobre superficie oscura"),
]


def resolver(nombre):
    return PALETA.get(nombre, nombre)


def probar_contrato():
    fallas = []
    print(f"{'par':<44}{'para':<38}{'ratio':>8}  exigido")
    print("-" * 106)
    for fg, bg, minimo, para in CONTRATO:
        r = contraste(resolver(fg), resolver(bg))
        marca = "" if r >= minimo else "  <-- FALLA"
        print(f"{fg + ' / ' + bg:<44}{para:<38}{r:>7.2f}:1  {minimo}:1{marca}")
        if r < minimo:
            fallas.append((fg, bg, r, minimo, para))
    print()
    if fallas:
        print(f"{len(fallas)} par(es) incumplen el contrato del sistema.")
        return 1
    print(f"Los {len(CONTRATO)} pares del contrato cumplen.")
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
