$(document).ready(function() {
// Handler for .ready() called.

	$('#login-over').hover(function () {
		$('#login').show();
	}, function() { 
		$('#login').hover(function() { $(this).show(); }, function() { $(this).hide(); });
	});
});

