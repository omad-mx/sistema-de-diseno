# Pendientes

Fecha: 2026-09-25 · Estado: vivo

Lo que falta, en el orden en que conviene hacerlo. Cada renglón dice qué
lo bloquea. El detalle vive en su issue o PR, no aquí: esta lista es el
mapa, no el expediente.

Al terminar algo, se borra de esta lista. Si fue una decisión, pasa a
[`decisiones.md`](decisiones.md), y el historial queda en git.

---

## En curso

- **Cerrar la dirección visual.** [PR #7](https://github.com/omad-mx/sistema-de-diseno/pull/7), en borrador.
  Falta cambiar `--omad-radio-1` de 2 a 8 px en `tokens/omad-tokens.css` y
  actualizar el párrafo de la sección 7 del documento. Después, pasar el PR a
  listo, hacer merge y cerrar [#1](https://github.com/omad-mx/sistema-de-diseno/issues/1).

## Siguiente

1. **Pictogramas de los seis perfiles.** Los de la maqueta son bosquejos.
   *Bloquean la franja.*
2. **Nombres de tokens: español o inglés** ([#2](https://github.com/omad-mx/sistema-de-diseno/issues/2)).
   Conviene decidirlo antes del primer componente: después, cambiar un nombre
   significa cambiarlo en todos los componentes que lo usan.
3. **Definir qué es un componente en este repositorio:** qué archivos lleva
   cada carpeta de `componentes/` y qué documenta. Hay que tenerlo antes del
   primero.
4. **La franja de seis perfiles**, el primer componente. Depende de 1, 2 y 3.
   Su especificación está en la [sección 5](omad-sistema-de-diseno.md#5-los-seis-perfiles).

## Herramientas

- **La paleta está duplicada entre el CSS y el script** ([#5](https://github.com/omad-mx/sistema-de-diseno/issues/5)).
  Si un color cambia solo en el CSS, la revisión automática pasa en verde.
  No bloquea nada; se puede hacer en cualquier hueco.

## Verificación

- **Pruebas con tecnologías de apoyo** ([#4](https://github.com/omad-mx/sistema-de-diseno/issues/4)):
  NVDA, TalkBack, VoiceOver, zoom al 400% y espaciado de texto forzado.
  Empiezan cuando exista el primer componente, porque antes no hay nada que
  probar. De estas pruebas depende poder declarar conformidad.

## Esperan al consejo

- Ratificar que este repositorio sea público (decidido el 2026-09-15, ver
  [`decisiones.md`](decisiones.md)).
- Registrar la franja como marca ([#3](https://github.com/omad-mx/sistema-de-diseno/issues/3)).
  El documento pide decidirlo antes de publicarla, y el repositorio es público.
