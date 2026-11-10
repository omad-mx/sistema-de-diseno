# Botón

Estado: `borrador`

## Qué es

El control que hace algo o lleva a la acción principal de una página. Hay
dos: primario y secundario. La misma clase viste a un `<button>` y a un
enlace que lleva a una acción.

## Cuándo se usa

- **Primario**, para la acción principal: una por pantalla, o una por bloque
  si la página tiene varios.
- **Secundario**, para la acción que acompaña a la principal.
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
- **Dos primarios juntos.** Si dos acciones pesan lo mismo, ninguna es la
  principal: van las dos como secundarias.

## Anatomía

Una sola pieza:

- `.boton`, sobre un `<button type="button">` o un `<a href>`. Dentro, solo
  texto.

Nunca va sobre un `<div>` ni un `<span>`: no se podrían activar con teclado.

## Variantes y estados

| Variante | Cómo se pide |
|---|---|
| Primario | sin atributo |
| Secundario | `data-variante="secundario"` |

| Estado | Qué lo activa | Qué cambia |
|---|---|---|
| Reposo | — | — |
| Puntero encima | `:hover` | El primario se oscurece; el secundario se rellena con el resalte. |
| Foco | `:focus-visible` | El anillo de doble capa de las reglas base. El botón no lo redefine. |
| Presionado | `:active` | El primario se oscurece un paso más; al secundario se le oscurece el contorno. |

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
- En `forced-colors`, visto en la emulación de Chromium, los dos botones se
  ven iguales: un contorno, sin relleno. Se distinguen de un enlace, pero no
  entre sí. Falta verlo en Windows y decidir si importa.
- Safari y Firefox. Hasta ahora solo se ha visto en Chromium: 320 px y
  escritorio, tema claro y oscuro, con y sin espaciado forzado, y los cuatro
  estados con puntero y teclado.
- Pantalla táctil: que el relleno del puntero encima no se quede pegado
  después de tocar.
