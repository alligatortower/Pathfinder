
$(document).ready(function() {

	// Tabs on character page
	$('#character_stats div:not(:first)').hide();
	$('#character_nav li').click(function(e) {
		$('#character_stats div').hide();
		$('#character_nav .current').removeClass("current");
		$(this).addClass('current');
		
		var clicked = $(this).find('a:first').attr('href');
		$('#character_stats ' + clicked).fadeIn('fast');
		e.preventDefault();
	}).eq(0).addClass('current');
 
});

$(document).ready(function() {
	// POSTing character edits
	var edit_character_form = $('#edit_character_form');
	edit_character_form.submit(function () {
		$.ajax({
			type: 'POST',
			url: '/character/edit/',
			data: 'title=ajax call',
			datatype: 'json',
		});
		return false;

	});
});

//	alert($('#character_stats').length);
