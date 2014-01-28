
$(document).ready(function() {
	//bootstrap tabs
	$('#character_nav a').click(function (e) {
                e.preventDefault()
                $(this).tab('show')
		//save previous tab
		localStorage.setItem('lastTab', $(this).attr('href'));
        })
	//Posts character edits 
	bind_jquery_to_form()

	//Skill Magic
	skill_magic()
});
function bind_jquery_to_form(){
	$(".edit_character_form").on("submit", function(e){
		e.preventDefault();
		var form_data = $(this).serialize();
		submit_form.call(this,[form_data]);
	})
	$(".edit_character_modal_form").on("submit", function(e){
		e.preventDefault();
		var form_data = $(this).serialize();
		$('.modal.in').modal('hide').on("hidden.bs.modal", function(){
			submit_form.call(this,[form_data]);
		})	
	})
}

function submit_form(form_data){
		the_input = $(this).find("button.form_save") ;
		tab = $(the_input).attr("name");
		serialized_data = form_data;
		serialized_data += "&tab=" + encodeURIComponent(tab);
		var url = '/character/' + slug + '/edit/'; 
		$.pjax({
			type: 'POST',
			url: url, 
			data: serialized_data,
			container: "#character_stats",
			success: function(){
			},
			error: function(){
				console.log("pjax says: POST failure");
			},
		});
		return false;
 

}
function skill_magic(){
	$(".skill_details").hide()

	$(".skill_housing")
		//sexy rollover colors
		.mouseover(function(){
			$(this).find(".skill_housing_section").addClass("skill_clicked")
		})
		.mouseleave(function(){
			$(this).find(".skill_housing_section").removeClass("skill_clicked")
			
		})

		// create popovers
		.popover({
			html: true,
			delay: 000,
			animation: false,
			trigger: "hover",
			//set title depending on things
			title: function(){
				if ($(this).find(".class_skill").length == 1){
					var title = "Class Skill"
					if ($(this).find(".skill_ranks .skill_component_number").html() >= 1) {
						title = title + " +3"
					}
					else {
						title = title + ", no ranks yet"
					}
					return title
				}	
			},
			content:function(){
				return $(this).find(".skill_details").html()
			}
				
		})
		.on("click", function(){
			var skill = $(this).find(".skill_name span").html()
			var modal_id = "#" + skill + "_modal"
			$(modal_id).modal()	
		})
}
	
$(document).on("pjax:end", function(){
	console.log("pjax has ended")
	//redo bindings after pseudo page refresh
	bind_jquery_to_form()
	skill_magic()


	//Then return to correct tab
	$("div#character_stats div.active").removeClass("active in");
	$("ul#character_nav li.active").removeClass("active"); //Remove default tab being active	
	var lastTab = localStorage.getItem('lastTab');
	if (lastTab) {
		var my_tab = $("ul#character_nav li").find("a[href='" + lastTab +"']")
		var string_tab = String(lastTab)
		var tab_id = string_tab.replace("#","")
		var my_content = $(document).find("div[id='" + tab_id +"']")
		my_tab.parent().addClass("active"); //add previous tab as active
		my_content.addClass("active in")
		$(my_tab).tab('show') 
	};
})
