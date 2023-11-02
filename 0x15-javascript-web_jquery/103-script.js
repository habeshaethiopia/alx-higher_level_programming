window.onload = function () {
  function translate () {
    $.get('https://hellosalut.stefanbohacek.dev/?mode=' + $('#language_code').val(), function (data) {
      $('DIV#hello').text(data.hello);
    });
  }

  $('#btn_translate').click(translate);

  $('#language_code').keypress(function (event) {
    if (event.which === 13) {
      translate();
    }
  });
};
