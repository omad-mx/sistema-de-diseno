/* OMAD — cifra citable: botón «Copiar la cita».
   Mejora progresiva: sin este script, el texto de la cita se ve completo y
   se puede seleccionar a mano. Con él, cada bloque «Cómo citar» gana un
   botón que copia el texto y lo confirma por escrito, en un mensaje de
   estado que el lector de pantalla anuncia (WCAG 4.1.3). */
(function () {
  var bloques = document.querySelectorAll('.cifra-citable-cita');
  for (var i = 0; i < bloques.length; i++) preparar(bloques[i]);

  function preparar(bloque) {
    var texto = bloque.querySelector('.cifra-citable-cita-texto');
    var acciones = bloque.querySelector('.cifra-citable-cita-acciones');
    var estado = bloque.querySelector('.cifra-citable-estado');
    if (!texto || !acciones || !estado) return;

    var boton = document.createElement('button');
    boton.type = 'button';
    boton.className = 'boton';
    boton.setAttribute('data-variante', 'terciario');
    boton.textContent = 'Copiar la cita';
    acciones.insertBefore(boton, estado);

    boton.addEventListener('click', function () {
      var cita = texto.textContent.replace(/\s+/g, ' ').trim();
      copiar(cita).then(function () {
        avisar('Cita copiada.');
      }, function () {
        seleccionar(texto);
        avisar('No se pudo copiar. La cita quedó seleccionada: cópiala con el teclado.');
      });
    });

    function avisar(mensaje) {
      // Se vacía primero para que el mismo mensaje se anuncie otra vez.
      estado.textContent = '';
      window.setTimeout(function () { estado.textContent = mensaje; }, 50);
    }
  }

  function copiar(cita) {
    if (navigator.clipboard && navigator.clipboard.writeText) return navigator.clipboard.writeText(cita);
    return Promise.reject(new Error('Sin portapapeles'));
  }

  function seleccionar(el) {
    var rango = document.createRange();
    rango.selectNodeContents(el);
    var sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(rango);
  }
})();
