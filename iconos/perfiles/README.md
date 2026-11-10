# Pictogramas de los seis perfiles

Uno por perfil, en el orden fijo de la franja. Se eligieron el 2026-11-10 en
[`docs/maqueta-pictogramas.html`](../../docs/maqueta-pictogramas.html).

| # | Perfil | Archivo | Pictograma | Original en Lucide |
|---|---|---|---|---|
| 1 | Lector de pantalla | `lector.svg` | bocina | `volume-2` |
| 2 | Solo teclado | `teclado.svg` | teclado | `keyboard` |
| 3 | Baja visión | `baja-vision.svg` | ojo | `eye` |
| 4 | Motriz | `motriz.svg` | mano que señala | `pointer` |
| 5 | Persona sorda | `sorda.svg` | globo de texto | `message-square-text` |
| 6 | Cognitivo | `cognitivo.svg` | cerebro | `brain` |

## De dónde vienen

De [Lucide](https://lucide.dev), versión 0.460.0, licencia ISC: se pueden
usar, modificar y redistribuir conservando el aviso de copyright, que está en
[`LICENSE`](LICENSE). El dibujo no se cambió; solo se quitó el atributo
`class` y se agregó un comentario con el origen.

No se dibujaron a mano: un set profesional da en los seis el mismo trazo
(2 px), la misma retícula (24 px) y las mismas esquinas, que es lo que pide
el paso 3.1 del [plan](../../docs/plan-de-construccion.md).

## Cómo se usan

- Con `currentColor`: toman el color del texto que los rodea. No tienen color
  propio (los perfiles no tienen color, sección 5 del documento).
- Siempre junto al nombre del perfil, y con `aria-hidden="true"`: el nombre
  es lo que se lee.
- A 24 px en la franja. Se probaron a 16, 24 y 48.

## Lo que no son

- No son un símbolo de discapacidad: se descartaron la silla de ruedas, la
  oreja tachada y la pieza de rompecabezas.
- No son de OMAD en exclusiva: vienen de un set público. Si la franja se
  registra como marca ([#3](https://github.com/omad-mx/sistema-de-diseno/issues/3)),
  el consejo tiene que saberlo.
