# Botón

Estado: `borrador`

## Qué es

El control que hace algo o lleva a la acción principal de una página. Hay
tres: primario, secundario y terciario. Los dos primeros visten igual a un
`<button>` que a un enlace que lleva a una acción; el terciario solo va
sobre un `<button>`.

## Cuándo se usa

- **Primario**, para la acción principal: una por pantalla, o una por bloque
  si la página tiene varios.
- **Secundario**, para la acción que acompaña a la principal.
- **Terciario**, para una acción dentro de un bloque, donde un contorno
  pesaría demasiado: ver la evidencia de un hallazgo, copiar una cita,
  ordenar una tabla. Se ve como enlace.
- Sobre un `<button>` cuando hace algo en la misma página (copiar la cita).
- Sobre un `<a href>` cuando lleva a otra página o descarga un archivo
  (consultar el ranking, descargar la evidencia).

## Cuándo no

- **Para un enlace dentro de un texto.** Es un enlace, subrayado, de las
  reglas base.
- **Para la navegación.** La navegación son enlaces (paso 3.7 del plan).
- **Para algo que no se puede hacer.** No hay botón deshabilitado: un botón
  apagado no dice por qué está apagado, y un lector de pantalla puede
  saltárselo. Si algo no se puede hacer, la página lo explica.
- **Un terciario que lleva a otra página.** Si se ve como enlace y lleva a
  otra parte, es un enlace: `<a href>`, sin clase.
- **Dos primarios juntos.** Si dos acciones pesan lo mismo, ninguna es la
  principal: van las dos como secundarias.

## Anatomía

Una sola pieza:

- `.boton`, sobre un `<button type="button">` o un `<a href>` (el
  terciario, solo sobre `<button>`). Dentro, solo texto.

Nunca va sobre un `<div>` ni un `<span>`: no se podrían activar con teclado.

## Variantes y estados

| Variante | Cómo se pide |
|---|---|
| Primario | sin atributo |
| Secundario | `data-variante="secundario"` |
| Terciario | `data-variante="terciario"` |

| Estado | Qué lo activa | Qué cambia |
|---|---|---|
| Reposo | — | — |
| Puntero encima | `:hover` | La etiqueta se subraya; en el terciario, el subrayado engruesa. Además, el primario se oscurece y el secundario se rellena con el resalte. |
| Foco | `:focus-visible` | El anillo de doble capa de las reglas base. El botón no lo redefine. |
| Presionado | `:active` | El primario se oscurece un paso más; al secundario se le oscurece el contorno; el terciario se rellena con el resalte. |

El subrayado del puntero encima está porque el cambio de relleno solo apenas
se nota: entre reposo y encima hay de 1.14 a 1.48 de contraste, y en tema
oscuro, sobre una superficie, el secundario no cambia nada (1.0). WCAG no
exige que el puntero encima se vea, pero el sistema sí.

El terciario tiene un relleno lateral que amplía el área activable y un
margen negativo del mismo tamaño, para que la etiqueta quede alineada con el
texto que tiene arriba.

Un enlace con `.boton` no cambia de color al visitarse.

Una etiqueta larga ocupa dos líneas y el botón crece. Una etiqueta de dos
letras no baja de 44 × 44 px.

## Cómo se oye

Esperado; no se ha probado con un lector de pantalla.

- Sobre un `<button>`: «Copiar la cita, botón».
- Sobre un `<a>`: «Consultar el ranking, enlace». Se ve como botón y se
  anuncia como enlace, y está bien: dice la verdad sobre lo que hace. No se
  le pone `role="button"`.

Lo que se oye es la etiqueta, así que la etiqueta tiene que entenderse sola:
«Descargar la evidencia», no «Descargar».

## Criterios WCAG

- **1.4.1 Uso del color.** Es el único enlace sin subrayado del sistema. Lo
  que lo señala como activable es su forma (contorno y relleno), no el color
  del texto.
- **1.4.3 Contraste mínimo** y **1.4.11 Contraste de elementos no textuales.**
  El contrato de contraste mide el texto sobre el relleno en los tres estados
  y el contorno sobre las tres superficies, en claro y en oscuro.
- **2.1.1 Teclado.** Solo elementos nativos.
- **2.4.7 Foco visible** y **2.4.13 Apariencia del foco** (AAA). El anillo de
  la base.
- **2.5.8 Tamaño del objetivo.** Mínimo de 44 × 44 px; la norma pide 24.
- **1.4.12 Espaciado del texto** y **1.4.10 Reflujo.** Sin altura fija; la
  etiqueta se parte y el botón crece.

## Falta probar

- Lectores de pantalla: VoiceOver, NVDA y TalkBack
  ([#4](https://github.com/omad-mx/sistema-de-diseno/issues/4)).
- En `forced-colors`, visto en la emulación de Chromium, los tres botones se
  ven como un contorno sin relleno; el terciario se distingue por el
  subrayado, pero primario y secundario se ven iguales. Falta verlo en
  Windows y decidir si importa.
- Safari y Firefox. Hasta ahora solo se ha visto en Chromium: 320 px y
  escritorio, tema claro y oscuro, con y sin espaciado forzado, y los cuatro
  estados con puntero y teclado.
- Pantalla táctil: que el relleno del puntero encima no se quede pegado
  después de tocar.
