# Pendientes

Fecha: 2026-11-10 · Estado: vivo

Lo que falta ahora, en el orden en que conviene hacerlo. El camino completo
está en [`plan-de-construccion.md`](plan-de-construccion.md); esta lista
muestra el tramo en curso. El detalle vive en su issue o PR, no aquí.

Al terminar algo, se borra de esta lista. Si fue una decisión, pasa a
[`decisiones.md`](decisiones.md), y el historial queda en git.

---

## En curso

Nada. La fase 2 (elementos) está completa: tipografía, botón, distintivo de
gravedad, marca de resultado, criterio WCAG y aviso están en el
[catálogo](../componentes/index.html), los seis como `borrador` hasta que se
prueben con tecnologías de apoyo.

## Siguiente: fase 3 del plan, componentes

1. **Pictogramas de los seis perfiles** (3.1). Los dibujamos la dirección de
   diseño y Claude, con tiempo acotado (D3).
2. **Franja** (3.2). Se construye ya, como propuesta (D2); el registro como
   marca ([#3](https://github.com/omad-mx/sistema-de-diseno/issues/3)) se
   lleva al consejo con la franja hecha.
3. **Resultado por perfiles** (3.3), antes «franja mini».
4. **Hallazgo** (3.4). La evidencia es una captura de pantalla.
5. **Cifra citable** (3.5).
6. **Tabla de datos** (3.6). Ojo: la caja con desplazamiento necesita
   `position: relative`, o los textos ocultos para lector de pantalla se
   salen y estiran la página (se vio en la maqueta de la marca de gravedad).
7. **Cabecera, navegación y pie** (3.7).

## Herramientas

- **Escala de radio al revés:** `--omad-radio-1` es 8 px y `--omad-radio-2`
  sigue en 4. Nadie usa el 2 todavía; se define cuando un componente lo pida.

## Diseño

- **La marca de OMAD en la cabecera es provisional.** La sigla con su barra
  es un lugar para el logo, que todavía no existe. Si el enlace a la portada
  lleva subrayado o es una excepción a la regla se decide con el logo.

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

## Esperan al consejo

- Ratificar que este repositorio sea público (decidido el 2026-09-15, ver
  [`decisiones.md`](decisiones.md)).
- Su opinión sobre lo construido, cuando haya algo que enseñar. Por ahora la
  dirección de diseño decide y el consejo opina después (ver
  [`decisiones.md`](decisiones.md), 2026-11-10). Lo primero que se le lleva:
  la franja hecha y si se registra como marca
  ([#3](https://github.com/omad-mx/sistema-de-diseno/issues/3)), con el dato
  de que sus pictogramas vienen de un set público.
