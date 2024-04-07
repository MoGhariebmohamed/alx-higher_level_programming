//updates the text color of the <header> element to red (#FF0000) when the user clicks on the tag
$(document).ready(function() {
	$('DIV#toggle_header').click(function() {
	const yourChoice = $('HEADER').attr('class');
	if (yourChoice === 'red') {
		$('HEADER').removeClass('red');
		$('HEADER').addClass('green');
	} else {
		$('HEADER').removeClass('green');
		$('Header').addClass('red');
		}
	});
});
