#!/usr/bin/env python3
"""
revisar-componentes.py — OMAD
Lee todo el CSS de componentes/ y falla si encuentra lo que las reglas del
sistema prohíben. Así las reglas dejan de depender de que alguien las
recuerde en la revisión.

Falla si un archivo tiene:
  - una primitiva de la capa 1 (por ejemplo, --omad-petroleo-600);
  - un color escrito a mano: hex, rgb(), hsl(), oklch(), oklab(), color();
  - outline: none (o 0) sin un :focus-visible en el mismo archivo;
  - !important.

Uso:  python3 herramientas/revisar-componentes.py
Sale con 1 si hay fallas; con 0 si todo cumple o si todavía no hay componentes.
"""

import importlib.util
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CARPETA = RAIZ / "componentes"

# Las primitivas son exactamente los nombres de la capa 1 de los tokens, y el
# script del contrato ya sabe leerlos. Se reutiliza en vez de copiarlo.
_spec = importlib.util.spec_from_file_location("verificar_contraste", RAIZ / "herramientas" / "verificar-contraste.py")
_vc = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_vc)
PRIMITIVAS = set(_vc.PALETA)

COLOR_A_MANO = re.compile(r"#[0-9a-fA-F]{3,8}\b|\b(?:rgba?|hsla?|oklch|oklab|lab|lch|color)\(", re.I)
OUTLINE_FUERA = re.compile(r"outline\s*:\s*(?:none|0)\b", re.I)
IMPORTANTE = re.compile(r"!\s*important", re.I)
TOKEN = re.compile(r"--omad-([\w-]+)")


def sin_comentarios(css):
    # Se conservan los saltos de línea para que los números de línea sigan siendo los del archivo.
    return re.sub(r"/\*.*?\*/", lambda m: re.sub(r"[^\n]", " ", m.group(0)), css, flags=re.S)


def revisar(ruta):
    css = sin_comentarios(ruta.read_text(encoding="utf-8"))
    fallas = []
    for numero, linea in enumerate(css.splitlines(), 1):
        for nombre in TOKEN.findall(linea):
            if nombre in PRIMITIVAS:
                fallas.append((numero, f"primitiva --omad-{nombre}; usa un token semántico"))
        if COLOR_A_MANO.search(linea):
            fallas.append((numero, "color escrito a mano; los colores viven en los tokens"))
        if IMPORTANTE.search(linea):
            fallas.append((numero, "!important"))
    if OUTLINE_FUERA.search(css) and ":focus-visible" not in css:
        fallas.append((0, "outline: none sin un :focus-visible equivalente en el archivo"))
    return fallas


def main():
    archivos = sorted(CARPETA.rglob("*.css"))
    if not archivos:
        print("No hay componentes todavía. Nada que revisar.")
        return 0
    total = 0
    for ruta in archivos:
        fallas = revisar(ruta)
        relativa = ruta.relative_to(RAIZ)
        if not fallas:
            print(f"{relativa}: cumple")
            continue
        total += len(fallas)
        for numero, mensaje in fallas:
            donde = f"{relativa}:{numero}" if numero else str(relativa)
            print(f"{donde}: {mensaje}")
    print()
    if total:
        print(f"{total} falla(s) en {len(archivos)} archivo(s).")
        return 1
    print(f"Los {len(archivos)} archivo(s) de componentes cumplen.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
