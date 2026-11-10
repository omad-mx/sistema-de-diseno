# Aviso

Estado: `borrador`

## Qué es

Un bloque de texto que avisa algo sobre toda la página. Su primer uso es
«Datos de ejemplo»: cada página del prototipo con datos inventados lo lleva
arriba, antes del título, para que se vea en cualquier captura.

## Cuándo se usa

- «Datos de ejemplo», en toda página que los muestre (sección 2 del plan).
- Algo que cambia cómo se lee toda la página: una auditoría en revisión, un
  corte de datos viejo.

## Cuándo no

- **Para el resultado de una acción** («cita copiada»). Eso es un mensaje de
  estado, y necesita anunciarse (4.1.3); el aviso no se anuncia.
- **Para un error de formulario.** Va junto al campo.
- **Para contenido de la página.** Si el aviso pasa de dos párrafos, lo que
  dice probablemente es contenido.
- **Para gravedad.** No usa los colores de la escala de gravedad.

## Anatomía

```html
<div class="aviso" role="note" aria-labelledby="aviso-datos">
  <p class="aviso-titulo" id="aviso-datos">Datos de ejemplo</p>
  <p>Nada de lo que aparece en esta página es una auditoría real.</p>
</div>
```

- `.aviso`, con `role="note"` y nombrado por su título.
- `.aviso-titulo`: un párrafo en peso fuerte. No es un encabezado, para no
  meterse en el índice de encabezados de la página.
- Uno o dos párrafos. Pueden llevar enlaces.

## Variantes y estados

Ninguna. Solo existe el uso que el prototipo necesita. Si un día hace falta
un aviso más urgente, se agrega entonces, y no con los colores de gravedad.

El aviso ocupa todo el ancho de su contenedor, pero su texto no pasa de la
medida de lectura. El borde grueso del inicio lo separa del contenido aunque
no haya color, y sigue ahí en alto contraste.

## Cómo se oye

Comprobado en el árbol de accesibilidad de Chromium; no se ha probado con un
lector de pantalla.

- «Nota, Datos de ejemplo», y luego sus párrafos.

No se anuncia solo al cargar la página: se lee en orden, y por eso va antes
del título.

## Criterios WCAG

- **1.3.1 Información y relaciones.** `role="note"` y su nombre dicen qué es.
- **1.4.3 Contraste mínimo.** Texto sobre `superficie`, medido en el
  contrato.
- **1.4.11 Contraste de elementos no textuales.** El borde es `borde-fuerte`,
  medido a 3:1 sobre las tres superficies.
- **1.4.10 Reflujo** y **1.4.12 Espaciado del texto.** Sin altura fija.

## Falta probar

- Que se vea lo bastante en una captura, sobre todo en tema oscuro, donde es
  discreto. Es la razón de que exista.
- Cómo anuncian `role="note"` los distintos lectores de pantalla: no todos
  lo anuncian ([#4](https://github.com/omad-mx/sistema-de-diseno/issues/4)).
- `forced-colors` en Windows.
- Safari y Firefox. Hasta ahora solo se ha visto en Chromium: 320 px y
  escritorio, tema claro y oscuro, con y sin espaciado forzado.
