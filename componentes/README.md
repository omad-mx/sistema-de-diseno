# Componentes

Aquí vive el catálogo. [`index.html`](index.html) muestra todos los
componentes en una página; cada uno tiene su carpeta con su CSS, su ejemplo
y su ficha. La receta completa está en
[`docs/como-se-hace-un-componente.md`](../docs/como-se-hace-un-componente.md).

Los primeros son los elementos de la fase 2 del
[plan](../docs/plan-de-construccion.md); se extraen de la
[maqueta de la dirección visual](../docs/maqueta-direccion-visual.html).

| Componente | Qué es | Estado |
|---|---|---|
| [`tipografia`](tipografia/README.md) | Encabezados, párrafo, listas, cejilla, entrada y prosa. | `borrador` |
| [`boton`](boton/README.md) | Botón primario, secundario y terciario, sobre un botón o sobre un enlace. | `borrador` |
| [`distintivo-gravedad`](distintivo-gravedad/README.md) | Los cuatro niveles de un hallazgo, con marca, nombre y color. | `borrador` |
| [`marca-resultado`](marca-resultado/README.md) | Si un perfil completó el trámite o no. | `borrador` |
| [`criterio-wcag`](criterio-wcag/README.md) | La referencia a un criterio, enlazada a su explicación. | `borrador` |
| [`aviso`](aviso/README.md) | Un aviso sobre toda la página, como «Datos de ejemplo». | `borrador` |
| [`tabla`](tabla/README.md) | Resultados en filas y columnas, con desplazamiento propio. | `borrador` |
| [`cabecera`](cabecera/README.md) | Saltar al contenido, la marca de OMAD y la navegación. | `borrador` |
| [`pie`](pie/README.md) | Enlaces secundarios y créditos. | `borrador` |
| [`resultado-perfiles`](resultado-perfiles/README.md) | El resultado de un trámite en una celda de tabla, escrito: total y quién no completó. | `borrador` |
| [`hallazgo`](hallazgo/README.md) | Un problema de una auditoría: gravedad, criterios, perfiles y la captura que lo prueba. | `borrador` |
| [`franja`](franja/README.md) | El componente firma: seis perfiles, su resultado y el titular «X de 6». Propuesta. | `borrador` |

El componente firma del sistema es **la franja de seis perfiles** (fase 3);
su especificación, incluido cómo se linealiza en un lector de pantalla, está
en [el documento del sistema](../docs/omad-sistema-de-diseno.md#5-los-seis-perfiles).

Todo CSS de esta carpeta usa únicamente tokens semánticos (capa 2) de
[`tokens/omad-tokens.css`](../tokens/omad-tokens.css). Nunca primitivas,
nunca un color escrito a mano. Lo revisa `herramientas/revisar-componentes.py`
en cada PR.
