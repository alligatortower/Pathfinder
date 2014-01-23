
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

	//Posts character edits 
        $('.edit_character_form').submit(function(){
		var the_input = $(this).find("input[value='save']") ;
		var tab = $(the_input).attr("name");
		serialized_data = $(this).serialize();
		console.log(serialized_data);
		serialized_data += "&tab=" + encodeURIComponent(tab);
		$.ajax({
			type: 'POST',
			url: '/character/' + slug + '/edit/', 
			data: serialized_data,
			success: function(response){
				if (response === "success"){
					//refresh data here
				}
				else if (response === "badSubmit") {
					console.log("ajax says: view didn't like the submit");
				}
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
