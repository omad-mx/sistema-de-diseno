# Cifra citable

Estado: `borrador`

## Qué es

El número grande de OMAD, con lo que hace falta para citarlo: su base, qué
mide, de cuándo es y de dónde sale, y un bloque «Cómo citar» con el texto
listo. Su forma principal es «X de N»: «4 de 10 trámites auditados se pueden
completar sin ayuda». Es
el primer trabajo del sistema según la sección 1 del documento: que quien
vea la cifra salga con un dato exacto y una fuente, no con una impresión.

## Cuándo se usa

- En la portada, una vez: la cifra del observatorio.
- En la página de una dependencia o de un corte, para su propia cifra.

## Cuándo no

- **Para cualquier número.** Solo para una cifra que OMAD publica y quiere
  que se cite. Un dato dentro de un texto es texto.
- **Varias en la misma pantalla.** Es lo único grande de la página.

## Anatomía

```html
<figure class="cifra-citable" aria-labelledby="c-numero c-que">
  <p class="cifra-citable-numero" id="c-numero" data-cifra>00 <span class="cifra-citable-base">de 00</span></p>
  <p class="cifra-citable-que" id="c-que">trámites auditados se pueden completar sin ayuda.</p>
  <p class="cifra-citable-corte">Índice de trámites completables · corte al …</p>
  <div class="cifra-citable-cita" role="group" aria-labelledby="c-cita">
    <p class="cifra-citable-cita-titulo" id="c-cita">Cómo citar</p>
    <p class="cifra-citable-cita-texto">Observatorio Mexicano de Accesibilidad Digital (OMAD). …</p>
    <div class="cifra-citable-cita-acciones">
      <p class="cifra-citable-estado" role="status"></p>
    </div>
  </div>
</figure>
<script src="…/componentes/cifra-citable/cifra-citable.js"></script>
```

- `.cifra-citable`: una figura nombrada por el número y la frase.
- `.cifra-citable-numero`: el número, a 4xl, en cifras tabulares.
- `.cifra-citable-base`: «de N», dentro del número, a la mitad del tamaño. Si
  no cabe en la línea, baja completa, sin partirse.
- `.cifra-citable-que`: qué mide, pegado al número. Sin esto el número no
  dice nada.
- `.cifra-citable-corte`: la fecha de corte, el universo (cuántos trámites) y
  el nombre del índice.
- `.cifra-citable-cita`: el texto para citar, siempre a la vista y
  seleccionable, y el mensaje de estado, vacío hasta que se copia.
- `cifra-citable.js`, opcional: agrega el botón terciario «Copiar la cita».

## Variantes y estados

No tiene variantes de estilo. Tiene dos formas de escribir el número, y una
regla para las dos: **ninguna cifra sin su base** (dictamen del 2026-11-10).

| Forma | Cuándo | Cómo |
|---|---|---|
| **«X de N»** (la principal) | Siempre que se pueda, y siempre que la base sea chica | `00 <span class="cifra-citable-base">de 00</span>`, y la frase sigue: «trámites auditados se pueden…» |
| Porcentaje | Solo con una base grande, como la cifra nacional | `00 %`, y la frase lleva la base: «…sin ayuda: 00 de 00». Nunca solo. |

**Por qué:** un porcentaje suena igual de sólido con 2 trámites que con 200.
Una dependencia con 1 de 2 trámites accesibles (50 %) saldría mejor que una
con 4 de 10 (40 %), aunque la primera tiene un trámite que falla y la
segunda, seis; y con dos trámites, un solo resultado mueve la cifra de 0 a
100 %. El ejemplo lo muestra. «X de N» es además el mismo lenguaje que la
franja («2 de 6 perfiles»).

- **Sin JavaScript** el bloque es el mismo, sin el botón: la cita se
  selecciona a mano. Nada se esconde.
- **Con JavaScript**, «Copiar la cita» copia el texto y escribe «Cita
  copiada.» en el mensaje de estado, a la vista y para lector de pantalla, sin
  mover el foco. Si el navegador no deja copiar, la cita queda seleccionada y
  el mensaje lo explica.
- La cifra se lee con el cero con diagonal de Atkinson Hyperlegible, que lo
  distingue de la O.

En los ejemplos, el número es un marcador («00 %») y la línea del corte dice
«cifra de ejemplo, no es un resultado de auditoría», pegada al número, para
que se lea aunque alguien recorte la imagen.

## Cómo se oye

Comprobado en el árbol de accesibilidad de Chromium; no se ha probado con un
lector de pantalla.

1. Figura: «00 de 00 trámites auditados se pueden completar sin ayuda».
2. El corte.
3. «Cómo citar, grupo», el texto de la cita y «Copiar la cita, botón».
4. Al copiar: «Cita copiada.», sin mover el foco.

## Criterios WCAG

- **1.3.1 Información y relaciones.** Figura nombrada; grupo con nombre.
- **4.1.3 Mensajes de estado.** «Cita copiada» se anuncia con `role="status"`.
- **2.1.1 Teclado.** El botón es un `button`; sin él, la cita se selecciona con
  el teclado.
- **1.4.10 Reflujo.** A 320 px, si la base no cabe junto al número, baja
  completa a la línea siguiente.

## Falta probar

- **Qué mide el índice y cómo se cita** es de la metodología, no del
  componente: qué cuenta como trámite que «pasa», si se pondera por cuánta
  gente usa cada trámite, y desde qué base se permite un porcentaje. Está en
  `docs/pendientes.md`. El nombre del índice, la frase y el formato de la
  cita del ejemplo son de la maqueta.
- Lectores de pantalla: VoiceOver, NVDA y TalkBack
  ([#4](https://github.com/omad-mx/sistema-de-diseno/issues/4)). En especial,
  que «Cita copiada» se anuncie en todos.
- El portapapeles en Safari y Firefox, y desde un archivo abierto sin
  servidor. En Chromium funciona.
- `forced-colors` en Windows.
