# Documentos del sistema

Cada documento lleva arriba título, versión si aplica, fecha y estado. Nombres
de archivo en minúsculas y con guiones. Lo que sea operación de OMAD y no del
sistema (costos, acuerdos, presupuestos) no va aquí: va en el repositorio
privado `omad-mx/interno`.

## Estados

| Estado | Qué significa |
|---|---|
| `borrador` | Se está escribiendo. Puede cambiar entero. |
| `en discusión` | Está completo y espera dictamen. Los puntos abiertos están en el registro de decisiones o en un issue. |
| `aprobado` | El consejo o la dirección de diseño lo ratificó. Cambiarlo requiere reabrir la decisión. |
| `superado` | Lo reemplazó otro documento. Se conserva por el historial. |

## Índice

| Documento | Qué es | Fecha | Estado |
|---|---|---|---|
| [`omad-sistema-de-diseno.md`](omad-sistema-de-diseno.md) | El documento del sistema, versión 0.1: problema, dirección visual, paleta, el hallazgo de visión cromática, los seis perfiles, tipografía, espacio y foco. | 2026-09-09 | `en discusión` |
| [`decisiones.md`](decisiones.md) | Registro cronológico de lo decidido y lo pendiente. | 2026-09-15 | vivo |
| [`maqueta-direccion-visual.html`](maqueta-direccion-visual.html) | Maqueta a tamaño real con la que se ratificó la dirección visual ([#1](https://github.com/omad-mx/sistema-de-diseno/issues/1)): A (0.1) y B (cálida) sobre el mismo contenido, con controles; abre en la combinación ratificada. Ábrela en el navegador desde el clon. | 2026-09-20 | `aprobado` |
| [`plan-de-construccion.md`](plan-de-construccion.md) | El plan paso a paso, del documento 0.1 a un prototipo funcional y una fundación verificada. | 2026-09-25 | `en discusión` |
| [`pendientes.md`](pendientes.md) | Lo que falta, en orden y con lo que lo bloquea. | 2026-09-25 | vivo |
| [`como-se-hace-un-componente.md`](como-se-hace-un-componente.md) | La receta de todo componente: carpeta, HTML, CSS, ejemplo, ficha y lista de revisión. | 2026-11-03 | `aprobado` |
| [`maqueta-marca-gravedad.html`](maqueta-marca-gravedad.html) | Maqueta para elegir la marca del distintivo de gravedad: cuatro propuestas al tamaño real, en color, grises, deuteranopia simulada y sin color. Se eligió la C, una forma por nivel. Ábrela en el navegador desde el clon. | 2026-11-10 | `aprobado` |
| [`maqueta-pictogramas.html`](maqueta-pictogramas.html) | Maqueta para elegir los pictogramas de los seis perfiles: candidatos del set Lucide (licencia ISC) a 16, 24 y 48 px, y una franja de prueba que cambia con la elección. Ábrela en el navegador desde el clon. | 2026-11-10 | `en discusión` |

## Pendientes de escribir

- Guía de pruebas manuales con tecnologías de apoyo ([#4](https://github.com/omad-mx/sistema-de-diseno/issues/4)).
- Especificación de la franja de seis perfiles como componente. La dirección visual ya está ratificada; falta la iconografía de los seis perfiles.
