$(document).ready(function() {
// Handler for .ready() called.

	$('#login-over').hover(function () {
		$('#login').show();
	}, function() { 
		$('#login').hover(function() { $(this).show(); }, function() { $(this).hide(); });
	});

	$('#books').hover(function () {
		console.log('hovering');
		$('#test').show();
		$('#cateTable').show();
	}, function() { 
		$('#test').hide();
		//$('#cateTable').hover(function() { $(this).show(); }, function() { $(this).hide(); });
	});


});

