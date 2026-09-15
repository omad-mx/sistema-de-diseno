# Sistema de diseño OMAD
### Documento de tokens · versión 0.1 · documento de trabajo

Acompaña a `omad-tokens.css` (implementación) y `verificar-contraste.py` (verificación).

Esto es una propuesta para discusión, no una decisión tomada. Los valores de color están calculados y verificados; la dirección visual está abierta a que el consejo la tumbe.

---

## 1. Qué problema resuelve este sistema

OMAD publica una cifra que se va a citar en notas periodísticas, en oficios y probablemente en un derecho de réplica. El sistema visual tiene tres trabajos, en este orden:

1. **Que la cifra se pueda citar.** Alguien tiene que poder ver una ficha de auditoría y salir con un dato exacto y una fuente, no con una impresión.
2. **Que el sitio sobreviva su propio criterio.** Van a reprobar sitios por cosas que un auditor externo podría encontrar en el suyo. El piso de conformidad no es una aspiración, es una condición de credibilidad.
3. **Que no se vea como gobierno ni como despacho.** Ni la institucionalidad prestada ni el aire de consultoría; ambas cosas les cuestan independencia.

Todo lo demás es secundario.

---

## 2. Dirección visual, y lo que se descartó

**Lo que se descartó primero.** La combinación de fondo crema cálido, serif de titular y acento terracota es la salida por defecto de cualquier herramienta generativa hoy; se ve en la mitad de los sitios producidos con IA. También se descartó el pastiche de periódico —filetes capilares, columnas densas, cero radio en todo— por la misma razón. Y se descartó cualquier cercanía con la identidad gráfica federal 2024-2030, incluida la que arrastra Sisdai en sus versiones 4.1.0 en adelante.

**Lo que queda.** Tinta fría sobre superficies frías, casi de reporte de laboratorio. Una sola familia tipográfica. Un solo color de marca. Cero decoración. La única audacia del sistema está en un componente —la franja de seis perfiles— y todo lo demás se mantiene callado para que esa franja sea lo que la gente recuerde.

**De dónde sale el color de marca.** El objeto visual más característico del mundo de la accesibilidad es el anillo de foco del teclado. El petróleo del sistema se eligió como color de anillo de foco primero y como color de marca después. La consecuencia práctica es que el color de marca no puede ser de bajo contraste: está atado por definición al requisito de 3:1 no textual.

---

## 3. Paleta

### 3.1 Tinta — neutro frío

Base de texto y de superficies oscuras. Frío deliberado: el gris cálido lee editorial y el editorial ya está tomado.

| Token | Hex | Uso |
|---|---|---|
| `tinta-950` | `#080F13` | fondo de sección a sangre |
| `tinta-900` | `#0E1A1F` | texto principal (claro) · fondo (oscuro) |
| `tinta-800` | `#16262D` | superficie (oscuro) |
| `tinta-700` | `#22363F` | texto secundario (claro) · superficie alta (oscuro) |
| `tinta-600` | `#334A55` | texto terciario (claro) · borde (oscuro) |
| `tinta-500` | `#4C646F` | texto deshabilitado |
| `tinta-400` | `#6B838E` | borde fuerte |
| `tinta-300` | `#94A8B1` | texto terciario (oscuro) |
| `tinta-200` | `#BDCBD1` | borde (claro) · texto secundario (oscuro) |
| `tinta-100` | `#DCE4E7` | separadores |
| `tinta-50` | `#EDF1F2` | superficie (claro) |
| `tinta-0` | `#FBFCFC` | fondo (claro) |

### 3.2 Petróleo — marca, foco, acción, completitud

| Token | Hex | Uso |
|---|---|---|
| `petroleo-800` | `#053A45` | enlace visitado (claro) |
| `petroleo-700` | `#074C5B` | hover de acción |
| `petroleo-600` | `#0B5563` | **marca** · enlace · foco · botón · "completó" |
| `petroleo-300` | `#5FAEBD` | enlace y acción en oscuro |
| `petroleo-200` | `#9BCED8` | anillo de foco en oscuro |
| `petroleo-100` | `#CDE7EC` | fondo de resalte |

### 3.3 Escala de gravedad

Cuatro niveles. Bloqueante y severa son las únicas que reciben color caliente; moderada y menor son neutros de familias distintas (cálido y frío). La decisión es semántica antes que estética: visualmente el sistema afirma que solo los dos primeros niveles son la nota.

| Nivel | Hex | Contraste sobre `tinta-0` |
|---|---|---|
| Bloqueante | `#7C1D06` | 10.04:1 |
| Severa | `#9F5500` | 5.41:1 |
| Moderada | `#63594A` | 6.68:1 |
| Menor | `#41586B` | 7.21:1 |

---

## 4. El hallazgo que cambió la paleta

La primera versión de esta escala usaba un semáforo convencional: rojo, naranja, ámbar, gris, más verde para "completado". Al simularla bajo deficiencias de visión cromática, se cayó.

Distancia CIE76 entre etiquetas (por debajo de ~20 se confunden a simple vista):

| Par | Visión típica | Protanopia | Deuteranopia |
|---|---|---|---|
| bloqueante / severa | 23.7 | **17.0** | **6.7** |
| bloqueante / moderada | 47.7 | **19.6** | **5.7** |
| severa / moderada | 26.4 | **5.4** | **5.2** |

Un semáforo de cuatro pasos es ilegible para una parte considerable de la población que OMAD dice representar. La escala actual, separada por luminosidad y por familia además de por tono, mantiene un peor par de 21.0 en las tres simulaciones.

**Y aun así**: no hubo forma de encontrar un verde de "completado" que no colapsara contra el neutro cálido de "moderada" bajo deuteranopia —se probaron seis, el mejor par quedó en 13.9. Por eso el eje de completitud abandonó el verde. "Completó" y "no completó" se distinguen por marca, por texto y por el azul de marca contra el rojo bloqueante, con una separación de 40.1 en el peor caso.

**Regla que se deriva de esto, y que aplica a todo el sistema:** el color nunca es el único portador de significado. Cada nivel de gravedad y cada resultado de perfil lleva siempre marca gráfica, etiqueta de texto y posición fija. Este es el criterio 1.4.1 de WCAG, y es literalmente el primero por el que OMAD va a reprobar a alguien.

Vale la pena publicar esta tabla en la ficha metodológica. Enseña el trabajo y establece el estándar contra el que se van a medir los sitios auditados.

---

## 5. Los seis perfiles

Cada perfil tiene identidad fija: nombre, marca gráfica y posición constante en la franja. Aparecen siempre en el mismo orden, en todas las fichas, en el informe impreso y en las gráficas.

| # | Perfil | Etiqueta corta |
|---|---|---|
| 1 | Lector de pantalla | Lector |
| 2 | Solo teclado | Teclado |
| 3 | Baja visión | Baja visión |
| 4 | Motriz | Motriz |
| 5 | Persona sorda | Sorda |
| 6 | Cognitivo | Cognitivo |

**Los perfiles no tienen color propio.** Se distinguen por marca y por posición. Asignarles seis colores categóricos habría reintroducido exactamente el problema de la sección 4, y además habría competido con la escala de gravedad en la misma pantalla. El único color en la franja es el del eje completó / no completó.

### La franja — componente firma

Es el único lugar donde el sistema levanta la voz. Seis celdas de ancho fijo, siempre las mismas, siempre en el mismo orden, que acompañan a toda entidad auditada como una marca de conformidad.

```
┌────────┬────────┬────────┬────────┬────────┬────────┐
│ Lector │Teclado │  Baja  │ Motriz │ Sorda  │ Cogni- │
│        │        │ visión │        │        │  tivo  │
├────────┼────────┼────────┼────────┼────────┼────────┤
│   ×    │   ×    │   ●    │   ×    │   ●    │   ×    │
└────────┴────────┴────────┴────────┴────────┴────────┘
   2 de 6 perfiles completaron el trámite sin ayuda
```

Linealizada por un lector de pantalla, la franja debe leerse como una lista de seis resultados con su etiqueta, no como una tabla de símbolos sueltos. Se marca con `role="list"`, cada celda con su texto accesible completo, y el titular de "X de 6" existe como texto real, no como imagen ni como suma calculada en el cliente.

---

## 6. Tipografía

**Una sola familia: Atkinson Hyperlegible.** Del Braille Institute, diseñada específicamente para baja visión, con formas de letra que separan caracteres habitualmente confundibles.

Es a la vez la decisión funcional y la declaración de principios: el observatorio compone su propio texto en la tipografía hecha para las personas por las que audita. Y resuelve el problema de identidad sin tener que inventar una pareja tipográfica que se vería como cualquier otra.

La jerarquía la cargan el peso, el tamaño y el espacio. No hay segunda familia para titulares. Hay una mono, pero solo aparece dentro de fragmentos de código en los anexos de evidencia, donde el ancho fijo hace un trabajo real.

**Escala 1.25 sobre base de 18px.** La base es mayor que los 16px habituales por decisión, no por descuido: es el cuerpo mínimo cómodo, no el mínimo legal.

| Token | rem | px | Uso |
|---|---|---|---|
| `4xl` | 4.291 | 69 | cifra del ITC |
| `3xl` | 2.747 | 44 | h1 |
| `2xl` | 2.197 | 35 | h2 |
| `xl` | 1.758 | 28 | h3 |
| `lg` | 1.406 | 22.5 | entrada, h4 |
| `base` | 1.125 | 18 | cuerpo |
| `sm` | 1 | 16 | tabla densa |
| `xs` | 0.875 | 14 | notas, créditos |

Medida máxima de 66 caracteres en prosa. Interlínea de 1.65 en cuerpo, 1.15 solo en titulares grandes. Cifras siempre en `tabular-nums` para que las columnas alineen.

---

## 7. Espacio, forma, foco

Escala de espacio en base 4. Radio de 2px en controles y 0 en tablas de datos: el registro es el de un formulario oficial, no el de una tarjeta de producto.

**Objetivo táctil mínimo: 44×44px.** WCAG 2.2 AA exige 24px en el criterio 2.5.8. El sistema exige 44 porque el criterio mínimo es exactamente el tipo de conformidad de trámite que OMAD va a criticar.

**Anillo de foco de doble capa**, 3px de color de marca más 2px de separación en el color de fondo. Funciona sobre cualquier superficie sin redefinirse por componente, y cumple 2.4.11 y 2.4.13. `outline: none` sin un `:focus-visible` equivalente es motivo de rechazo de PR, sin excepción.

Los enlaces conservan subrayado siempre. El color no distingue un enlace del texto que lo rodea.

Movimiento solo como respuesta a una acción de la persona, y anulado bajo `prefers-reduced-motion`.

---

## 8. Cómo se usa esto en Claude Design

Este documento es el brief. En el flujo de configuración del sistema de diseño en Claude Design, sube los tres archivos —el `.md`, el `.css` y el script— más las capturas de los trámites ya auditados. Las capturas importan tanto como los tokens: sin contenido real, lo que salga va a ser una maqueta bonita de datos inventados.

Luego valida con un proyecto de prueba antes de publicar. Los dos que revelan si el sistema aguanta son la ficha de auditoría de un trámite y la tabla del ranking; si esos dos salen bien, el resto también.

Una advertencia sobre el orden: lo que se publica como sistema de diseño de la organización se hereda en todo proyecto nuevo, así que conviene que el consejo apruebe la dirección antes de activar el interruptor, no después.

---

## 9. Decisiones abiertas

El estado de cada una se lleva en [`decisiones.md`](decisiones.md) y en los issues con etiqueta `decisión`; esta lista es la foto de la versión 0.1.

- **La dirección visual completa.** Frío y contenido es una propuesta, no un consenso. La alternativa razonable es un registro más cálido y más divulgativo, que ganaría accesibilidad cognitiva y perdería tono de autoridad citable.
- **El nombre de los tokens en español.** Consistente con el proyecto y legible para colaboradores mexicanos; incómodo si en algún momento se abre a contribución internacional.
- **Si la franja de seis perfiles se registra como marca.** Si va a funcionar como sello de conformidad citable, conviene decidirlo antes de publicarla, no después de que alguien la copie.
- **Verificación pendiente.** Nada de esto está probado todavía con NVDA, TalkBack ni VoiceOver, ni con zoom al 400%, ni con espaciado de texto forzado. Los números de contraste están calculados; el comportamiento no está probado. Ese es el trabajo que sigue y no lo puede hacer una herramienta.
