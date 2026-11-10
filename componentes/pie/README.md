# Pie

Estado: `borrador`

## Qué es

El final de cada página: enlaces secundarios (metodología, datos abiertos,
contacto) y la línea de créditos.

## Cuándo se usa

- En todas las páginas del sitio, una vez.

## Cuándo no

- **Para la navegación principal.** Esa va en la cabecera.
- **Para notas de una tabla o de una cifra.** Van junto a lo que explican.

## Anatomía

```html
<footer class="pie">
  <nav class="pie-nav" aria-label="Pie">
    <ul>
      <li><a href="/metodologia">Metodología</a></li>
    </ul>
  </nav>
  <p class="pie-creditos">Sistema de diseño versión 0.1 · sin aprobación del consejo</p>
</footer>
```

- `.pie`: el `footer` de la página.
- `.pie-nav`: una lista de enlaces, con nombre («Pie»), para que no se
  confunda con la navegación principal.
- `.pie-creditos`: un párrafo.

## Variantes y estados

No tiene variantes. Los enlaces a la izquierda y los créditos a la derecha;
si no caben juntos, los créditos bajan. Los enlaces miden 44 px de alto.

## Cómo se oye

Esperado; no se ha probado con un lector de pantalla.

- «Información de contenido» (el `footer`). «Pie, navegación, lista, 3
  elementos». Luego los créditos.

## Criterios WCAG

- **1.3.1 Información y relaciones.** `footer`, `nav` con nombre, lista.
- **2.5.8 Tamaño del objetivo.** 44 px de alto.
- **1.4.10 Reflujo.** Se acomoda en varias líneas.

## Falta probar

- Lectores de pantalla: VoiceOver, NVDA y TalkBack
  ([#4](https://github.com/omad-mx/sistema-de-diseno/issues/4)).
- Safari y Firefox. Hasta ahora solo se ha visto en Chromium: 320 px y
  escritorio, tema claro y oscuro, con y sin espaciado forzado.
