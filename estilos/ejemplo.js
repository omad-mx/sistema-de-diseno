/* Controles de las páginas de ejemplo: tema, ancho y espaciado de texto.
   Es andamio. Ningún componente depende de este archivo. */
(function () {
  var form = document.getElementById('controles');
  var marco = document.getElementById('marco');
  if (!form || !marco) return;
  var raiz = document.documentElement;
  function valor(nombre) { return form.querySelector('input[name="' + nombre + '"]:checked').value; }
  function aplicar() {
    var tema = valor('tema');
    if (tema === 'sistema') raiz.removeAttribute('data-tema'); else raiz.setAttribute('data-tema', tema);
    marco.setAttribute('data-ancho', valor('ancho'));
    raiz.setAttribute('data-espaciado', valor('espaciado'));
  }
  form.addEventListener('change', aplicar);
  aplicar();
})();
