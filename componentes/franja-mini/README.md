# Franja mini

Estado: `borrador` · **propuesta, como la franja**

## Qué es

La franja en pequeño, para una celda de tabla: seis casillas con la marca de
resultado de cada perfil, en el mismo lugar que en la franja (dos filas de
tres), y el total a la vista, «4 de 6». Sin pictogramas ni nombres: la
posición dice el perfil, y una leyenda en la tabla lo explica.

## Cuándo se usa

- En el ranking y en cualquier tabla con un trámite por fila.
- Siempre con su leyenda en la nota de la tabla.

## Cuándo no

- **Para el resultado destacado de un trámite.** Eso es la franja (3.2).
- **Sin tabla y sin leyenda.** Fuera de una tabla con leyenda, las casillas
  no dicen qué perfil es cada una; va la franja.

## Anatomía

```html
<span class="franja-mini">
  <span class="franja-mini-celdas" aria-hidden="true">
    <span class="franja-mini-casilla"><span class="marca-resultado" data-resultado="si"></span></span>
    <!-- …las otras cinco, en el orden de la franja -->
  </span>
  <span class="franja-mini-total">4 de 6</span>
  <span class="visualmente-oculto"> perfiles completaron. No completaron: baja visión y cognitivo.</span>
</span>
```

- `.franja-mini-celdas`: las seis casillas, con `aria-hidden`.
- `.franja-mini-casilla`: una por perfil, con una marca de resultado (2.4)
  sin texto. El borde toma el color del resultado.
- `.franja-mini-total`: el total a la vista, para no contar marcas.
- La frase oculta completa el total para lector de pantalla y dice quién no
  completó.

**La leyenda** es la misma pieza con el pictograma de cada perfil
(`.franja-mini-picto`, de `iconos/perfiles/`) en lugar de la marca, sin total,
y con la lista de perfiles en orden como texto oculto. Va en la nota
(`.tabla-nota`) de la tabla.

## Variantes y estados

No tiene variantes ni estados.

- Dos filas de tres casillas, el mismo mapa que la franja: cada perfil está
  en el mismo lugar en las dos.
- Las casillas usan `--omad-radio-2` (4 px), el radio chico del sistema, que
  hasta ahora nadie usaba.
- En `forced-colors` las casillas se dibujan con el color de texto del
  sistema.

## Cómo se oye

Comprobado en el árbol de accesibilidad de Chromium; no se ha probado con un
lector de pantalla.

- «2 de 6 perfiles completaron. No completaron: lector de pantalla, solo
  teclado, motriz y cognitivo.»
- «6 de 6 perfiles completaron.»
- La leyenda, en la nota: «Perfiles, en el orden de la franja: lector de
  pantalla, solo teclado, baja visión, motriz, persona sorda y cognitivo.»

En una tabla, cada fila dice el resultado completo sin recorrer seis
casillas.

## Criterios WCAG

- **1.1.1 Contenido no textual.** Las casillas tienen su equivalente en texto:
  el total y la frase.
- **1.3.1 Información y relaciones.** La leyenda explica qué perfil es cada
  posición.
- **1.4.1 Uso del color.** Palomita y tache; el borde de color acompaña.
- **1.4.11 Contraste de elementos no textuales.** Las marcas usan
  `completo` y `no-completo`, medidos en el contrato.

## Falta probar

- **Dos filas de tres o una línea de seis.** El ejemplo compara las dos. La
  línea es más baja y cabe mejor en un renglón, pero cada perfil queda en
  otro lugar que en la franja. Lo decide la dirección de diseño.
- Lectores de pantalla: VoiceOver, NVDA y TalkBack
  ([#4](https://github.com/omad-mx/sistema-de-diseno/issues/4)).
- Si el texto de la frase debe generarse de los datos (paso 4.1 del plan):
  hoy se escribe a mano en cada fila.
- Safari y Firefox. Hasta ahora solo se ha visto en Chromium: 320 px y
  escritorio, tema claro y oscuro, con y sin espaciado forzado, y
  `forced-colors` emulado.
