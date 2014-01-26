
$(document).ready(function() {
/*
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

	
	$(function () {
    		$('#character_nav a:last').tab('show')
	})
	
*/

	//Posts character edits 
        $('.edit_character_form').submit(function(){
		var the_input = $(this).find("input[value='save']") ;
		var tab = $(the_input).attr("name");
		var this_tab = $(this).parent()
		serialized_data = $(this).serialize();
		serialized_data += "&tab=" + encodeURIComponent(tab);
		$.ajax({
			type: 'POST',
			url: '/character/' + slug + '/edit/', 
			data: serialized_data,
			success: function(data){
				console.log(this_tab.attr("id"));	
				this_tab.load("/ #character_ability_block");
			//	$('#character_stats').load(' #character_stats').children(); //, function(){$(this).children().unwrap()})
			//	$(this).addClass('current');
			//	$('#character_stats div:not(.current)').hide();
			},
			error: function(){
				console.log("ajax says: POST failure");
			},
		});
		return false;
	});
});
/*	
$(document).ready(function() {
	var edit_character_form = $('#edit_character_form');
        edit_character_form.submit(function () {
                $.ajax({
                        type: 'POST',
                        url: '/character/' + slug + '/edit/',
                        data: $(this).serialize(),
                        success: function(response){
                                if (response === "success"){
                                }
                                else if (response === "badSubmit") {
                                        alert("woah bad submit baby");
                                }
                        },
                        error: function(){
                                alert("ajax has returend the ERROR");
                        },
                });
                return false;
        });
	
}); */
//	alert($('#character_stats').length);
