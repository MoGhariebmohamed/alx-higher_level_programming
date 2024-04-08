// updates the text of the <header> element to New Header!!!
$(document).ready(function () {
  $('DIV#update_header').click(function () {
    $('HEADER').html('New Header!!!');
  });
});
