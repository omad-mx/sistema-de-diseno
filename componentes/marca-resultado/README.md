# Marca de resultado

Estado: `borrador`

## Qué es

Dice si un perfil completó el trámite sin ayuda o no. Lleva marca, texto y
color: una palomita en el color de la marca del sistema para
«completó», y un tache en el rojo de bloqueante para «no completó».

## Cuándo se usa

- En la franja y en la franja mini (pasos 3.2 y 3.3), una por perfil.
- En una tabla o un texto, cuando hay que decir el resultado de un perfil.

## Cuándo no

- **Para la gravedad de un hallazgo.** Eso es el distintivo de gravedad.
- **Para un resultado que no sea «completó» o «no completó».** No hay
  «parcial»: el sistema mide si una persona termina el trámite sin ayuda, y
  eso es sí o no.
- **Sin texto.** La marca puede ir sola a la vista, pero el texto siempre va
  en el HTML.

## Anatomía

```html
<!-- Con el texto a la vista -->
<span class="marca-resultado" data-resultado="si">Completó</span>

<!-- Solo la marca a la vista -->
<span class="marca-resultado" data-resultado="no">
  <span class="visualmente-oculto">No completó</span>
</span>
```

- `.marca-resultado`, con el resultado en `data-resultado` (`si` o `no`).
- La marca, antes del texto. La dibuja el CSS a partir de `data-resultado`:
  no se puede olvidar ni contradecir al texto.
- El texto, a la vista o dentro de `.visualmente-oculto`. Lo decide quien la
  usa: la franja lo esconde porque el perfil ya está nombrado en la celda.

## Variantes y estados

| `data-resultado` | Marca | Color |
|---|---|---|
| `si` | palomita | `completo` (petróleo) |
| `no` | tache | `no-completo` (rojo de bloqueante) |

La palomita reemplazó al círculo de la maqueta el 2026-11-10: el círculo ya
es «menor» en el distintivo de gravedad, y en grises, en alto contraste o
impreso se confundían. Ninguna forma del sistema se repite entre las dos
escalas.

No tiene variantes de tamaño: la marca mide lo que mide la letra que la
rodea. Si el texto a la vista ocupa dos líneas, la marca se queda junto a la
primera.

Sin `data-resultado`, o con uno que no existe, no hay marca ni color. Es un
error de marcado, y se nota.

No tiene estados: no es interactiva.

## Cómo se oye

Esperado; no se ha probado con un lector de pantalla.

- «Completó» o «No completó». La marca no se anuncia.

Fuera de la franja, el texto tiene que decir de quién es el resultado. Seis
«Completó» seguidos no dicen nada; «Lector de pantalla: no completó el
trámite», sí. Ese texto lo pone la franja (3.2).

## Criterios WCAG

- **1.4.1 Uso del color.** El resultado está en la forma y en el texto. El
  color lo acompaña. Es el par de color que la sección 4 del documento
  midió: petróleo contra rojo de bloqueante, 40.1 en el peor caso bajo
  simulación de visión cromática.
- **1.4.3 Contraste mínimo.** El contrato de contraste mide `completo` y
  `no-completo` sobre las tres superficies, en claro y en oscuro.
- **1.4.11 Contraste de elementos no textuales.** La marca usa el mismo color
  que el texto, que cumple 4.5:1.
- **1.3.1 Información y relaciones.** El resultado está en el texto, no solo
  en un atributo.

## Falta probar

- Lectores de pantalla: VoiceOver, NVDA y TalkBack
  ([#4](https://github.com/omad-mx/sistema-de-diseno/issues/4)).
- `forced-colors` en Windows. En la emulación de Chromium la marca se
  conserva, con el color de texto del sistema.
- Safari y Firefox. Hasta ahora solo se ha visto en Chromium: 320 px y
  escritorio, tema claro y oscuro, con y sin espaciado forzado.
