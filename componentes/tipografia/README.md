# Tipografía y prosa

Estado: `borrador`

## Qué es

Cómo se ve el texto del sitio: los encabezados de primer a cuarto nivel, el
párrafo, las listas, la cejilla (el rótulo pequeño sobre un título), la
entrada (el párrafo de apertura) y el contenedor de prosa, que pone la medida
de lectura y el espacio entre párrafos.

## Cuándo se usa

- Los encabezados y el párrafo, siempre: se estilan por elemento, así que
  cualquier `h1` a `h4` y cualquier `p` del sitio ya los trae.
- `.prosa`, para texto corrido de lectura: la metodología, la descripción de
  un hallazgo, un aviso largo.
- `.cejilla`, sobre un título, para decir a qué sección o a qué tipo de
  página pertenece.
- `.entrada`, bajo el título de una página o de una sección, para resumirla.

## Cuándo no

- **No se elige un encabezado por su tamaño.** El nivel lo decide la
  estructura de la página. No hay clases para que un `h2` se vea como `h3`.
- **`.prosa` no es un contenedor de página.** No se meten en ella una tabla
  ancha ni una franja: quedarían limitadas a la medida de lectura.
- **La cejilla no sustituye a un encabezado.** Es un párrafo. Si el texto
  nombra una sección, es un encabezado.
- **Una cifra no es una entrada.** Para el número grande, la cifra citable
  (paso 3.5 del plan).

## Anatomía

No hay una raíz común. Son tres clases y cinco elementos:

- `h1`, `h2`, `h3`, `h4`: tamaño, peso e interlínea. Sin margen.
- `p`: sin margen. El espacio lo pone quien lo contiene.
- `.cejilla`: va en un `p`, justo antes del encabezado.
- `.entrada`: va en un `p`, justo después del encabezado.
- `.prosa`: va en un `div`, un `section` o un `article`. Dentro, HTML sin
  clases: encabezados, `p`, `ul`, `ol`.

Es la única excepción a la regla de que las partes llevan el nombre del
componente como prefijo: aquí cada clase es su propia raíz, porque ninguna
contiene a las otras.

## Variantes y estados

No tiene variantes ni estados. Sí tiene un comportamiento:

- **En un contenedor angosto, los cuatro encabezados bajan un paso de la
  escala** y lo recuperan poco a poco al ensancharse. A tamaño completo,
  «accesibilidad» en un `h1` no cabe en una línea de 320 px con el espaciado
  de texto forzado, y se parte a media palabra. Bajan los cuatro y no solo el
  primero para que ningún nivel alcance al siguiente.
- La entrada nunca pasa de la medida del sistema, por ancho que sea su
  contenedor.
- Una palabra o una dirección más ancha que su columna se parte en lugar de
  desbordar la página. Esa regla vive en `estilos/base.css`.

## Cómo se oye

Esperado; no se ha probado con un lector de pantalla.

- Los encabezados se anuncian con su nivel: «encabezado de nivel 2, Cómo se
  compone el texto». Se puede saltar de uno a otro.
- La cejilla se lee como un párrafo, antes del encabezado, con el texto como
  está escrito en el HTML. Las mayúsculas las pone el CSS, así que no se
  deletrea.
- La entrada se lee como un párrafo.
- Las listas anuncian cuántos elementos tienen; las numeradas, además, el
  número de cada uno.

## Criterios WCAG

- **1.3.1 Información y relaciones.** Encabezados y listas son los elementos
  nativos, no párrafos con otro tamaño.
- **1.4.3 Contraste mínimo.** La cejilla usa `texto-terciario` y la entrada,
  `texto-secundario`; el contrato de contraste mide los dos sobre las tres
  superficies, en claro y en oscuro.
- **1.4.4 Cambio de tamaño del texto.** Todos los tamaños están en `rem`. Los
  encabezados que se ajustan al contenedor tienen sus límites en `rem`.
- **1.4.10 Reflujo.** Sin anchos ni alturas fijas; lo que no cabe, se parte.
- **1.4.12 Espaciado del texto.** El ejemplo trae un control que lo fuerza.
- **2.4.6 Encabezados y etiquetas** y **2.4.10 Encabezados de sección** (AAA):
  al no poder elegir un encabezado por su tamaño, el nivel sigue a la
  estructura.
- **1.4.8 Presentación visual** (AAA), en parte: la medida no pasa de 66
  caracteres y la interlínea del cuerpo es de 1.65.

## Falta probar

- Lectores de pantalla: VoiceOver, NVDA y TalkBack
  ([#4](https://github.com/omad-mx/sistema-de-diseno/issues/4)). En especial,
  que ninguno deletree la cejilla.
- `forced-colors` (el modo de alto contraste de Windows).
- Safari y Firefox. Hasta ahora solo se ha visto en Chromium: 320 px y
  escritorio, tema claro y oscuro, con y sin espaciado forzado.
- Zoom al 400 % en un navegador real.
