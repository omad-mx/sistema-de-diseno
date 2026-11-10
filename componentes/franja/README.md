# Franja de seis perfiles

Estado: `borrador` · **propuesta, sin aprobación del consejo**

## Qué es

El componente firma del sistema: seis celdas, una por perfil, siempre en el
mismo orden, con su pictograma, su nombre corto y su resultado, y el titular
«X de 6 perfiles completaron el trámite sin ayuda» como texto real.
Acompaña a cada trámite auditado. Su especificación está en la sección 5 del
[documento del sistema](../../docs/omad-sistema-de-diseno.md#5-los-seis-perfiles).

Si se registra como marca lo decide el consejo
([#3](https://github.com/omad-mx/sistema-de-diseno/issues/3)). Por ahora se
construye como propuesta (decisión del 2026-11-10).

## Cuándo se usa

- En la ficha de cada trámite auditado, una vez, cerca del título.
- En la portada, junto a la cifra citable, si se destaca un trámite.

## Cuándo no

- **En una tabla con muchas filas.** Ahí va la franja mini (paso 3.3).
- **Para menos de seis perfiles.** Si un perfil no se auditó, la franja no
  se usa hasta que se audite: la franja siempre son seis.
- **Con otro orden.** El orden es fijo en todas las páginas, en el informe
  impreso y en las gráficas.

## Anatomía

```html
<div class="franja">
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
  <p class="franja-resumen"><strong>2 de 6</strong> perfiles completaron el trámite sin ayuda.</p>
</div>
```

- `.franja`: el bloque. Es un contenedor: su ancho decide si las celdas van
  en una fila o en dos.
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
- `.franja-resumen`: el titular, escrito en el HTML. Con un solo perfil va en
  singular: «1 de 6 perfil completó el trámite sin ayuda».

## Variantes y estados

No tiene variantes. Comportamiento:

- Cada celda lleva en la base una barra del color de su resultado. Acompaña a
  la marca; no la sustituye.
- **En un contenedor de menos de 30 rem, dos filas de tres.** El orden se lee
  igual: de izquierda a derecha y de arriba abajo.
- Los nombres cortos se parten con guion si no caben (con el espaciado de
  texto forzado, «Cognitivo» no cabe en un tercio de 320 px).
- En `forced-colors` desaparecen la barra y las líneas entre celdas; las
  celdas se dibujan con un contorno.

## Cómo se oye

Comprobado en el árbol de accesibilidad de Chromium; no se ha probado con un
lector de pantalla.

1. «Resultado por perfil de uso, lista, 6 elementos».
2. «Lector de pantalla: no completó el trámite», y así los seis, en orden.
3. «2 de 6 perfiles completaron el trámite sin ayuda».

## Criterios WCAG

- **1.3.1 Información y relaciones.** Una lista de seis resultados, no una
  tabla de símbolos sueltos.
- **1.3.2 Secuencia significativa.** El orden del HTML es el orden fijo de
  los perfiles, en una fila o en dos.
- **1.4.1 Uso del color.** El resultado está en la marca y en el texto; la
  barra de color lo acompaña.
- **1.4.10 Reflujo.** Dos filas de tres en lugar de seis celdas aplastadas.
- **1.4.12 Espaciado del texto.** Los nombres se parten antes que salirse.

## Falta probar

- **Qué hace a 320 px:** el ejemplo compara dos filas de tres (lo que está en
  el CSS) con las seis encogidas de la maqueta. Lo decide la dirección de
  diseño.
- Si el titular va antes o después de las celdas. Hoy va después, como en el
  documento; para un lector de pantalla, oír primero «2 de 6» podría ser más
  claro.
- Lectores de pantalla: VoiceOver, NVDA y TalkBack
  ([#4](https://github.com/omad-mx/sistema-de-diseno/issues/4)).
- Safari y Firefox. Hasta ahora solo se ha visto en Chromium: 320 px y
  escritorio, tema claro y oscuro, con y sin espaciado forzado, y
  `forced-colors` emulado.
- Impresión.
