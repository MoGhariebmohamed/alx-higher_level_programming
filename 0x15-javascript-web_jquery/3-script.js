//updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag
$(document).ready(function() {
	$('DIV#red_header').click(function() {
		$('HEADER').addClass('red');
	});
});
