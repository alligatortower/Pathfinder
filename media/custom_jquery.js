
$(document).ready(function() {

	$('#character_stats div:not(:first)').hide();
	
	$('#character_nav li').click(function(e) {
		$('#character_stats div').hide();
		$('#character_nav .current').removeClass("current");
		$(this).addClass('current');
		
		var clicked = $(this).find('a:first').attr('href');
		$('#character_stats ' + clicked).fadeIn('fast');
		e.preventDefault();
	}).eq(0).addClass('current');
 
//	alert($('#character_stats').length);
});

