# Sistema de diseño OMAD

Tokens, documentación y herramientas de verificación del sistema de diseño del
Observatorio Mexicano de Accesibilidad Digital.

> **Versión 0.1 · documento de trabajo · sin aprobación del consejo.**
> Los valores de color están calculados y verificados. La dirección visual es
> una propuesta abierta a discusión, no una decisión tomada. Ver
> [Decisiones abiertas](docs/omad-sistema-de-diseno.md#9-decisiones-abiertas).

---

## Qué es esto

OMAD publica una cifra que se va a citar en notas periodísticas, en oficios y
probablemente en un derecho de réplica. Este repositorio contiene la capa
visual que sostiene esa cifra, y existe para que tres cosas sean verificables
por cualquiera, no afirmadas de palabra:

1. **Que la cifra se pueda citar.** Una ficha de auditoría tiene que dejar
   salir a quien la lee con un dato exacto y una fuente.
2. **Que el sitio sobreviva su propio criterio.** OMAD va a reprobar sitios por
   cosas que un auditor externo podría encontrar en el suyo. El piso de
   conformidad no es una aspiración, es una condición de credibilidad.
3. **Que no se vea como gobierno ni como despacho.** Las dos cercanías cuestan
   independencia.

El razonamiento completo, incluido el hallazgo de visión cromática que tumbó la
primera paleta, está en
[`docs/omad-sistema-de-diseno.md`](docs/omad-sistema-de-diseno.md).

## Estructura

| Carpeta | Qué contiene |
|---|---|
| [`tokens/`](tokens/) | `omad-tokens.css` — la implementación. Dos capas: primitivas y semánticos. |
| [`docs/`](docs/) | Los documentos del sistema y el registro de decisiones. El [índice](docs/README.md) dice qué hay y en qué estado está. |
| [`herramientas/`](herramientas/) | `verificar-contraste.py` — calcula el contraste WCAG de cada par y verifica el contrato. |
| [`componentes/`](componentes/) | Todavía vacío a propósito. Ver la nota adentro. |

## El contrato de contraste

El sistema promete que ciertos pares de color cumplen un mínimo concreto:
texto principal, texto secundario, enlaces, anillo de foco, las cuatro etiquetas
de gravedad, en tema claro y en tema oscuro. Esa promesa está escrita como una
lista explícita en la constante `CONTRATO` de
[`herramientas/verificar-contraste.py`](herramientas/verificar-contraste.py),
que hoy verifica **31 pares**.

```sh
# verificar el contrato (sale con código 1 si algún par incumple)
python3 herramientas/verificar-contraste.py

# volcar la matriz completa de todos los pares de la paleta
python3 herramientas/verificar-contraste.py --csv > contrastes.csv
```

Solo necesita Python 3, sin dependencias.

**El script es la fuente de verdad.** Si cambias un valor de la capa 1 en
`tokens/omad-tokens.css`, actualiza también la paleta del script y vuelve a
correrlo antes de abrir el PR.

### Verificación automática

[`.github/workflows/verificar-contraste.yml`](.github/workflows/verificar-contraste.yml)
corre el script en cada pull request. Si un solo par incumple, **el build falla
y el PR no se integra**. El reporte queda en el resumen del job y la matriz
completa se adjunta como artefacto.

Para cambiar el contrato hay que cambiarlo a propósito, en el PR, a la vista.

## Reglas no negociables

Están en el CSS y no son sugerencias de estilo. Un componente que las
sobreescriba tiene que justificarlo en la revisión:

- **El color nunca es el único portador de significado** (WCAG 1.4.1). Cada
  nivel de gravedad y cada resultado de perfil lleva siempre marca gráfica,
  etiqueta de texto y posición fija.
- **`outline: none` sin un `:focus-visible` equivalente es motivo de rechazo de
  PR**, sin excepción. El anillo de foco es de doble capa y funciona sobre
  cualquier superficie sin redefinirse por componente.
- **Los enlaces conservan subrayado siempre.**
- **Objetivo táctil mínimo de 44×44px.** WCAG 2.2 AA exige 24 en el criterio
  2.5.8; el sistema exige 44, porque el mínimo legal es exactamente el tipo de
  conformidad de trámite que OMAD va a criticar.
- **Nada de alturas fijas en contenedores de texto.** El texto tiene que
  sobrevivir el reflujo a 320px y el espaciado forzado (1.4.10 y 1.4.12).
- En el CSS de componentes solo aparecen tokens semánticos (capa 2). Las
  primitivas (capa 1) no se usan directamente.

## Lo que todavía no está probado

El contraste está calculado; el comportamiento no. Nada de esto se ha probado
con NVDA, TalkBack ni VoiceOver, ni con zoom al 400%, ni con espaciado de texto
forzado. Ese trabajo sigue pendiente y no lo puede hacer una herramienta.

## Por qué es público

Un observatorio que va a reprobar sitios ajenos gana credibilidad si su propio
sistema es verificable por cualquiera. Y en la práctica, es lo que permite
proteger `main` sin pagar: nada entra sin pull request, sin que la
verificación de contraste pase y sin commit firmado.

Aquí va solo lo que es del sistema de diseño. Lo que es operación de OMAD
(costos, acuerdos, presupuestos) vive en un repositorio privado aparte.

## Cómo colaborar

1. **Todo entra por pull request.** No se puede empujar directo a `main`, ni
   siendo admin.
2. **La CI tiene que estar verde.** Si cambias un color, cámbialo en
   `tokens/omad-tokens.css` **y** en la `PALETA` del script, y corre
   `python3 herramientas/verificar-contraste.py` antes de abrir el PR.
3. **Los commits van firmados.** GitHub rechaza los que no lo estén.
4. **Las decisiones se registran.** Lo que está por decidirse es un issue con
   la etiqueta `decisión`; lo decidido se pasa a
   [`docs/decisiones.md`](docs/decisiones.md) con fecha, quién y por qué.
5. **Los documentos nuevos van en `docs/`** con cabecera de fecha y estado, y
   se agregan al [índice](docs/README.md).

## Licencia

[Apache License 2.0](LICENSE).
