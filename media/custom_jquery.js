
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
		the_input = $(this).find("button.form_save") ;
		tab = $(the_input).attr("name");
		if (tab == "ability_tab"){
			var url = '/character/' + slug + '/edit_abilities/'; 
		}
		else if (tab == "combatstats_tab"){
			var url = '/character/' + slug + '/edit_combatstats/'; 
		}
		form_data += "&tab=" + encodeURIComponent(tab);
		submit_form.call(this,form_data,url);
	})
	$(".edit_character_modal_form").on("submit", function(e){
		e.preventDefault();	
	})
	$(".modal_form_save_button").on("click", function(e){
		e.preventDefault();
		var form_data = $(this).closest(".edit_character_modal_form").serialize();
		var skill_modal = $(this).closest(".modal")
		var this_modal = skill_modal.attr("data-type")
		console.log(this_modal)
		if (this_modal == "edit_craft_or_profession"){
			var url = '/character/' + slug + '/edit_multiskill/'; 
			var skill_domain = skill_modal.find("#multiskill_domain").html()
			var skill_type = skill_modal.find("#skill_type").html()
			form_data += "&skill_domain=" + encodeURIComponent(skill_domain);
			form_data += "&skill_type=" + encodeURIComponent(skill_type);
		}
		else if (this_modal == "add_craft_or_profession_modal"){
			var url = '/character/' + slug + '/add_multiskill/';
		}
		else {
			var url = '/character/' + slug + '/edit_skills/';

		}
		form_data += "&modal=" + encodeURIComponent(this_modal);
		form_data += "&tab=" + encodeURIComponent("skills_tab");
		$('.modal.in').modal('hide').on("hidden.bs.modal", function(){
			submit_form.call(this, form_data, url);
		})	
	})
	$(".craft_or_profession_delete").on("click", function(e){
		e.preventDefault();
		var form_data
		var skill_modal = $(this).closest(".modal")
		var this_modal = skill_modal.attr("data-type")
		var url = '/character/' + slug + '/delete_multiskill/'; 
		var skill_domain = skill_modal.find("#multiskill_domain").html()
		var skill_type = skill_modal.find("#skill_type").html()
		form_data += "&skill_domain=" + encodeURIComponent(skill_domain);
		form_data += "&skill_type=" + encodeURIComponent(skill_type);
		$('.modal.in').modal('hide').on("hidden.bs.modal", function(){
			submit_form.call(this, form_data, url);
		})	
	})
}

function submit_form(form_data, url){
		$.pjax({
			type: 'POST',
			url: url, 
			data: form_data,
			push: false,
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
			$(this).find(".skill_housing").addClass("skill_clicked")
		})
		.mouseleave(function(){
			$(this).find(".skill_housing").removeClass("skill_clicked")
			
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
			if (!$(this).hasClass("craft_or_profession_housing")){
			var skill = $(this).find(".skill_name span").html()
			var modal_id = "#" + skill + "_modal"
			$(modal_id).modal()	
			}
		})
	$(".add_craft_or_profession").on("click", function(){
		$("#add_craft_or_profession_modal").modal()
	})
	$(".craft_or_profession_housing").on("click", function(){
		var which_one = $(this).attr("id")
		$("#" + which_one +"_modal" ).modal()
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
