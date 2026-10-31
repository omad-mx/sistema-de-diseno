# Cómo se hace un componente

Fecha: 2026-10-31 · Estado: `borrador`

Esta es la receta que siguen todos los componentes del sistema, de la
distinción de gravedad a la franja. Dice dónde vive un componente, cómo se
escribe, cómo se documenta y qué tiene que pasar para entrar al catálogo. Es
el paso 1.1 del [plan de construcción](plan-de-construccion.md).

Aquí «componente» incluye a los elementos de la fase 2 (botón, distintivo,
aviso…) y a los componentes de la fase 3 (franja, hallazgo, tabla…). Todos se
hacen igual.

---

## 1. Antes de empezar

- **Que una página lo necesite.** Un componente existe porque el prototipo o
  el sitio lo usa, no por completar un catálogo. Si una página necesita algo
  que el catálogo no tiene, primero se agrega al catálogo y después se usa.
- **Que no exista ya.** Si se parece a algo que ya está, se extiende eso con
  una variante en lugar de hacer uno nuevo.
- **Que tenga de dónde salir.** Casi todo ya está bosquejado en la
  [maqueta de la dirección visual](maqueta-direccion-visual.html). Se parte
  de ese marcado: el trabajo es limpiarlo, documentarlo y probarlo, no
  rediseñarlo.

## 2. La carpeta

Cada componente vive en su propia carpeta dentro de `componentes/`:

```
componentes/
  <nombre>/
    <nombre>.css     sus estilos, y nada más
    ejemplo.html     todos sus estados y variantes, con los casos límite
    README.md        su ficha (sección 6)
```

El nombre va en español, en singular, sin acentos, con ñ → n y con guiones
entre palabras: `franja`, `franja-mini`, `cifra-citable`, `distintivo-gravedad`.
Es el mismo en la carpeta, en los archivos, en la clase y en la rama
(`componentes/<nombre>`).

## 3. El HTML

- **Primero el elemento nativo.** Un botón es un `<button>`, un enlace es un
  `<a href>`, una lista de resultados es una `<ul>`. ARIA solo se usa cuando
  no hay un elemento que lo resuelva, y entonces se documenta por qué.
- **El texto es texto.** Una cifra, un titular o un resultado nunca va dentro
  de una imagen ni se genera con `content:` en CSS si alguien necesita leerlo.
- **Sin JavaScript, mientras se pueda.** Si un componente lo necesita, tiene
  que funcionar sin él (se ve el contenido completo, aunque no se pueda
  plegar ni filtrar) y el README explica qué agrega el script.
- **Lo que solo es para lector de pantalla** usa `.visualmente-oculto` (llega
  a las reglas base en el paso 1.3), nunca
  `display: none` ni `aria-label` sobre un elemento que ya tiene texto visible
  distinto.

## 4. El CSS

- **Solo tokens semánticos** (capa 2 de `tokens/omad-tokens.css`). Nunca una
  primitiva como `--omad-petroleo-600`, nunca un hex, `rgb()` ni `oklch()`
  escrito a mano. Desde el paso 1.4 la CI lo revisa.
- **Si falta un token, se agrega en el mismo PR**, en la capa 2. Si es un
  color, también se agrega al par correspondiente del script de contraste y
  se corre antes de abrir el PR.
- **La clase raíz es el nombre del componente**: `.franja`. Sus partes llevan
  el nombre como prefijo: `.franja-celda`, `.franja-marca`. Así ningún
  componente pisa a otro.
- **Las variantes van en un atributo**, no en otra clase:
  `<a class="boton" data-variante="secundario">`. Se leen solas en el
  marcado y no chocan con otras clases.
- **El estado se toma del HTML, no de una clase.** `:hover`, `:focus-visible`,
  `[aria-current]`, `[aria-expanded]`, `:checked`. Así lo que se ve y lo que
  oye un lector de pantalla no pueden contradecirse.
- **El foco no se redefine.** El anillo de doble capa ya está en las reglas base y
  funciona sobre cualquier superficie. Un componente solo lo toca si su forma
  lo obliga, y entonces lo explica en el README.
- **El ancho lo decide el contenedor, no la pantalla.** Para que un componente
  funcione igual en una columna angosta y en la página completa, se usan
  consultas de contenedor (`@container`) en lugar de `@media` por ancho de
  pantalla. `@media` se queda para las preferencias de la persona:
  `prefers-color-scheme`, `prefers-reduced-motion`, `forced-colors`.
- **Nada de alturas fijas** en contenedores de texto, ni `!important`.
- **Propiedades lógicas** (`margin-inline`, `padding-block`) en lugar de
  `left`, `right`, `top` y `bottom`.

## 5. El ejemplo

`ejemplo.html` es una página que se abre directo en el navegador, sin
servidor. Carga los tokens con una ruta relativa y el CSS del componente, y
nada más:

```html
<link rel="stylesheet" href="../../tokens/omad-tokens.css">
<link rel="stylesheet" href="<nombre>.css">
```

Tiene una sección por estado y por variante, cada una con su encabezado. Y
tiene los casos que rompen: el texto más largo que pueda llegar, el valor
mínimo y el máximo (0 de 6 y 6 de 6), un nombre de trámite de tres líneas.
Un ejemplo que solo muestra el caso bonito no prueba nada.

Mientras no existan los datos de ejemplo del prototipo (paso 4.1), los
ejemplos usan texto genérico que no se parezca a ningún trámite ni
dependencia real. Las reglas de la sección 2 del plan aplican aquí también.

## 6. La ficha

El `README.md` de cada componente sigue esta plantilla. Se copia completa y
se llenan todas las secciones; si una no aplica, se dice por qué.

```markdown
# <Nombre del componente>

Estado: `borrador` | `listo`

## Qué es

Una o dos frases. Qué muestra y para qué.

## Cuándo se usa

- …

## Cuándo no

- … (y qué se usa en su lugar)

## Anatomía

Las partes, en el orden en que aparecen en el HTML, con su clase.

## Variantes y estados

Cada variante con su `data-variante`, y cada estado con lo que lo activa.

## Cómo se oye

Lo que dice un lector de pantalla, escrito como se oye y en orden, de entrar
al componente a salir de él. Si se probó con un lector concreto, se dice
cuál y en qué versión; si no se ha probado, se escribe lo que se espera y se
marca como «esperado».

## Criterios WCAG

Los criterios que este componente ayuda a cumplir, con su número, y cómo.

## Falta probar

Lo que no se ha probado con tecnologías de apoyo (#4). Esta sección no se
borra: si ya se probó todo, dice con qué y cuándo.
```

## 7. Lista de revisión

Un componente entra al catálogo como `listo` cuando:

- [ ] Su CSS usa solo tokens semánticos.
- [ ] Su `ejemplo.html` muestra todos sus estados y variantes, con los casos
      límite.
- [ ] Funciona solo con teclado y el foco se ve en todas sus partes.
- [ ] Aguanta 320 px de ancho, zoom al 400 % y espaciado de texto forzado
      (WCAG 1.4.12), sin cortar ni encimar texto.
- [ ] Se ve bien en tema claro, tema oscuro y `forced-colors`.
- [ ] Ningún significado depende solo del color.
- [ ] Sus objetivos táctiles miden al menos 44 × 44 px.
- [ ] Su ficha está completa.

Un componente que no pasa todo esto puede entrar a `main` como `borrador`,
pero no se usa en el prototipo.

## 8. Cómo entra

1. Una rama `componentes/<nombre>` desde `main`.
2. Un PR por componente, con la lista de revisión copiada en la descripción y
   marcada.
3. La CI en verde: contraste y, desde el paso 1.4, la revisión de
   componentes.
4. El componente se agrega al catálogo (`componentes/index.html`, desde el
   paso 1.6).
5. Si el componente obligó a tomar una decisión que vale para todo el
   sistema, se registra en [`decisiones.md`](decisiones.md) y, si cambia esta
   receta, se cambia aquí en el mismo PR.
