$(document).ready(function() {
// Handler for .ready() called.

	$('#login-over').hover(function () {
		$('#login').show();
		}, function() { 
	    $('#login').hover(function() { $(this).show(); }, function() { $(this).hide(); }); 
		//$('#email_field').focus();
	});

	$('#login').focus(function() {
		$('#login').unbind('hover');
		$('#login').hover(function() { $(this).show(); }, function() {});
	}, function() {});

 	$('.login_field').focus(function() { 
		$('#login').unbind('hover');
		$('#login').hover(function() {  $(this).show(); }, function() {});
	}); 

	$('#books').hover(function () {
		$('#cateTable').toggle();
	});
});

