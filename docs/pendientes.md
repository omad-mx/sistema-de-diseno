# Pendientes

Fecha: 2026-11-10 · Estado: vivo

Lo que falta ahora, en el orden en que conviene hacerlo. El camino completo
está en [`plan-de-construccion.md`](plan-de-construccion.md); esta lista
muestra el tramo en curso. El detalle vive en su issue o PR, no aquí.

Al terminar algo, se borra de esta lista. Si fue una decisión, pasa a
[`decisiones.md`](decisiones.md), y el historial queda en git.

---

## En curso

Nada. La fase 3 (componentes) está completa: pictogramas, franja, resultado
por perfiles (en lugar de la franja mini), hallazgo, cifra citable, tabla de
datos (con su variante apilable), cabecera y pie están en el
[catálogo](../componentes/index.html), todos como `borrador` hasta que se
prueben con tecnologías de apoyo. A quién sirve cada parte está en
[`quien-usa-omad.html`](quien-usa-omad.html).

## Siguiente: fase 4 del plan, prototipo

1. **El modelo de una auditoría y los datos de ejemplo** (4.1). La forma de
   una auditoría (trámite, perfiles, hallazgos) escrita una vez, los datos de
   ejemplo con esa forma, y una plantilla de hoja de cálculo para quien
   audita. Es lo que une a los cuatro niveles de
   [`quien-usa-omad.html`](quien-usa-omad.html).
2. **Portada** (4.2), **ranking** (4.3), **fichas de auditoría** (4.4) y
   **metodología** (4.5).

## Herramientas

- **Escala de radio al revés:** `--omad-radio-1` es 8 px y `--omad-radio-2`
  sigue en 4. Nadie usa el 2 todavía; se define cuando un componente lo pida.

## Diseño

- **La marca de OMAD en la cabecera es provisional.** La sigla con su barra
  es un lugar para el logo, que todavía no existe. Si el enlace a la portada
  lleva subrayado o es una excepción a la regla se decide con el logo.

## Metodología

- **Qué mide el índice.** Si un trámite «pasa» solo cuando lo completan los
  seis perfiles o si se cuenta cada combinación de trámite y perfil; si se
  pondera por cuánta gente usa cada trámite; y desde qué base tiene sentido
  dar un porcentaje. El sistema ya garantiza que ninguna cifra aparezca sin
  su base (ver [`decisiones.md`](decisiones.md), 2026-11-10).
- **El ranking de dependencias no se ordena por porcentaje.** Con pocas
  auditorías por dependencia, el porcentaje premia o castiga por cuántos
  trámites se auditaron. Falta decidir el orden: por trámites que fallan, por
  bloqueantes, o de otra forma, y cómo marcar las dependencias con pocos
  trámites auditados.

## Contenido

- **Explicaciones de los criterios WCAG en español.** Por ahora el componente
  criterio WCAG enlaza a las del W3C, en inglés, porque no hay traducción
  oficial de WCAG 2.2 (ver [`decisiones.md`](decisiones.md), 2026-11-10).
- **Una tabla única de números y nombres de criterios en español**, para que
  no se traduzcan distinto en cada página. Hace falta antes del hallazgo
  (3.4).

## Verificación

- **Pruebas con tecnologías de apoyo** ([#4](https://github.com/omad-mx/sistema-de-diseno/issues/4)):
  NVDA, TalkBack, VoiceOver, zoom al 400% y espaciado de texto forzado.
  Es el paso 5.2, pero cada componente se puede probar en cuanto exista. De
  estas pruebas depende poder declarar conformidad.

## Decisiones abiertas

- **¿Los hallazgos se publican o se dan bajo pedido?** Todavía no se decide.
  El componente ya está hecho y sirve en los dos casos. Ver
  [`decisiones.md`](decisiones.md), «Abiertas».

## Esperan al consejo

- Ratificar que este repositorio sea público (decidido el 2026-09-15, ver
  [`decisiones.md`](decisiones.md)).
- Su opinión sobre lo construido, cuando haya algo que enseñar. Por ahora la
  dirección de diseño decide y el consejo opina después (ver
  [`decisiones.md`](decisiones.md), 2026-11-10). Lo primero que se le lleva:
  la franja hecha y si se registra como marca
  ([#3](https://github.com/omad-mx/sistema-de-diseno/issues/3)), con el dato
  de que sus pictogramas vienen de un set público.
