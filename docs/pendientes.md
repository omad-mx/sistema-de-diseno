# Pendientes

Fecha: 2026-10-31 · Estado: vivo

Lo que falta ahora, en el orden en que conviene hacerlo. El camino completo
está en [`plan-de-construccion.md`](plan-de-construccion.md); esta lista
muestra el tramo en curso. El detalle vive en su issue o PR, no aquí.

Al terminar algo, se borra de esta lista. Si fue una decisión, pasa a
[`decisiones.md`](decisiones.md), y el historial queda en git.

---

## En curso

- **Cerrar la fase 0.** La dirección visual entró con el
  [PR #7](https://github.com/omad-mx/sistema-de-diseno/pull/7); falta cerrar
  [#1](https://github.com/omad-mx/sistema-de-diseno/issues/1). Con el merge de
  este plan ([PR #8](https://github.com/omad-mx/sistema-de-diseno/pull/8)) se
  cierra [#2](https://github.com/omad-mx/sistema-de-diseno/issues/2).

## Siguiente: fase 1 del plan, cimientos

1. **Cómo se hace un componente** (paso 1.1).
2. **Fuentes propias** (paso 1.2).
3. **Separar tokens y reglas base** (paso 1.3). Falta la decisión D4. De paso,
   rehacer la escala de radio: `--omad-radio-1` subió a 8 px y
   `--omad-radio-2` se quedó en 4, así que la escala quedó al revés.
4. **Revisión automática de componentes en la CI** (paso 1.4).
5. **Esqueletos del catálogo y del prototipo** (paso 1.6).

## Herramientas

- **La paleta está duplicada entre el CSS y el script** ([#5](https://github.com/omad-mx/sistema-de-diseno/issues/5)).
  Si un color cambia solo en el CSS, la revisión automática pasa en verde.
  Es el paso 1.5 y puede ir en paralelo con el resto de la fase 1.

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
