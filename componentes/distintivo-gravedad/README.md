# Distintivo de gravedad

Estado: `borrador`

## Qué es

La etiqueta que dice qué tan grave es un hallazgo. Son cuatro niveles:
bloqueante, severa, moderada y menor. Cada uno lleva tres señales a la vez:
una marca, su nombre en texto y su color.

## Cuándo se usa

- Junto a un hallazgo de una auditoría, al inicio.
- En la metodología, para explicar la escala.

## Cuándo no

- **Para el resultado de un perfil** (completó o no completó). Eso es la
  marca de resultado (paso 2.4 del plan).
- **Para un estado que no sea gravedad** («nuevo», «en revisión»). La escala
  tiene cuatro niveles y no se le agregan.
- **Sin el nombre.** La marca sola, o el color solo, no son el distintivo.

## Anatomía

```html
<span class="distintivo-gravedad" data-nivel="severa">
  <span class="visualmente-oculto">Gravedad: </span>Severa
</span>
```

- `.distintivo-gravedad`: la caja, con el color del nivel.
- La marca: una forma rellena, antes del texto. La dibuja el CSS a partir de
  `data-nivel`; no hay que escribirla en el HTML, así que no se puede
  olvidar ni contradecir al texto.
- «Gravedad: », solo para lector de pantalla. Fuera de contexto, «severa» no
  dice de qué se habla.
- El nombre del nivel, escrito normal. Las mayúsculas las pone el CSS.

## Variantes y estados

El nivel va en `data-nivel`, no en `data-variante`: no es una manera de verse,
es el dato.

| `data-nivel` | Marca |
|---|---|
| `bloqueante` | octágono, la señal de alto |
| `severa` | triángulo, la señal de precaución |
| `moderada` | rombo |
| `menor` | círculo |

La marca se eligió el 2026-11-10 entre cuatro propuestas (barras en
escalera, cuadros en fila, una forma por nivel y una mixta), en
[`docs/maqueta-marca-gravedad.html`](../../docs/maqueta-marca-gravedad.html).
Las barras se descartaron porque se parecen a la señal del teléfono, donde
más barras es mejor. El octágono y el triángulo ya significan peligro; el
rombo y el círculo no dicen nada por sí mismos, y el orden de los cuatro se
aprende.

Sin `data-nivel`, o con un nivel que no existe, el distintivo se queda sin
color y sin marca. Es un error de marcado, y se nota.

No tiene estados: no es interactivo. No se parte en dos líneas; si no cabe
junto al texto, baja completo.

El distintivo mide lo que mide su texto. Alinear una columna de distintivos
le toca a quien los contiene (el componente hallazgo, paso 3.4).

## Cómo se oye

Esperado; no se ha probado con un lector de pantalla.

- «Gravedad: severa».

La marca no se anuncia: es un dibujo del CSS, y el nivel ya está dicho.

## Criterios WCAG

- **1.4.1 Uso del color.** Es la razón de ser del componente: el nivel se lee
  en el texto y en la marca, y el color lo acompaña. Sin color (impreso en
  blanco y negro, o en `forced-colors`) se sigue entendiendo.
- **1.4.3 Contraste mínimo.** El contrato de contraste mide el texto de cada
  nivel sobre su fondo, en claro y en oscuro. La marca usa el mismo color que
  el texto.
- **1.3.1 Información y relaciones.** El nivel está en el texto, no solo en
  un atributo ni en una clase.
- **1.4.12 Espaciado del texto.** Sin ancho ni alto fijos.

## Falta probar

- Lectores de pantalla: VoiceOver, NVDA y TalkBack
  ([#4](https://github.com/omad-mx/sistema-de-diseno/issues/4)).
- `forced-colors` en Windows. En la emulación de Chromium la marca y el
  contorno se conservan.
- Que la marca se entienda sin explicación: que el octágono y el triángulo
  se lean como lo más grave, y que la gente aprenda el orden de los cuatro.
  Es una prueba con personas.
- Las distancias de color de la sección 4 del documento se calcularon para
  las etiquetas sobre el fondo de la página, no para el texto de un nivel
  sobre su propio fondo. No se han vuelto a correr para este uso; por eso el
  distintivo no depende del color.
- Safari y Firefox. Hasta ahora solo se ha visto en Chromium: 320 px y
  escritorio, tema claro y oscuro, con y sin espaciado forzado.
- Impresión.
