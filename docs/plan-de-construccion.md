# Plan de construcción: del documento 0.1 a un prototipo funcional

Fecha: 2026-09-25 · Estado: `en discusión`

Este plan lleva el sistema de lo que es hoy (tokens, un script de contraste y
una maqueta) a una **fundación**. Una fundación aquí quiere decir tres cosas:
un catálogo de componentes documentados, un prototipo navegable del sitio de
OMAD armado solo con esos componentes, y verificación automática y manual de
que todo cumple lo que el sistema promete.

El sistema se construye **al mismo tiempo que las auditorías**. Mientras no
haya auditorías reales, el prototipo usa datos de ejemplo, con las reglas de
la sección 2.

Este documento dice qué se hace y en qué orden. Lo que falta hoy está en
[`pendientes.md`](pendientes.md), que apunta al paso en curso de este plan.

---

## 1. Decisiones que este plan necesita

Hay que tomarlas antes del paso que las necesita, no antes de empezar.

| # | Decisión | Antes del paso | Recomendación |
|---|---|---|---|
| D1 | Nombres de tokens: español o inglés ([#2](https://github.com/omad-mx/sistema-de-diseno/issues/2)) | 2.1 | **Decidida el 2026-09-27:** español, sin acentos y ñ → n. Ver [`decisiones.md`](decisiones.md). |
| D2 | ¿La franja se construye en el repositorio público antes de que el consejo decida si se registra como marca ([#3](https://github.com/omad-mx/sistema-de-diseno/issues/3))? | 3.2 | Pedirle al consejo que decida mientras se hacen las fases 1 y 2, que no la necesitan. Si no llega a tiempo, construirla y marcarla como propuesta. |
| D3 | ¿Quién dibuja los seis pictogramas? | 3.1 | La dirección de diseño, con los requisitos del paso 3.1. |
| D4 | Separar los tokens de las reglas base en dos archivos | 1.3 | Sí. Hoy `omad-tokens.css` mezcla las variables con reglas sobre `body`, `a` y el foco. |
| D5 | Páginas del prototipo escritas a mano, o generadas desde un archivo de datos | 4.1 | A mano mientras sean pocas. Generarlas cuando lleguen las auditorías reales, porque para entonces ya habrá muchas fichas. |

---

## 2. Datos de ejemplo

Dictamen del 2026-09-25, registrado en [`decisiones.md`](decisiones.md):
hasta que haya auditorías reales, el prototipo usa datos de ejemplo.

OMAD publica cifras para citarse. Una captura del prototipo puede circular
sin contexto, y si en ella aparece un trámite real reprobado, eso es una
acusación sin auditoría detrás. Por eso los datos de ejemplo siguen cuatro
condiciones:

1. **Todo es ficticio.** Ningún trámite, dependencia, dominio ni persona
   existe. Los nombres no se parecen a los reales: nada de «SAT» ni «IMSS»,
   tampoco con una letra cambiada.
2. **Cada página con datos de ejemplo lo avisa a la vista**, con el componente
   *aviso* (paso 2.6), no con una nota al pie.
3. **Todos los datos de ejemplo viven en un solo lugar**, en
   `prototipo/datos-de-ejemplo.md`. Así, cuando llegue la primera auditoría
   real, se sabe exactamente qué reemplazar.
4. **Los datos se diseñan para romper los componentes**, no para verse
   bonitos. Tienen que incluir 6 de 6 y 0 de 6, un trámite con un nombre muy
   largo, una ficha con muchos hallazgos y otra sin ninguno bloqueante.

El contenido que sí existe no se inventa. La metodología, los seis perfiles
y la tabla de visión cromática salen del documento del sistema.

---

## 3. Cómo queda el repositorio

Sin framework. HTML y CSS que se abren directo en el navegador, y
herramientas en Python sin dependencias, como la que ya existe.

```
tokens/
  omad-tokens.css         solo variables (capa 1 y capa 2)
estilos/
  base.css                reglas base: foco, enlaces, cuerpo, reflujo
  omad.css                importa tokens, base y todos los componentes
fuentes/                  Atkinson Hyperlegible Next y JetBrains Mono, con sus licencias OFL
iconos/perfiles/          los seis pictogramas en SVG
componentes/
  index.html              catálogo: todos los componentes en una página
  <nombre>/
    <nombre>.css
    ejemplo.html          todos sus estados y variantes
    README.md             su ficha (ver sección 5)
prototipo/
  datos-de-ejemplo.md
  index.html              portada
  ranking.html
  tramite-*.html          fichas de auditoría
  metodologia.html
herramientas/
  verificar-contraste.py  ya existe
  revisar-componentes.py  nuevo (paso 1.4)
```

El catálogo es la documentación del sistema. El prototipo demuestra que el
sistema alcanza para hacer el sitio.

---

## 4. Fases

Cada paso es un PR. Ningún paso empieza sin que el anterior esté en `main`,
salvo donde se dice que pueden ir en paralelo.

### Fase 0 · Cerrar lo abierto

- **0.1** Terminar el [PR #7](https://github.com/omad-mx/sistema-de-diseno/pull/7):
  `--omad-radio-1` a 8 px y el párrafo de la sección 7 del documento. Merge y
  cierre de [#1](https://github.com/omad-mx/sistema-de-diseno/issues/1).
- **0.2** Este plan, el dictamen de los datos de ejemplo y la lista de
  pendientes ([PR #8](https://github.com/omad-mx/sistema-de-diseno/pull/8)).

*Lista cuando:* los dos PR están en `main`.

### Fase 1 · Cimientos

Nada visible todavía. Al terminar esta fase, un componente nuevo ya tiene
dónde vivir, cómo documentarse y quién lo revisa.

- **1.1 Cómo se hace un componente.** `docs/como-se-hace-un-componente.md`:
  la estructura de carpeta, la plantilla del README y la lista de revisión de
  la sección 5.
- **1.2 Fuentes propias.** Atkinson Hyperlegible Next y JetBrains Mono en
  `fuentes/`, con sus licencias y `@font-face`. Solo los pesos que usa el
  sistema (400, 600 y 700). Sin servicios externos: el sitio no depende de
  Google Fonts.
- **1.3 Separar tokens y base** (D4). `tokens/omad-tokens.css` se queda solo
  con variables. Las reglas pasan a `estilos/base.css`, y `estilos/omad.css`
  importa todo. La utilidad `.visualmente-oculto` también va en la base.
- **1.4 Revisión automática de componentes.** `herramientas/revisar-componentes.py`
  lee todo el CSS de `componentes/` y falla si encuentra una primitiva (por
  ejemplo, `--omad-petroleo-600`), un color escrito a mano (hex, `rgb()` u
  `oklch()`) o un `outline: none` sin su `:focus-visible`. Entra a la CI junto
  al contrato de contraste. Así las reglas de `CLAUDE.md` dejan de depender de
  que alguien las recuerde.
- **1.5 Paleta única** ([#5](https://github.com/omad-mx/sistema-de-diseno/issues/5)).
  El script de contraste lee la paleta del CSS. Puede ir en paralelo con
  1.1–1.4.
- **1.6 Esqueletos.** `componentes/index.html` y `prototipo/index.html`
  vacíos, con la cabecera provisional de la maqueta, para ver cada componente
  en contexto desde el primer día.

*Lista cuando:* un PR con un color escrito a mano en `componentes/` falla en
la CI, y las fuentes cargan sin conexión a internet.

### Fase 2 · Elementos

Las piezas pequeñas, sin datos. Se extraen de la maqueta de #1: su marcado ya
existe y está probado a ojo, así que el trabajo es limpiarlo, documentarlo y
probarlo. Los pasos 2.2 a 2.6 pueden ir en paralelo después de 2.1.

- **2.1 Tipografía y prosa.** Encabezados h1 a h4, párrafo, listas, medida de
  66 caracteres, cejilla (el rótulo pequeño sobre un título) y entrada (el
  párrafo de apertura). Tiene que aguantar el espaciado forzado de 1.4.12.
- **2.2 Enlace y botón.** Botón primario y secundario, y el enlace que parece
  botón. Estados: reposo, encima, foco y activo. No hay botón deshabilitado:
  si algo no se puede hacer, se explica por qué.
- **2.3 Distintivo de gravedad.** Los cuatro niveles, cada uno con marca,
  texto y color, porque el color nunca va solo (sección 4 del documento).
- **2.4 Marca de resultado.** Completó (●) y no completó (×), con su texto
  para lector de pantalla. La usan la franja y la franja mini.
- **2.5 Criterio WCAG.** La referencia a un criterio (por ejemplo, 2.1.1),
  que enlaza a su explicación en la norma.
- **2.6 Aviso.** Una franja de texto para avisos de página. Su primer uso es
  «Datos de ejemplo».

*Lista cuando:* los seis están en el catálogo, cada uno con su ficha, y pasan
la lista de revisión de la sección 5.

### Fase 3 · Componentes

Las piezas que cargan el contenido de OMAD.

- **3.1 Pictogramas de los seis perfiles** (D3). Seis SVG en `iconos/perfiles/`,
  con estos requisitos:
  - Se reconocen a 24 px.
  - Se distinguen por silueta, no por color, y siguen distinguiéndose en blanco
    y negro.
  - Todos tienen el mismo grosor de trazo.
  - Nada de símbolos de discapacidad institucionales: ni la silla de ruedas
    del símbolo internacional de accesibilidad ni la oreja tachada.

  Los de la maqueta son bosquejos, un punto de partida.
- **3.2 Franja** (D2). Seis celdas en orden fijo, con pictograma, nombre y
  marca de resultado, más el titular «X de 6» como texto real. Un lector de
  pantalla la lee como lista de seis resultados (sección 5 del documento). En
  320 px de ancho no se corta ni se desborda: hay que diseñar qué hace.
- **3.3 Franja mini.** La versión de una línea para las tablas, con su
  etiqueta accesible «X de 6 perfiles completaron».
- **3.4 Hallazgo.** Distintivo de gravedad, descripción, criterios WCAG y
  perfiles afectados. Hay que resolver cómo se ve la evidencia: captura,
  fragmento de código en mono, o las dos.
- **3.5 Cifra citable.** El número grande, qué mide, la fecha de corte y un
  bloque «Cómo citar» con el texto listo para copiar. Es el primer trabajo del
  sistema, según la sección 1 del documento.
- **3.6 Tabla de datos.** Radio 0, cifras tabulares, `caption` obligatorio,
  desborde horizontal accesible con teclado, y encabezado de fila en la
  columna del trámite.
- **3.7 Cabecera, navegación y pie.** Sin JavaScript: en teléfono la
  navegación se acomoda en varias líneas en lugar de esconderse en un menú. Si
  eso no alcanza, se decide entonces.

*Lista cuando:* los siete están en el catálogo, con su ficha, y pasan la lista
de revisión.

### Fase 4 · Prototipo

Las páginas del sitio, armadas solo con componentes del catálogo. Si una
página necesita algo que el catálogo no tiene, se agrega primero al catálogo.
Ninguna página lleva estilos propios.

- **4.1 Datos de ejemplo** (sección 2). Unos 8 trámites ficticios y sus
  dependencias, con los casos límite a propósito. Se escriben antes de las
  páginas.
- **4.2 Portada.** La cifra citable, la entrada, las acciones y el resumen del
  ranking.
- **4.3 Ranking.** La tabla completa. Ordenar o filtrar se decide después;
  primero, estática.
- **4.4 Fichas de auditoría.** Tres: la mejor, la peor y la del nombre largo.
  Llevan metadatos, franja, hallazgos, evidencia y cómo citar.
- **4.5 Metodología.** Contenido real, del documento del sistema: los seis
  perfiles, la escala de gravedad y la tabla de visión cromática. Prueba la
  prosa larga.

*Lista cuando:* se puede navegar el sitio completo solo con teclado, y cada
página con datos de ejemplo lo avisa.

### Fase 5 · Verificación y versión 0.2

- **5.1 Revisión manual de cada página.** Solo teclado, zoom al 400% y 320 px
  de ancho, espaciado de texto forzado, tema oscuro, `forced-colors` (el modo
  de alto contraste de Windows) y `prefers-reduced-motion`.
- **5.2 Tecnologías de apoyo** ([#4](https://github.com/omad-mx/sistema-de-diseno/issues/4)):
  VoiceOver en macOS e iOS, NVDA en Windows y TalkBack en Android. Esta prueba
  requiere personas, no la puede hacer una herramienta. Lo que falle regresa
  al componente, no a la página.
- **5.3 Versión 0.2.** El documento del sistema se actualiza con lo aprendido,
  se etiqueta la versión en git y se registra en [`decisiones.md`](decisiones.md).

*Lista cuando:* el prototipo pasa 5.1 completo, y 5.2 está hecho o tiene sus
fallas registradas como issues. Esa es la fundación.

---

## 5. Lista de revisión de cada componente

Un componente entra al catálogo cuando:

- [ ] Su CSS usa solo tokens semánticos (lo revisa la CI desde el paso 1.4).
- [ ] Su `ejemplo.html` muestra todos sus estados y variantes, con los casos
      límite.
- [ ] Funciona solo con teclado y el foco se ve en todas sus partes.
- [ ] Aguanta 320 px de ancho, zoom al 400% y espaciado de texto forzado, sin
      cortar ni encimar texto.
- [ ] Se ve bien en tema claro, tema oscuro y `forced-colors`.
- [ ] Ningún significado depende solo del color.
- [ ] Sus objetivos táctiles miden al menos 44 × 44 px.
- [ ] Su README dice:
  - qué es y cuándo se usa (y cuándo no);
  - su anatomía;
  - cómo lo lee un lector de pantalla, escrito como se oye;
  - qué criterios WCAG cubre;
  - qué falta probar con tecnologías de apoyo.

Un componente que no pasa todo esto puede entrar a `main` con la etiqueta
`borrador` en su README, pero no se usa en el prototipo.
