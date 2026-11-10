# Resultado por perfiles

Estado: `borrador`

## Qué es

El resultado de un trámite en una línea de texto, para una celda de tabla:
el total y quién no completó, escrito. «4 de 6 · no completaron: baja visión
y cognitivo».

Reemplaza a la franja mini, una cuadrícula de seis casillas con palomita o
tache. Se descartó el 2026-11-10: sin pictogramas ni nombres, había que
saberse de memoria qué perfil era cada casilla o ir a una leyenda. Una
columna por perfil lo resolvía en escritorio, pero en un teléfono escondía
hasta el total, y cruzar fila y columna para cada dato es más carga
cognitiva que leer una frase.

## Cuándo se usa

- En el ranking y en cualquier tabla con un trámite por fila.
- En una lista o un texto, cuando hay que dar el resultado en una línea.

## Cuándo no

- **Para el resultado destacado de un trámite.** Eso es la franja (3.2).
- **Para comparar un perfil entre muchos trámites.** Eso pide una vista
  propia, que no existe todavía.

## Anatomía

```html
<span class="resultado-perfiles">
  <strong class="resultado-perfiles-total">4 de 6</strong><span class="visualmente-oculto"> perfiles completaron</span>
  · no completaron: baja visión y cognitivo
</span>
```

- `.resultado-perfiles`: la línea.
- `.resultado-perfiles-total`: el total, en peso fuerte y cifras tabulares,
  sin partirse.
- «perfiles completaron», solo para lector de pantalla: a la vista lo dice el
  encabezado de la columna; al oído, el total tiene que entenderse solo.
- Quién no completó, con los nombres completos de los perfiles y en su orden
  fijo.

## Variantes y estados

No tiene variantes. Cómo se escribe cada caso:

| Resultado | Se escribe |
|---|---|
| 6 de 6 | «6 de 6», nada más. |
| 5 de 6 | «5 de 6 · no completó: motriz», en singular. |
| De 1 a 4 | «4 de 6 · no completaron: baja visión y cognitivo». |
| 0 de 6 | «0 de 6 · no completó ninguno», sin listar a los seis. |

A 320 px la frase se acomoda en varias líneas y el total no se parte. Pero dentro de una tabla de cuatro columnas, en un teléfono la columna queda fuera de la vista: la tabla se desplaza. Ver «Falta probar».

## Cómo se oye

Comprobado en el árbol de accesibilidad de Chromium; no se ha probado con un
lector de pantalla.

- «4 de 6 perfiles completaron · no completaron: baja visión y cognitivo».
- «6 de 6 perfiles completaron».

## Criterios WCAG

- **1.3.1 Información y relaciones** y **1.1.1 Contenido no textual.** Todo
  es texto: no hay símbolos que necesiten equivalente.
- **1.4.1 Uso del color.** No usa color.
- **1.4.10 Reflujo.** Una línea de texto que se acomoda en cualquier ancho.
- **3.1.5 Nivel de lectura** (AAA), en parte: una frase en lugar de una
  matriz.

## Falta probar

- **En un teléfono, dentro de una tabla, el resultado queda fuera de la
  vista.** La tabla de datos solo deja ver el número y el trámite a 320 px.
  Hace falta que la tabla sepa acomodarse en un ancho angosto; está en
  discusión.
- Lectores de pantalla: VoiceOver, NVDA y TalkBack
  ([#4](https://github.com/omad-mx/sistema-de-diseno/issues/4)).
- Que la frase se genere de los datos (paso 4.1 del plan) con las reglas de
  la tabla de arriba; hoy se escribe a mano.
- Safari y Firefox. Hasta ahora solo se ha visto en Chromium: 320 px y
  escritorio, tema claro y oscuro, con y sin espaciado forzado.
