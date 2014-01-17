$(document).ready(function() {
        // POSTing character edits
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
});

