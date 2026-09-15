# Sistema de diseño OMAD

Sistema de diseño del Observatorio Mexicano de Accesibilidad Digital. Versión
0.1, documento de trabajo, **sin aprobación del consejo**: la dirección visual
es propuesta, no consenso. Todo en español, incluidos nombres de tokens,
commits, issues y PRs.

Este proyecto es **aparte de Katachi**. No aplican aquí los acuerdos de otros
repositorios.

## Qué hay

- `tokens/omad-tokens.css` — dos capas: primitivas (capa 1) y semánticos (capa 2).
- `herramientas/verificar-contraste.py` — verifica 31 pares de contraste WCAG 2.2 AA. Sin dependencias. Sale con 1 si alguno incumple; la CI lo corre en cada PR.
- `docs/` — el documento del sistema, el índice (`docs/README.md`) y el registro de decisiones (`docs/decisiones.md`).
- `componentes/` — vacío a propósito hasta que se ratifique la dirección visual (#1).

## Reglas que no se discuten en un PR

- **El script es la fuente de verdad de los colores**, no el CSS. Un cambio de color se hace en los dos y se corre el script antes de abrir el PR. La CI solo mira el script (#5).
- **La escala de gravedad no vuelve al semáforo y no hay verde de «completado».** Sale de distancias CIE76 bajo deuteranopia (sección 4 del documento). No se re-litiga sin volver a correr las distancias.
- **Los seis perfiles no tienen color propio.** Marca gráfica y posición fija.
- En CSS de componentes **solo tokens semánticos**. Nunca primitivas, nunca un hex suelto.
- `outline: none` sin `:focus-visible` equivalente es motivo de rechazo. Enlaces siempre subrayados. Objetivo táctil 44×44. Sin alturas fijas en contenedores de texto.
- Una sola familia: Atkinson Hyperlegible. Base 18px.

## Flujo

- `main` está protegido: PR obligatorio, CI verde, commits firmados, sin force-push. Aplica a admins.
- Ramas: `docs/…`, `tokens/…`, `componentes/…`, `herramientas/…`.
- Decisiones pendientes = issue con etiqueta `decisión`. Decisiones tomadas = entrada en `docs/decisiones.md` con fecha, quién y por qué.
- Lo que sea operación de OMAD (costos, acuerdos) **no va aquí**: va en `omad-mx/interno`, privado.

## Al escribir documentos

- Cabecera con título, fecha y estado (`borrador` / `en discusión` / `aprobado` / `superado`); se agregan al índice.
- Nada de cifras medidas a mano. Lo que se afirma numéricamente sale del script o de una medición reproducible.
- Nunca inventar datos, trámites ni resultados de auditoría para ilustrar.
