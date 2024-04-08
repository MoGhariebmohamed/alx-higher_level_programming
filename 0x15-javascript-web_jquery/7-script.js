// fetches the character name from this URL
$.get('https://swapi.co/api/people/5/?format=json', function (data, status) {
  $('DIV#character').html(data.name);
});
