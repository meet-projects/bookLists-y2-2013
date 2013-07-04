$(document).ready(function() {
// Handler for .ready() called.

	$('#login-over').hover(function () {
		$('#login').show();
		}, function() { 
	    $('#login').hover(function() { $(this).slideDown(); }, function() { $(this).hide(); }); 
		//$('#email_field').focus();
	});

 	/**$('.login_field').blur(function() { $('#login').hide(); }); **/

	$('#books').hover(function () {
		$('#cateTable').toggle();
	});
});

