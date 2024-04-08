// fetches the character name from this URL
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, status) {
  $('DIV#hello').html(data.hello);
});
