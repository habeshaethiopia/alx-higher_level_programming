
window.onload = function () {
  $('#btn_translate').click(function () {
    $.get('https://hellosalut.stefanbohacek.dev/?mode=' + $('#language_code').val(), function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
};
