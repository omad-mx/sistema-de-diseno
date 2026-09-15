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
| [#1](https://github.com/omad-mx/sistema-de-diseno/issues/1) | Dirección visual: fría y contenida, o cálida y divulgativa | Consejo |
| [#2](https://github.com/omad-mx/sistema-de-diseno/issues/2) | Nombres de tokens en español o en inglés | Dirección de diseño |
| [#3](https://github.com/omad-mx/sistema-de-diseno/issues/3) | Registrar la franja de seis perfiles como marca | Consejo |
| [#4](https://github.com/omad-mx/sistema-de-diseno/issues/4) | Verificación con tecnologías de apoyo (no es una decisión: es trabajo pendiente que condiciona declarar conformidad) | Dirección de diseño |
| — | Que el consejo ratifique que este repositorio sea público | Consejo |

---

## Tomadas

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
