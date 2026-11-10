# Sistema de diseño OMAD

Sistema de diseño del Observatorio Mexicano de Accesibilidad Digital. Versión
0.1, documento de trabajo, **sin aprobación del consejo**: la dirección visual
es propuesta, no consenso. Todo en español, incluidos nombres de tokens,
commits, issues y PRs.

Este proyecto es **aparte de Katachi**. No aplican aquí los acuerdos de otros
repositorios.

## Qué hay

- `tokens/omad-tokens.css` — solo variables, dos capas: primitivas (capa 1) y semánticos (capa 2).
- `estilos/omad.css` — la hoja única que carga una página. Importa los tokens, `fuentes.css` (las dos familias desde `fuentes/`, sin Google Fonts) y `base.css` (foco, enlaces, cuerpo, `.visualmente-oculto`).
- `herramientas/verificar-contraste.py` — lee los tokens y verifica el contrato de contraste WCAG 2.2 AA: pares de tokens semánticos, medidos en tema claro y en oscuro. Falla también si un token de color queda sin medir o si la capa 2 trae un color a mano. Sin dependencias. Sale con 1 si alguno incumple; la CI lo corre en cada PR.
- `herramientas/revisar-componentes.py` — lee el CSS de `componentes/` y falla si hay una primitiva, un color a mano, `outline: none` sin `:focus-visible` o `!important`. La CI lo corre en cada PR.
- `herramientas/paleta-direccion-b.py` — deriva la paleta cálida de la maqueta de #1 (mismo L y C, tono girado) y la verifica. `--css` imprime el bloque que va en `docs/maqueta-direccion-visual.html`; ese bloque no se edita a mano.
- `docs/` — el documento del sistema, el índice (`docs/README.md`) y el registro de decisiones (`docs/decisiones.md`).
- `componentes/` — el catálogo (`index.html`) y una carpeta por componente, según `docs/como-se-hace-un-componente.md`.
- `prototipo/` — el sitio armado solo con componentes del catálogo; sin estilos propios.

## Reglas que no se discuten en un PR

- **Los colores viven en un solo lugar: la capa 1 de `tokens/omad-tokens.css`.** El script los lee de ahí y ningún color entra sin pasar el contrato. La capa 1 solo admite hexadecimales, porque es lo que el script sabe medir; la capa 2 solo admite `var()` a una primitiva.
- **La escala de gravedad no vuelve al semáforo y no hay verde de «completado».** Sale de distancias CIE76 bajo deuteranopia (sección 4 del documento). No se re-litiga sin volver a correr las distancias.
- **Los seis perfiles no tienen color propio.** Marca gráfica y posición fija.
- En CSS de componentes **solo tokens semánticos**. Nunca primitivas, nunca un hex suelto.
- `outline: none` sin `:focus-visible` equivalente es motivo de rechazo. Enlaces siempre subrayados. Objetivo táctil 44×44. Sin alturas fijas en contenedores de texto.
- Una sola familia: Atkinson Hyperlegible. Base 18px.
- Nombres (tokens, clases, archivos, ramas) en español, **sin acentos y con ñ → n**: `petroleo`, `tipografia`, `tamano`. Nunca `tamanio`.

## Flujo

- `main` está protegido: PR obligatorio, CI verde, commits firmados, sin force-push. Aplica a admins.
- Ramas: `docs/…`, `tokens/…`, `estilos/…`, `componentes/…`, `prototipo/…`, `herramientas/…`.
- Decisiones pendientes = issue con etiqueta `decisión`. Decisiones tomadas = entrada en `docs/decisiones.md` con fecha, quién y por qué.
- Lo que sea operación de OMAD (costos, acuerdos) **no va aquí**: va en `omad-mx/interno`, privado.

## Al escribir documentos

- Cabecera con título, fecha y estado (`borrador` / `en discusión` / `aprobado` / `superado`); se agregan al índice.
- Nada de cifras medidas a mano. Lo que se afirma numéricamente sale del script o de una medición reproducible.
- Datos de ejemplo solo en el prototipo y con las condiciones de la sección 2 de `docs/plan-de-construccion.md`: todo ficticio, avisado en la página y concentrado en `prototipo/datos-de-ejemplo.md`. Nunca un trámite o una dependencia real con un resultado inventado.
