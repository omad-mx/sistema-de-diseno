# Tabla de datos

Estado: `borrador`

## Qué es

Resultados en filas y columnas: el ranking, los perfiles por trámite, las
cifras por dependencia. Lleva su nombre arriba, cifras alineadas y un
encabezado por fila. Si no cabe, se desplaza a lo ancho dentro de su caja,
no la página.

## Cuándo se usa

- Para comparar varias filas en las mismas columnas.
- Cuando cada fila describe una cosa (un trámite, una dependencia) y cada
  columna, un dato de esa cosa.

## Cuándo no

- **Para acomodar contenido en columnas.** Eso es la rejilla de una página.
- **Para una sola fila o una sola columna.** Es una lista.
- **Para el resultado de un trámite por perfil, de forma destacada.** Eso es
  la franja (3.2). En una tabla con un trámite por fila va el resultado por perfiles (3.3).

## Anatomía

```html
<div class="tabla" role="region" aria-labelledby="t-ranking" tabindex="0">
  <table>
    <caption id="t-ranking">
      Ranking de trámites
      <span class="tabla-nota">Corte al 30 de junio.</span>
    </caption>
    <thead>
      <tr><th scope="col">Trámite</th><th scope="col" class="tabla-cifra">Bloqueantes</th></tr>
    </thead>
    <tbody>
      <tr><th scope="row">…</th><td class="tabla-cifra">3</td></tr>
    </tbody>
  </table>
</div>
```

- `.tabla`: la caja que se desplaza. Lleva `role="region"`, el nombre de la
  tabla (`aria-labelledby` apuntando al `caption`) y `tabindex="0"`, para que
  se pueda desplazar con las flechas del teclado. Si no va sobre el fondo de
  la página, dice sobre qué va: `data-sobre="superficie"` o
  `data-sobre="superficie-alta"` (lo necesita la sombra del borde).
- `<table>` sin clases.
- `<caption>`, obligatorio: el nombre de la tabla. Va arriba.
- `.tabla-nota`, opcional, dentro del `caption`: la fuente, el corte o
  «Datos de ejemplo».
- `<th scope="col">` en el encabezado y `<th scope="row">` en la columna que
  nombra la fila.
- `.tabla-cifra` en las celdas y encabezados de columnas numéricas: se
  alinean a la derecha.
- `.tabla-vacia` en la única celda de una tabla sin datos, con `colspan`.

## Variantes y estados

| Variante | Cómo se pide | Qué hace |
|---|---|---|
| Normal | sin atributo | Si no cabe, se desplaza a lo ancho dentro de su caja. |
| Apilable | `data-variante="apilable"` | En un contenedor de menos de 36 rem, cada fila se acomoda como tarjeta: el encabezado de fila arriba y cada dato en su renglón, con el nombre de su columna delante. |

**Apilable** es para tablas con una cosa por fila, como el ranking, donde
desplazar a lo ancho esconde lo importante: a 320 px, una tabla de cuatro
columnas solo deja ver el número y el trámite. Una tabla para comparar
muchas columnas no la lleva.

Al cambiar el `display` de las celdas, algunos navegadores dejan de anunciar
la tabla como tabla. Por eso la variante pide los roles escritos en el HTML,
y cada celda de datos lleva el nombre de su columna en `data-etiqueta`:

```html
<div class="tabla" data-variante="apilable" role="region" aria-labelledby="t-ranking" tabindex="0">
  <table role="table">
    <caption id="t-ranking">Ranking de trámites</caption>
    <thead role="rowgroup">
      <tr role="row"><th role="columnheader" scope="col">Trámite</th><th role="columnheader" scope="col">Bloqueantes</th></tr>
    </thead>
    <tbody role="rowgroup">
      <tr role="row"><th role="rowheader" scope="row">…</th><td role="cell" data-etiqueta="Bloqueantes">3</td></tr>
    </tbody>
  </table>
</div>
```

El nombre de la columna que se ve delante de cada dato lleva un texto
alternativo vacío, para que el lector de pantalla no lo lea dos veces: ya
anuncia el encabezado de la columna.

Comportamiento de las dos:

- Radio 0: es un dato, no un control.
- Cifras tabulares, para que las columnas alineen.
- Si la tabla es más ancha que su caja, se desplaza dentro de ella. El nombre
  (`caption`) se queda fijo y del ancho de lo que se ve, para leerse completo
  sin mover la tabla.
- El encabezado de fila tiene un ancho mínimo de 11 rem: en una pantalla
  angosta, la tabla se desplaza en lugar de partir el trámite en una palabra
  por renglón.
- **Cuando hay columnas fuera de la vista, una sombra suave aparece en ese
  borde**, y se va al llegar al extremo. Sin JavaScript: dos sombras fijas a
  la caja y dos «tapas» del color del fondo que viajan con el contenido. Por
  eso la tabla tiene que saber sobre qué fondo va. En `forced-colors` la
  sombra desaparece; la tabla se sigue viendo cortada.
- La caja recibe el foco con el tabulador (el anillo de la base) y se
  desplaza con las flechas.
- Sin datos, una sola fila dice por qué. Los encabezados se quedan, para que
  se sepa qué habría.

La caja necesita `position: relative`. Sin ella, los textos ocultos para
lector de pantalla de las celdas (por ejemplo, el de una marca de resultado)
se salen de la caja y estiran la página.

## Cómo se oye

Esperado; no se ha probado con un lector de pantalla.

- Al llegar a la caja: «Ranking de trámites, Corte al 30 de junio, región».
- Dentro: «Tabla, Ranking de trámites, 6 filas, 5 columnas». Al moverse por
  celdas, cada una se anuncia con su encabezado de columna y su encabezado de
  fila: «Bloqueantes, Trámite de ejemplo B, 1».

## Criterios WCAG

- **1.3.1 Información y relaciones.** `caption`, `th` con `scope`.
- **1.4.10 Reflujo.** Las tablas de datos son la excepción que la norma
  permite al desplazamiento en dos direcciones; aun así, se desplaza solo la
  tabla, no la página.
- **2.1.1 Teclado.** La caja que se desplaza recibe el foco.
- **1.4.12 Espaciado del texto.** Sin altura fija en celdas.

## Falta probar

- Lectores de pantalla: VoiceOver, NVDA y TalkBack
  ([#4](https://github.com/omad-mx/sistema-de-diseno/issues/4)). En especial,
  que el `caption` fijo no cambie cómo se anuncia la tabla, y que la variante
  apilable se siga anunciando como tabla. En el árbol de accesibilidad de
  Chromium, a 320 px, se conservan la tabla, sus filas, celdas y
  encabezados, y las etiquetas no se duplican.
- El texto alternativo vacío de las etiquetas (`content: … / ''`) es
  reciente; un navegador viejo lo ignora y lee la etiqueta junto con el
  encabezado de la columna.
- La sombra del borde en tema oscuro es más clara que el fondo y se nota
  menos que en claro. Aprobada así por ahora (2026-11-10).
- Ordenar y filtrar: el plan los deja para después (paso 4.3).
- Safari y Firefox. Hasta ahora solo se ha visto en Chromium: 320 px y
  escritorio, tema claro y oscuro, con y sin espaciado forzado.
