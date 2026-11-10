# Hallazgo

Estado: `borrador`

## Qué es

Un problema encontrado en una auditoría: qué tan grave es, qué pasa, qué
criterios WCAG incumple, a qué perfiles afecta, dónde está y la captura de
pantalla que lo prueba. Va dentro de una lista de hallazgos, en la ficha de
cada trámite.

## Cuándo se usa

- En la ficha de auditoría de un trámite, uno por problema, del más grave al
  menos grave.

## Cuándo no

- **Para un resumen de varios problemas.** Eso es la franja o el resultado
  por perfiles.
- **Para un consejo de cómo arreglarlo.** El hallazgo dice qué pasa y lo
  prueba; no prescribe la solución.

## Anatomía

```html
<ul class="hallazgos" aria-label="Hallazgos">
  <li class="hallazgo" aria-labelledby="h-1">
    <span class="distintivo-gravedad" data-nivel="bloqueante">…</span>
    <p class="hallazgo-titulo" id="h-1">El botón de envío no es alcanzable con teclado.</p>
    <p class="hallazgo-descripcion">En el paso 3, el foco salta…</p>
    <dl class="hallazgo-datos">
      <dt>Criterios</dt><dd><a class="criterio-wcag" …>…</a></dd>
      <dt>Perfiles afectados</dt><dd>Lector de pantalla, solo teclado y motriz</dd>
      <dt>Dónde</dt><dd>Paso 3 de 5 · Datos de contacto</dd>
    </dl>
    <details class="hallazgo-evidencia">
      <summary class="boton" data-variante="terciario">Ver la evidencia</summary>
      <figure>
        <img src="…" width="…" height="…" alt="Qué se ve en la captura que prueba el hallazgo.">
        <figcaption>Captura del paso 3, tomada con el perfil «solo teclado» el …. <a href="…">Abrir la captura en tamaño completo</a>.</figcaption>
      </figure>
    </details>
  </li>
</ul>
```

- `.hallazgos`: la lista, con nombre.
- `.hallazgo`: un elemento de la lista, nombrado por su título.
- El distintivo de gravedad (2.3), primero.
- `.hallazgo-titulo`: qué pasa, en una frase. **No es un encabezado**: un `h3`
  por hallazgo mediría 28 px, demasiado para una frase, y las reglas de
  tipografía no dejan encoger un encabezado con una clase. La lista y el
  distintivo dan la estructura.
- `.hallazgo-descripcion`, opcional: el detalle y a quién le impide qué.
- `.hallazgo-datos`: una lista de definiciones con los criterios (componente
  2.5, con su separador), los perfiles afectados (por su nombre completo, en
  el orden fijo) y dónde está.
- `.hallazgo-evidencia`, opcional: la captura, plegada en un `details`. Se
  abre con el botón terciario «Ver la evidencia», sin JavaScript.

## Variantes y estados

No tiene variantes.

- **La evidencia es una captura de pantalla, sin fragmento de código**
  (dictamen del 2026-11-10). Va plegada: se abre y se cierra con el botón,
  con el ratón o con el teclado. Una flecha decorativa gira al abrir.
- **El texto alternativo de la captura describe lo que prueba**, no la página
  entera. El pie dice de qué paso es, con qué perfil y cuándo se tomó, y
  enlaza a la captura en tamaño completo, para quien necesita ampliarla.
- La captura lleva `width` y `height` para que la página no salte al abrirla.
- En un contenedor angosto, las etiquetas de los datos van arriba de su valor.

## Cómo se oye

Comprobado en el árbol de accesibilidad de Chromium; no se ha probado con un
lector de pantalla.

1. «El botón de envío no es alcanzable con teclado», elemento de lista.
2. «Gravedad: Bloqueante».
3. La frase y la descripción.
4. «Criterios: enlace, 2.1.1 Teclado (explicación en inglés)…». «Perfiles
   afectados: …». «Dónde: …».
5. «Ver la evidencia, botón, contraído». Al abrirlo, la descripción de la
   captura y su pie.

## Criterios WCAG

- **1.1.1 Contenido no textual.** La captura tiene texto alternativo que dice
  lo que prueba.
- **1.3.1 Información y relaciones.** Lista, lista de definiciones, figura con
  su pie.
- **1.4.1 Uso del color.** La gravedad lleva forma y nombre.
- **2.1.1 Teclado.** La evidencia se abre con el teclado (`summary` nativo).
- **1.4.4 Cambio de tamaño del texto** y **1.4.10 Reflujo.** La captura se
  puede abrir en tamaño completo; los datos se apilan en un ancho angosto.

## Falta probar

- **No está decidido si los hallazgos se publican** en la ficha del trámite
  o se dan bajo pedido (`docs/decisiones.md`, «Abiertas»). El componente
  sirve en los dos casos.
- **Una tabla única de números y nombres de criterios en español**, para que
  el mismo criterio no se llame distinto en cada hallazgo. Está en
  `docs/pendientes.md`; hoy los nombres se escriben a mano.
- Cómo se toman y se guardan las capturas reales: tamaño, formato, si se
  marcan como en el ejemplo, y quién escribe el texto alternativo. Es parte de
  la metodología, no del componente.
- Lectores de pantalla: VoiceOver, NVDA y TalkBack
  ([#4](https://github.com/omad-mx/sistema-de-diseno/issues/4)). En especial,
  cómo anuncia cada uno el `summary` con estilo de botón.
- Safari y Firefox. Hasta ahora solo se ha visto en Chromium: 320 px y
  escritorio, tema claro y oscuro, con y sin espaciado forzado, y
  `forced-colors` emulado.
