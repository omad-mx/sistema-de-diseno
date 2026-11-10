# Franja de seis perfiles

Estado: `borrador` · **propuesta, sin aprobación del consejo**

## Qué es

El componente firma del sistema: el titular «X de 6 perfiles completaron el
trámite sin ayuda» como texto real y, debajo, seis celdas en dos filas de
tres, una por perfil, siempre en el mismo orden, con su pictograma, su
nombre corto y su resultado.
Acompaña a cada trámite auditado. Su especificación está en la sección 5 del
[documento del sistema](../../docs/omad-sistema-de-diseno.md#5-los-seis-perfiles).

Si se registra como marca lo decide el consejo
([#3](https://github.com/omad-mx/sistema-de-diseno/issues/3)). Por ahora se
construye como propuesta (decisión del 2026-11-10).

## Cuándo se usa

- En la ficha de cada trámite auditado, una vez, cerca del título.
- En la portada, junto a la cifra citable, si se destaca un trámite.

## Cuándo no

- **En una tabla con un trámite por fila.** Ahí va el resultado por
  perfiles (paso 3.3), escrito.
- **Para menos de seis perfiles.** Si un perfil no se auditó, la franja no
  se usa hasta que se audite: la franja siempre son seis.
- **Con otro orden.** El orden es fijo en todas las páginas, en el informe
  impreso y en las gráficas.

## Anatomía

```html
<div class="franja">
  <p class="franja-resumen"><strong>2 de 6</strong> perfiles completaron el trámite sin ayuda.</p>
  <ul class="franja-celdas" role="list" aria-label="Resultado por perfil de uso">
    <li class="franja-celda">
      <svg class="franja-picto" aria-hidden="true" focusable="false">…</svg>
      <span class="franja-nombre" aria-hidden="true">Lector</span>
      <span class="marca-resultado franja-marca" data-resultado="no">
        <span class="visualmente-oculto">Lector de pantalla: no completó el trámite</span>
      </span>
    </li>
    <!-- …las otras cinco, en orden -->
  </ul>
</div>
```

- `.franja`: el bloque, con un ancho máximo de 36 rem para que las celdas no
  se estiren en una página ancha.
- `.franja-resumen`: el titular, primero, escrito en el HTML. Con un solo
  perfil va en singular: «1 de 6 perfiles completó el trámite sin ayuda».
- `.franja-celdas`: la lista, con `role="list"` (Safari quita la semántica de
  lista cuando no hay viñetas) y su nombre.
- `.franja-celda`: una por perfil, en el orden de la sección 5: lector de
  pantalla, solo teclado, baja visión, motriz, persona sorda, cognitivo.
- `.franja-picto`: el SVG de `iconos/perfiles/`, dentro del HTML para que
  tome el color del texto. Con `aria-hidden`.
- `.franja-nombre`: el nombre corto, con `aria-hidden`: el texto completo de
  la marca ya dice el perfil.
- La marca de resultado (componente 2.4), con el texto completo para lector
  de pantalla: «Perfil: completó / no completó el trámite».

## Variantes y estados

No tiene variantes. Comportamiento:

- Cada celda lleva en la base una barra del color de su resultado. Acompaña a
  la marca; no la sustituye.
- **Dos filas de tres en todos los anchos** (dictamen del 2026-11-10). El
  orden se lee de izquierda a derecha y de arriba abajo. Se eligió sobre una
  sola fila de seis, que en un teléfono obliga a encoger los nombres a 12 px.
- **El titular va antes de las celdas** (dictamen del 2026-11-10): primero el
  resultado, luego el detalle, a la vista y para lector de pantalla.
- Los nombres cortos se parten con guion si no caben (con el espaciado de
  texto forzado, «Cognitivo» no cabe en un tercio de 320 px).
- En `forced-colors` desaparecen la barra y las líneas entre celdas; las
  celdas se dibujan con un contorno.

## Cómo se oye

Comprobado en el árbol de accesibilidad de Chromium; no se ha probado con un
lector de pantalla.

1. «2 de 6 perfiles completaron el trámite sin ayuda».
2. «Resultado por perfil de uso, lista, 6 elementos».
3. «Lector de pantalla: no completó el trámite», y así los seis, en orden.

## Criterios WCAG

- **1.3.1 Información y relaciones.** Una lista de seis resultados, no una
  tabla de símbolos sueltos.
- **1.3.2 Secuencia significativa.** El orden del HTML es el orden fijo de
  los perfiles.
- **1.4.1 Uso del color.** El resultado está en la marca y en el texto; la
  barra de color lo acompaña.
- **1.4.10 Reflujo.** Dos filas de tres caben a 320 px sin encoger nada.
- **1.4.12 Espaciado del texto.** Los nombres se parten antes que salirse.

## Falta probar

- Lectores de pantalla: VoiceOver, NVDA y TalkBack
  ([#4](https://github.com/omad-mx/sistema-de-diseno/issues/4)).
- Safari y Firefox. Hasta ahora solo se ha visto en Chromium: 320 px y
  escritorio, tema claro y oscuro, con y sin espaciado forzado, y
  `forced-colors` emulado.
- Impresión.
