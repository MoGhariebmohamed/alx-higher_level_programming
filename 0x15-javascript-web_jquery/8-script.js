// fetches the character name from this URL
$.get('https://swapi.co/api/people/5/?format=json', function (data, status) {
  let i = 0;
  while (i < data.count) {
    $('UL#list_movies').append('<li>' + data.results[i].title + '</li>');
    i++;
  }
});
