# Criterio WCAG

Estado: `borrador`

## Qué es

La referencia a un criterio de éxito de WCAG 2.2, con su número y su nombre,
que enlaza a su explicación en el sitio del W3C.

## Cuándo se usa

- En un hallazgo, después de su descripción: el criterio que se incumple.
- En la metodología, cuando se cita un criterio.
- En una tabla, en su versión compacta.

## Cuándo no

- **Dentro de una oración.** Ahí va un enlace normal, escrito como parte del
  texto: «incumple el criterio [2.1.1 Teclado]». El componente tiene un
  objetivo de 44 px de alto y abriría el renglón.
- **Para citar la norma completa** o una pauta (2.1, sin tercer número). Eso
  es un enlace normal.

## Anatomía

```html
<a class="criterio-wcag" href="https://www.w3.org/WAI/WCAG22/Understanding/keyboard.html" hreflang="en">
  <span class="criterio-wcag-numero">2.1.1</span>
  <span class="criterio-wcag-nombre">Teclado</span>
  <span class="visualmente-oculto"> (explicación en inglés)</span>
</a>
```

- `.criterio-wcag`: el enlace. Va subrayado, como todo enlace.
- `.criterio-wcag-numero`: el número, en cifras tabulares y peso medio.
- `.criterio-wcag-nombre`: el nombre en español.
- «(explicación en inglés)», solo para lector de pantalla, y `hreflang="en"`:
  el destino está en inglés y hay que avisarlo antes de llegar.

Si van varios seguidos, entre uno y otro va
`<span class="criterio-wcag-separador" aria-hidden="true">·</span>`. Sin
separador, los subrayados se juntan y no se ve dónde termina uno.

## Variantes y estados

| Variante | Cómo se pide | Qué se ve |
|---|---|---|
| Con nombre | sin atributo | «2.1.1 Teclado» |
| Compacto | `data-variante="compacto"` | «2.1.1» |

En el compacto, el nombre sigue dentro del enlace para lector de pantalla:
«2.1.1» solo no dice a dónde lleva.

Los estados son los de cualquier enlace (reglas base): visitado, puntero
encima (el subrayado engruesa) y foco.

El enlace mide 44 px de alto sin altura fija: el relleno completa lo que le
falta a una línea, y si el nombre ocupa dos, crece.

## Cómo se oye

Comprobado en el árbol de accesibilidad de Chromium; no se ha probado con un
lector de pantalla.

- «Enlace, 2.1.1 Teclado (explicación en inglés)». Igual en la versión
  compacta.
- El separador no se anuncia.

## Criterios WCAG

- **2.4.4 Propósito de los enlaces.** El nombre del criterio va siempre en el
  enlace, aunque no se vea. Un enlace que solo dice «2.1.1» sería el mismo
  hallazgo «menor» que OMAD va a reportar.
- **3.1.2 Idioma de las partes.** El destino en inglés se avisa.
- **2.5.8 Tamaño del objetivo.** 44 px de alto.
- **1.4.1 Uso del color.** Subrayado.

## Falta probar

- **Los enlaces van a las explicaciones del W3C, que están en inglés, por
  ahora** (dictamen del 2026-11-10). No hay traducción oficial de WCAG 2.2
  al español; la del W3C en español es de la 2.0. Escribir explicaciones
  propias en español está en `docs/pendientes.md`. El ejemplo lo avisa
  arriba.
- Los nombres en español de los criterios son traducción nuestra, a falta de
  la oficial. Conviene una tabla única de números y nombres para que no se
  traduzcan distinto en cada página.
- Lectores de pantalla: VoiceOver, NVDA y TalkBack
  ([#4](https://github.com/omad-mx/sistema-de-diseno/issues/4)). En especial,
  que el número se lea como número y no como fecha.
- Safari y Firefox. Hasta ahora solo se ha visto en Chromium: 320 px y
  escritorio, tema claro y oscuro, con y sin espaciado forzado.
