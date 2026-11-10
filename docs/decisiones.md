# Registro de decisiones

Una lista, cronológica, de arriba abajo. Cada entrada dice qué se decidió,
quién, por qué, y qué se descartó. Las decisiones abiertas viven como issues
con la etiqueta `decisión` y se pasan aquí cuando se cierran.

Una decisión registrada no se re-litiga sin un argumento que no estuviera en
la mesa cuando se tomó.

---

## Abiertas

| Issue | Decisión | Quién decide |
|---|---|---|
| [#3](https://github.com/omad-mx/sistema-de-diseno/issues/3) | Registrar la franja de seis perfiles como marca | Consejo |
| [#4](https://github.com/omad-mx/sistema-de-diseno/issues/4) | Verificación con tecnologías de apoyo (no es una decisión: es trabajo pendiente que condiciona declarar conformidad) | Dirección de diseño |
| — | Que el consejo ratifique que este repositorio sea público | Consejo |

---

## Tomadas

### 2026-11-10 · Sin franja mini: en una tabla, el resultado se escribe

**Decidió:** Daniel Ballinas, como dirección de diseño (paso 3.3 del plan,
[PR #19](https://github.com/omad-mx/sistema-de-diseno/pull/19)).
**Qué:** la franja mini (seis casillas con palomita o tache) no entra al
sistema. En una tabla con un trámite por fila, el resultado se escribe: «4 de
6 · no completaron: baja visión y cognitivo». Es el componente
`resultado-perfiles`.
**Por qué:** las casillas no tienen pictograma ni nombre; había que saberse
de memoria qué perfil era cada una o ir a una leyenda. Se comparó también una
columna por perfil, con el pictograma en el encabezado: resuelve eso en
escritorio, pero en un teléfono deja a la vista solo el nombre del trámite, y
cruzar fila y columna para cada dato es más carga cognitiva que leer una
frase.
**Se pierde:** comparar un mismo perfil entre muchos trámites de un vistazo.
Si hace falta, será una vista propia.

### 2026-11-10 · La franja: titular primero y dos filas de tres

**Decidió:** Daniel Ballinas, como dirección de diseño (paso 3.2 del plan,
[PR #18](https://github.com/omad-mx/sistema-de-diseno/pull/18)).
**Qué:**
- **Dos filas de tres celdas en todos los anchos**, no una fila de seis.
- **El titular «X de 6» va antes de las celdas**, no debajo.
**Por qué:** en un teléfono, una fila de seis obliga a encoger los nombres a
12 px y a partir «Cognitivo»; dos filas de tres caben a 320 px sin encoger
nada, y el orden se sigue leyendo de izquierda a derecha y de arriba abajo.
El titular primero da el resultado antes del detalle, a la vista y para
lector de pantalla.
**Cambia:** el diagrama de la sección 5 del documento del sistema.
**Sigue siendo:** una propuesta; su registro como marca lo decide el consejo
([#3](https://github.com/omad-mx/sistema-de-diseno/issues/3)).

### 2026-11-10 · La dirección de diseño decide y el consejo opina después

**Decidió:** Daniel Ballinas, como dirección de diseño.
**Qué:** por ahora, las decisiones de diseño no esperan al consejo. Se toman,
se construyen y se le enseñan al consejo para que dé su opinión. Lo primero
es la franja: se construye ya en el repositorio público, marcada como
propuesta (decisión D2 del plan), y el registro como marca
([#3](https://github.com/omad-mx/sistema-de-diseno/issues/3)) se lleva al
consejo con la franja hecha.
**Por qué:** #3 lleva desde el 2026-09-15 sin respuesta, y la fase 3 no
puede detenerse por eso. Al consejo le es más fácil opinar sobre algo que
puede ver que sobre una pregunta abstracta.
**Lo que no cambia:** el sistema sigue siendo una propuesta sin aprobación
del consejo, y así lo dice cada página.

### 2026-11-10 · Los pictogramas de los seis perfiles vienen de Lucide

**Decidió:** Daniel Ballinas, como dirección de diseño (paso 3.1 del plan,
[PR #16](https://github.com/omad-mx/sistema-de-diseno/pull/16)).
**Qué:** bocina (lector de pantalla), teclado (solo teclado), ojo (baja
visión), mano que señala (motriz), globo de texto (persona sorda) y cerebro
(cognitivo). Son íconos de [Lucide](https://lucide.dev), licencia ISC, sin
cambios en el dibujo. Están en `iconos/perfiles/`, con la licencia.
**Por qué de un set y no dibujados:** la decisión del 2026-10-31 (D3) pedía
dibujarlos con tiempo acotado a partir de los bosquejos de la maqueta. Un set
profesional cumple lo que pide el paso 3.1 (mismo trazo, misma retícula, se
reconocen a 24 px) sin el riesgo de unas formas orgánicas dibujadas a mano,
y en mucho menos tiempo. Los candidatos siguen las ideas de los bosquejos
donde funcionaban.
**Qué se descartó**, en [`maqueta-pictogramas.html`](maqueta-pictogramas.html):
para persona sorda, los subtítulos (un rectángulo, como el teclado; a 24 px
se confundían); de entrada, la silla de ruedas, la oreja tachada y la pieza
de rompecabezas.
**Pendiente:** si la franja se registra como marca
([#3](https://github.com/omad-mx/sistema-de-diseno/issues/3)), el consejo
tiene que saber que sus pictogramas vienen de un set público.

### 2026-11-10 · Marca de resultado, criterio WCAG y aviso

**Decidió:** Daniel Ballinas, como dirección de diseño (pasos 2.4 a 2.6 del
plan, [PR #15](https://github.com/omad-mx/sistema-de-diseno/pull/15)).
**Qué:**
- **«Completó» es una palomita, no un círculo.** El círculo ya es «menor» en
  el distintivo de gravedad, y en grises, en alto contraste o impreso se
  confundían. Palomita y tache se entienden en México sin explicación.
  Ninguna forma se repite entre la escala de gravedad y la de resultado.
- **Los criterios WCAG enlazan a las explicaciones del W3C, en inglés, por
  ahora.** No hay traducción oficial de WCAG 2.2 al español; la del W3C en
  español es de la 2.0. El destino en inglés se avisa con `hreflang` y con
  texto para lector de pantalla, y la página de ejemplo lo dice a la vista.
  Escribir explicaciones propias en español queda en
  [`pendientes.md`](pendientes.md).
- **El aviso es neutro y basta así.** No usa los colores de gravedad.

### 2026-11-10 · Los botones: tres variantes, y la única excepción al subrayado

**Decidió:** Daniel Ballinas, como dirección de diseño (paso 2.2 del plan,
[PR #14](https://github.com/omad-mx/sistema-de-diseno/pull/14)).
**Qué:**
- Hay tres botones: primario, secundario y terciario. El terciario es un
  botón que se ve como enlace, subrayado siempre, para acciones dentro de un
  bloque. Solo va sobre un `<button>`.
- **El primario y el secundario son los únicos enlaces sin subrayado del
  sistema.** Lo que dice que se pueden activar es su forma: contorno y
  relleno. Con el puntero encima se subrayan los tres.
**Por qué:** la regla del subrayado existe para que el color no sea lo único
que distingue un enlace del texto (WCAG 1.4.1). En el primario y el
secundario no lo es. En cambio, se descartó un botón «ghost» de texto de
color sin subrayado: ese sí se distinguiría del texto solo por el color.
**De paso:** el subrayado con el puntero encima se agregó porque el cambio de
relleno solo apenas se notaba (de 1.14 a 1.48 de contraste entre reposo y
encima), y en tema oscuro, sobre una superficie, el secundario no cambiaba
nada.

### 2026-11-10 · La marca de gravedad es una forma por nivel

**Decidió:** Daniel Ballinas, como dirección de diseño, «por ahora».
**Qué:** cada nivel lleva una forma rellena antes de su nombre: octágono para
bloqueante, triángulo para severa, rombo para moderada y círculo para menor.
La dibuja el CSS del distintivo a partir de `data-nivel`.
**Por qué lleva marca:** WCAG se cumple con el nombre escrito, pero un
hallazgo se busca recorriendo la lista con la vista. Sin el tono rojo
(daltonismo, alto contraste, impresión), el color deja de servir: en la
simulación de deuteranopia, bloqueante y moderada casi se confunden. Sin
marca, a esas personas solo les queda leer etiqueta por etiqueta.
**Qué se descartó**, en [`maqueta-marca-gravedad.html`](maqueta-marca-gravedad.html):
barras en escalera (se parecen a la señal del teléfono, donde más es mejor),
cuadros en fila (pueden leerse como calificación) y una mixta, con formas
rellenas para los graves y huecas para los demás.
**Lo que queda abierto:** el rombo y el círculo no dicen nada por sí mismos,
y el orden de los cuatro se aprende. Se revisa con las pruebas con personas
([#4](https://github.com/omad-mx/sistema-de-diseno/issues/4)).

### 2026-11-10 · El contrato de contraste se escribe con tokens semánticos

**Decidió:** Daniel Ballinas, como dirección de diseño
([#11](https://github.com/omad-mx/sistema-de-diseno/issues/11)).
**Qué:** el contrato de `herramientas/verificar-contraste.py` deja de listar
pares de primitivas (`tinta-900` sobre `tinta-0`) y lista pares de tokens
semánticos (`texto` sobre `fondo`). Cada par se mide en tema claro y en tema
oscuro. Lo que es texto, enlace, marca de resultado o etiqueta de gravedad se
mide sobre las tres superficies (`fondo`, `superficie` y `superficie-alta`)
con el mínimo de texto; el anillo de foco, el borde de control y el contorno
del botón, con el mínimo de lo no textual.
**Por qué:** los componentes solo pueden usar tokens semánticos, y el contrato
medía otra cosa. Apuntar `texto` a un gris claro dejaba el texto ilegible y la
CI pasaba en verde. Tres colores escritos directo en la capa 2 no se medían
nunca.
**De paso:**
- Esos tres colores pasan a la capa 1 con nombre: `blanco`, `severa-900` y
  `moderada-900`. Ningún valor cambió. La capa 2 ya solo admite `var()` a una
  primitiva.
- El script falla si los dos bloques del tema oscuro difieren, y si un token
  de color no está en ningún par ni en la lista de exentos.
- El único exento es `borde`: es una línea divisoria decorativa. Lo que
  delimita un control usa `borde-fuerte`, que sí se mide.

### 2026-11-09 · Los tokens y las reglas base viven en archivos distintos

**Decidió:** Daniel Ballinas, como dirección de diseño (decisión D4 del plan,
paso 1.3).
**Qué:** `tokens/omad-tokens.css` se queda solo con variables. Las reglas
sobre `body`, `a`, el foco y la utilidad `.visualmente-oculto` pasan a
`estilos/base.css`. Las fuentes se declaran en `estilos/fuentes.css` y se
sirven desde `fuentes/`, sin Google Fonts. Una página carga un solo archivo,
`estilos/omad.css`, que importa todo.
**Por qué:** un archivo de tokens que además pinta cosas no se puede reusar
sin arrastrar las reglas. Y el sitio de un observatorio de accesibilidad no
puede depender de un servicio externo para que su texto se vea.
**De paso:** la fase 1 del plan se hizo en un solo PR en vez de uno por paso
(1.2, 1.3, 1.4 y 1.6). Los pasos de plomería que no necesitan ojo de diseño
se agrupan; los que sí, siguen yendo uno por uno.

### 2026-11-05 · Los colores viven en el CSS y el script los verifica

**Decidió:** Daniel Ballinas, como dirección de diseño (paso 1.5 del plan,
[#5](https://github.com/omad-mx/sistema-de-diseno/issues/5)).
**Por qué:** la paleta estaba escrita dos veces y un cambio hecho solo en el
CSS pasaba verde. Ahora `herramientas/verificar-contraste.py` lee la capa 1 de
`tokens/omad-tokens.css`, así que no hay dos copias que puedan diferir.
**Se mantiene:** ningún color entra sin pasar el contrato.
**Reemplaza:** la entrada del 2026-09-09, «El script es la fuente de verdad de
los colores».

### 2026-11-03 · Convenciones de marcado de los componentes

**Decidió:** Daniel Ballinas, como dirección de diseño (paso 1.1 del plan,
[PR #9](https://github.com/omad-mx/sistema-de-diseno/pull/9)).
**Qué:**
- Las clases van sin prefijo: `.franja`, no `.omad-franja`. Las partes llevan
  el nombre del componente como prefijo (`.franja-celda`).
- Las variantes van en un atributo: `data-variante="secundario"`, no en una
  segunda clase.
- El estado se toma de ARIA y de las pseudoclases (`[aria-current]`,
  `:focus-visible`), nunca de una clase como `.activo`.

**Por qué:** el marcado se lee solo y no choca entre componentes. Y si el
estilo cuelga del mismo atributo que oye un lector de pantalla, lo que se ve
y lo que se oye no pueden contradecirse.
**Se reabre si:** otro sitio tiene que mezclar este CSS con el suyo y los
nombres chocan. Entonces se agrega el prefijo.
El detalle está en [`como-se-hace-un-componente.md`](como-se-hace-un-componente.md).

### 2026-10-31 · Los pictogramas de los seis perfiles los dibuja la dirección de diseño

**Decidió:** Daniel Ballinas, como dirección de diseño (decisión D3 del plan).
**Por qué:** nadie más en el colectivo dibuja por ahora.
**Condiciones:** tiempo acotado. Se parte de los bosquejos de la maqueta y se
cumplen los requisitos del paso 3.1 del
[plan](plan-de-construccion.md): se reconocen a 24 px, se distinguen por
silueta y no por color, tienen el mismo grosor de trazo y no usan símbolos de
discapacidad institucionales. Lo que no exijan esos requisitos no se pule.
Si alguien del colectivo que dibuje quiere retomarlos después, se reabre.

### 2026-09-27 · Los nombres se quedan en español, sin acentos y con ñ → n

**Decidió:** Daniel Ballinas, como dirección de diseño
([#2](https://github.com/omad-mx/sistema-de-diseno/issues/2), decisión D1 del
plan).
**Aplica a:** tokens, clases, archivos, carpetas y ramas.
**Por qué:**
- El vocabulario del sistema es el de la metodología (bloqueante, trámite,
  dependencia, perfil). Traducirlo pierde precisión y obliga a traducir de
  cabeza entre el documento y el código.
- Quien va a usar el sistema son equipos mexicanos y personas que quieran
  auditarlo.
- Sisdai, el sistema de referencia en México, hace lo mismo: sus variables,
  clases y archivos están en español (`--texto-secundario`, `.ancho-lectura`,
  `tipografia/parrafo.scss`).

Lo que es del lenguaje (`color`, `display`, `button`) sigue en inglés, porque
así es CSS.
**Regla de escritura:** sin acentos (`petroleo`, `tipografia`) y la ñ se
escribe n (`diseno`, `tamano`). Siempre así, para que nadie improvise;
Sisdai, por ejemplo, escribe `tamanio`.
**Se descartó:**
- El inglés.
- La mezcla de los dos, que es peor que cualquiera de los dos.

Si algún día hay contribución internacional, se publica un glosario
español-inglés; no se renombra nada.

### 2026-09-25 · El prototipo usa datos de ejemplo hasta que haya auditorías reales

**Decidió:** Daniel Ballinas, como dirección de diseño.
**Por qué:** el sistema se construye al mismo tiempo que las auditorías. Si
espera a tener resultados reales, se detiene. Y sin contenido que parezca
real, los componentes no se prueban.
**Condiciones:** todo lo de ejemplo es ficticio (trámites, dependencias,
dominios y personas, sin nombres parecidos a los reales); cada página que lo
usa lo avisa a la vista; vive en un solo archivo,
`prototipo/datos-de-ejemplo.md`; y el contenido que sí existe, como la
metodología, no se inventa. El detalle está en la sección 2 de
[`plan-de-construccion.md`](plan-de-construccion.md).
**Reemplaza:** la regla de `CLAUDE.md` que prohibía inventar datos para
ilustrar.

### 2026-09-20 · La dirección visual queda: fría, petróleo, radio 8 px, pictogramas, registro de oficio

**Decidió:** Daniel Ballinas, como dirección de diseño. El issue
[#1](https://github.com/omad-mx/sistema-de-diseno/issues/1) asignaba la
decisión al consejo; se reasigna porque el diseño de la experiencia es
competencia de la dirección de diseño, no del consejo.
**Con qué:** la maqueta `docs/maqueta-direccion-visual.html`, que muestra el
mismo contenido en la dirección de la 0.1 (A) y en una cálida y divulgativa
(B) con cinco controles independientes. La ratificada es A con dos cambios.
**Por qué:** el neutro frío y el petróleo se quedan; el registro de oficio se
queda porque la cifra tiene que poder citarse. El radio sube de 2 a 8 px y la
marca gráfica de cada perfil será un pictograma en vez del numeral de
posición.
**Se descartó:** el neutro cálido, la marca vino y el registro divulgativo.
De paso quedó demostrado, con `herramientas/paleta-direccion-b.py`, que una
marca naranja, terracota, ocre u oliva no es viable en ninguna dirección: todo
el arco 30°–160° queda por debajo de 21 ΔE76 contra bloqueante bajo
simulación de visión cromática. Eso no se re-litiga sin volver a correr el
barrido.
**Consecuencia:** cambiar `--omad-radio-1` a 8 px y el párrafo de la sección
7 del documento; los pictogramas de los seis perfiles son trabajo de
iconografía pendiente y condicionan la franja (los de la maqueta son
bosquejos). Con esto se levanta el bloqueo de `componentes/`.

### 2026-09-15 · El repositorio es público

**Decidió:** Daniel Ballinas.
**Por qué:** es la única forma gratuita de proteger la rama `main` en GitHub
(PR obligatorio, CI verde obligatoria, commits firmados), y un observatorio
que va a reprobar sitios ajenos gana credibilidad si su propio sistema es
verificable por cualquiera. La licencia Apache 2.0 ya apuntaba en esa
dirección desde el primer commit.
**Se descartó:** GitLab (tope de 5 usuarios en gratuito y aprobaciones que no
bloquean) y GitHub Team ($4 USD por usuario al mes). El detalle está en
`omad-mx/interno`.
**Consecuencia:** lo interno (costos, acuerdos, presupuestos) no va en este
repositorio. Va en `omad-mx/interno`, privado.
**Pendiente:** que el consejo lo ratifique.

### 2026-09-09 · El script es la fuente de verdad de los colores

**Superada** por la entrada del 2026-11-05.

**Decidió:** Daniel Ballinas.
**Por qué:** la CI verifica la constante `PALETA` de
`herramientas/verificar-contraste.py`, no el CSS. Si los dos difieren, manda
el script. Un cambio de color se hace en los dos archivos y se corre el script
antes de abrir el PR.
**Hueco conocido:** un cambio solo en el CSS pasa verde. Apuntado en
[#5](https://github.com/omad-mx/sistema-de-diseno/issues/5).

### 2026-09-09 · La escala de gravedad abandona el semáforo, y no hay verde de «completado»

**Decidió:** Daniel Ballinas, sobre las distancias CIE76 de la sección 4 del
documento.
**Por qué:** el semáforo rojo / naranja / ámbar / gris colapsaba bajo
protanopia y deuteranopia (peor par: 5.2, cuando por debajo de ~20 se
confunden). La escala actual separa por luminosidad y por familia además de
por tono y mantiene 21.0 en el peor caso de las tres simulaciones. Se probaron
seis verdes de «completado» y el mejor quedó en 13.9 contra el neutro cálido
de «moderada»; por eso completó / no completó se distingue por marca, texto y
azul de marca contra rojo bloqueante (40.1 en el peor caso).
**No se re-litiga** sin volver a correr las distancias.

### 2026-09-09 · Los seis perfiles no tienen color propio

**Decidió:** Daniel Ballinas.
**Por qué:** se distinguen por marca gráfica y por posición fija. Seis colores
categóricos habrían reintroducido el problema de la escala de gravedad y
habrían competido con ella en la misma pantalla. El único color en la franja
es el del eje completó / no completó.

### 2026-09-09 · Una sola familia tipográfica: Atkinson Hyperlegible

**Decidió:** Daniel Ballinas.
**Por qué:** diseñada para baja visión, y el observatorio compone su texto en
la tipografía hecha para las personas por las que audita. Resuelve la identidad
sin inventar una pareja tipográfica. Base de 18px (el cuerpo mínimo cómodo, no
el mínimo legal), escala 1.25.

### 2026-09-09 · Objetivo táctil mínimo de 44×44px

**Decidió:** Daniel Ballinas.
**Por qué:** WCAG 2.2 AA exige 24px (2.5.8). El sistema exige 44 porque el
mínimo legal es exactamente el tipo de conformidad de trámite que OMAD va a
criticar.

### 2026-09-09 · No se construyen componentes hasta ratificar la dirección visual

**Decidió:** Daniel Ballinas.
**Por qué:** la dirección es una propuesta abierta a que el consejo la tumbe.
Construir componentes antes es trabajo que se tira. El primero, cuando toque,
es la franja de seis perfiles.
