# Quién usa OMAD

Fecha: 2026-11-10 · Estado: `borrador`

El sistema de diseño se hace para personas concretas. Este documento dice
quiénes son, qué necesita cada una y qué parte de OMAD les sirve hoy. Sale de
una conversación de la dirección de diseño del 2026-11-10, al terminar la
fase 3 del [plan](plan-de-construccion.md).

---

## 1. Cuatro niveles

Son cuatro maneras de llegar a OMAD. Los dos primeros son el sitio público;
los dos últimos son el trabajo de quien audita y publica, y todavía no
tienen herramienta.

| Nivel | Quién | Qué busca | Qué usa | Existe hoy |
|---|---|---|---|---|
| **1. Quien visita** | Periodistas, ciudadanía, quien busca su trámite | Saber si un trámite se puede hacer y llevarse un dato citable | La portada, el ranking y la ficha de cada trámite | Los componentes, sí. Las páginas llegan en la fase 4. |
| **2. Quien revisa el detalle** | El consejo, prensa que investiga, la dependencia auditada | Saber por qué un trámite reprobó, dónde y con qué prueba | La ficha completa, con sus hallazgos | Los componentes, sí. Falta decidir si los hallazgos son públicos. |
| **3. Quien audita** | El equipo, al probar cada trámite con los seis perfiles | Registrar resultados y hallazgos con su captura | Una forma de capturar | No hay nada. |
| **4. Quien publica** | Quien revisa y sube las auditorías | Que una auditoría pase de revisada a publicada | Un lugar donde administrar las auditorías | No hay nada. |

### Nivel 1 · Quien visita

Llega desde una nota de prensa o una búsqueda, y quiere una respuesta corta:
¿este trámite se puede hacer sin ayuda? Se queda con la cifra o con la franja
de un trámite, y se va.

- **Lo que ve:** la cifra citable en la portada, el ranking (tabla apilable
  con el resultado por perfiles) y la franja de cada trámite.
- **Lo que necesita del sistema:** que la cifra se pueda citar tal cual, con
  su base y su fuente (sección 1 del [documento](omad-sistema-de-diseno.md)), y
  que todo funcione en un teléfono.

### Nivel 2 · Quien revisa el detalle

Quiere entender el resultado: qué falla, dónde, a quién le impide qué y con
qué prueba. Es el consejo, es la prensa que investiga, y es la dependencia
auditada cuando reclama.

- **Lo que ve:** la misma ficha que el nivel 1, más abajo: los hallazgos con
  su gravedad, sus criterios WCAG, los perfiles afectados y la captura.
- **Abierto:** si los hallazgos se publican en la ficha o se dan bajo pedido.
  El componente sirve en los dos casos (ver [`decisiones.md`](decisiones.md),
  «Abiertas»).
- **El consejo**, además, revisa una auditoría antes de que se publique. Eso
  es un paso del proceso, no una pantalla nueva: puede ser la misma ficha,
  sin publicar.

### Nivel 3 · Quien audita

Prueba cada trámite con los seis perfiles y registra lo que encuentra: qué
perfil completó el trámite, y cada hallazgo con su gravedad, sus criterios,
dónde está y una captura.

- **Lo que necesita:** una forma de capturar con la estructura de una
  auditoría (sección 2), para que lo capturado se pueda publicar sin
  reescribirlo.
- **Propuesta:** empezar con una hoja de cálculo con esas columnas. Es
  gratis, rápida y no hay que programar nada.

### Nivel 4 · Quien publica

Revisa lo capturado, lo aprueba y lo publica. Probablemente es la misma
herramienta que el nivel 3, con otro permiso.

- **Lo que necesita:** estados («en captura», «en revisión», «publicada»),
  cuentas y permisos.
- **Abierto:** si habrá un sistema de captura con base de datos o el sitio
  se genera de archivos. Es la decisión D5 del plan y el escenario B del
  documento de costos (en el repositorio interno).

---

## 2. Lo que une a los cuatro: el modelo de una auditoría

Cada auditoría tiene la misma forma:

- el trámite, su dependencia y la fecha;
- los seis perfiles, cada uno con su resultado (completó o no);
- la lista de hallazgos, cada uno con su gravedad, sus criterios WCAG, los
  perfiles a los que afecta, dónde está y su captura.

Si esa forma se escribe una vez, sirve para los cuatro niveles: quien audita
la captura (en una hoja de cálculo, hoy), el sitio se genera a partir de ella
(niveles 1 y 2), y si un día la hoja no alcanza, el sistema de captura se
construye sobre el mismo modelo sin cambiar el sitio.

Por eso es el siguiente paso: el **4.1** del plan, los datos de ejemplo,
escritos ya con esa forma y con una plantilla de hoja de cálculo para quien
audita.

---

## 3. Lo que esto cambia en el sistema de diseño

- **Niveles 1 y 2:** el catálogo ya los cubre. Tipografía, botón, distintivo
  de gravedad, marca de resultado, criterio WCAG, aviso, pictogramas, tabla,
  cabecera y pie, franja, resultado por perfiles, hallazgo y cifra citable.
- **Niveles 3 y 4:** si se construye una herramienta, le sirven los mismos
  colores, la misma tipografía, los botones, la tabla y el aviso. Pero le
  faltarían piezas que no están en el plan: **campos de formulario**,
  **mensajes de error**, **carga de archivos** (las capturas) y **estados de
  una auditoría**. Se agregan si se decide construirla.

---

## 4. Lo que falta decidir

| Decisión | Quién |
|---|---|
| ¿Los hallazgos se publican o se dan bajo pedido? | Dirección de diseño con el consejo |
| ¿Hoja de cálculo para quien audita, o un sistema de captura desde el principio? | Dirección de diseño con el equipo |
| ¿Quién aprueba una auditoría antes de publicarla? | Consejo |
| Qué mide el índice y cómo se ordena el ranking | Metodología y consejo (ver [`pendientes.md`](pendientes.md)) |
