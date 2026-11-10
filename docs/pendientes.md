# Pendientes

Fecha: 2026-11-05 · Estado: vivo

Lo que falta ahora, en el orden en que conviene hacerlo. El camino completo
está en [`plan-de-construccion.md`](plan-de-construccion.md); esta lista
muestra el tramo en curso. El detalle vive en su issue o PR, no aquí.

Al terminar algo, se borra de esta lista. Si fue una decisión, pasa a
[`decisiones.md`](decisiones.md), y el historial queda en git.

---

## En curso

Nada. La fase 1 (cimientos) está completa.

## Siguiente: fase 2 del plan, elementos

Se extraen de la [maqueta](maqueta-direccion-visual.html) siguiendo
[cómo se hace un componente](como-se-hace-un-componente.md). El 2.1 va
primero; del 2.2 al 2.6 pueden ir juntos.

1. **Tipografía y prosa** (2.1).
2. **Enlace y botón** (2.2).
3. **Distintivo de gravedad** (2.3).
4. **Marca de resultado** (2.4).
5. **Criterio WCAG** (2.5).
6. **Aviso** (2.6). Su primer uso es «Datos de ejemplo» en el prototipo.

## Herramientas

- **Escala de radio al revés:** `--omad-radio-1` es 8 px y `--omad-radio-2`
  sigue en 4. Nadie usa el 2 todavía; se define cuando un componente lo pida.

## Verificación

- **Pruebas con tecnologías de apoyo** ([#4](https://github.com/omad-mx/sistema-de-diseno/issues/4)):
  NVDA, TalkBack, VoiceOver, zoom al 400% y espaciado de texto forzado.
  Es el paso 5.2, pero cada componente se puede probar en cuanto exista. De
  estas pruebas depende poder declarar conformidad.

## Esperan al consejo

- Ratificar que este repositorio sea público (decidido el 2026-09-15, ver
  [`decisiones.md`](decisiones.md)).
- Registrar la franja como marca ([#3](https://github.com/omad-mx/sistema-de-diseno/issues/3)).
  El documento pide decidirlo antes de publicarla, y el repositorio es público.
  Es la decisión D2 del plan: conviene que el consejo la tome antes de la
  fase 3.
