# Cabecera

Estado: `borrador`

## Qué es

Lo primero de cada página: el enlace para saltar al contenido, la marca de
OMAD (que lleva a la portada) y la navegación principal.

## Cuándo se usa

- En todas las páginas del sitio, una vez.

## Cuándo no

- **En las páginas de ejemplo del catálogo.** Esas tienen su andamio.
- **Para la navegación dentro de una página** (un índice de secciones). Eso
  es otra lista de enlaces.

## Anatomía

```html
<a class="cabecera-saltar" href="#contenido">Saltar al contenido</a>
<header class="cabecera">
  <a class="cabecera-marca" href="/">
    <span class="cabecera-sigla">OMAD</span>
    <span class="cabecera-nombre">Observatorio Mexicano de Accesibilidad Digital</span>
  </a>
  <nav class="cabecera-nav" aria-label="Principal">
    <ul>
      <li><a href="/tramites">Trámites</a></li>
      <li><a href="/ranking" aria-current="page">Ranking</a></li>
    </ul>
  </nav>
</header>
<main id="contenido" tabindex="-1">…</main>
```

- `.cabecera-saltar`: el primer elemento de la página, antes del `header`.
  Fuera de la vista hasta que recibe el foco. Lleva al `main`, que tiene
  `tabindex="-1"` para que el foco llegue de verdad.
- `.cabecera`: el `header` de la página.
- `.cabecera-marca`: el enlace a la portada, con `.cabecera-sigla` y
  `.cabecera-nombre`. La barra petróleo bajo la sigla es decorativa (CSS).
- `.cabecera-nav`: la navegación principal, una lista de enlaces.

## Variantes y estados

No tiene variantes.

- La página actual lleva `aria-current="page"`: va en color de texto y con
  el subrayado grueso. Cambian el color y el grosor, no solo el color.
- Sin JavaScript y sin menú escondido: en un teléfono la navegación se
  acomoda en varias líneas. Con siete secciones a 320 px ocupa cuatro
  renglones. Si un día no alcanza, se decide entonces (paso 3.7 del plan).
- Con el puntero encima de la marca, el nombre se subraya.

## Cómo se oye

Esperado; no se ha probado con un lector de pantalla.

- Primer tabulador: «Saltar al contenido, enlace».
- «Banner». «OMAD Observatorio Mexicano de Accesibilidad Digital, enlace».
- «Principal, navegación, lista, 4 elementos». «Ranking, página actual,
  enlace».

## Criterios WCAG

- **2.4.1 Evitar bloques.** El enlace para saltar al contenido.
- **1.3.1 Información y relaciones.** `header`, `nav` con nombre, lista.
- **2.4.8 Ubicación** (AAA). `aria-current="page"`, que se ve y se oye.
- **2.5.8 Tamaño del objetivo.** Los enlaces miden 44 px de alto.
- **1.4.10 Reflujo.** La navegación se acomoda, no se esconde.
- **3.2.3 Navegación coherente.** La misma cabecera, en el mismo orden, en
  todas las páginas.

## Falta probar

- **La marca es un enlace sin subrayado**, como en la maqueta. La regla del
  subrayado tiene una sola excepción escrita, los botones. Una marca que
  lleva a la portada no está dentro de un texto, así que no choca con 1.4.1,
  pero hay que decidir si se escribe como segunda excepción.
- Lectores de pantalla: VoiceOver, NVDA y TalkBack
  ([#4](https://github.com/omad-mx/sistema-de-diseno/issues/4)).
- Safari y Firefox. Hasta ahora solo se ha visto en Chromium: 320 px y
  escritorio, tema claro y oscuro, con y sin espaciado forzado. El enlace
  para saltar se probó con el teclado: aparece con el primer tabulador y
  Enter lleva el foco al contenido.
