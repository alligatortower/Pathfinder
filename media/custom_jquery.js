
$(document).ready(function() {
	//bootstrap tabs
	$('#character_nav a').click(function (e) {
                e.preventDefault()
                $(this).tab('show')
		//save previous tab
		localStorage.setItem('lastTab', $(this).attr('href'));
        })
	//Posts character edits 
	bind_jquery_submit_logic()
	bind_other_jquery_magic()
});
function bind_jquery_submit_logic(){
	$(".add_base_class_form").on("submit", function(e){
		e.preventDefault()
		var form_data = $(this).serialize();
		var url = '/character/' + slug + '/add_base_class/';
		$('.modal.in').modal('hide').on("hidden.bs.modal", function(){
			submit_form(form_data, url);
		})
	})
	$(".edit_details_form").on("submit", function(e) {
		e.preventDefault()
		var form_data = $(this).serialize();
		var url = '/character/' + slug + '/edit_details/';
		$('.modal.in').modal('hide').on("hidden.bs.modal", function(){
			submit_form(form_data, url);
		})

	})
	$(".edit_base_class_form").on("submit", function(e){
		e.preventDefault();
		var form_data = $(this).serialize();
		var url = '/character/' + slug + '/edit_base_class/'
		var class_name = $(this).closest(".modal").attr("data-type")
		form_data += "&class_name=" + class_name;
		$('.modal.in').modal('hide').on("hidden.bs.modal", function(){
			submit_form(form_data, url);
		})
	})
	$(".edit_health_modal_form").on("submit", function(e) {
		e.preventDefault();
		var form_data = $(this).serialize();
		var url = '/character/' + slug + '/edit_health/'
		$('.modal.in').modal('hide').on("hidden.bs.modal", function(){
			submit_form(form_data, url);
		})
	})
	$(".edit_initiative_modal_form").on("submit", function(e) {
		e.preventDefault();
		var form_data = $(this).serialize();
		var url = '/character/' + slug + '/edit_initiative/'
		$('.modal.in').modal('hide').on("hidden.bs.modal", function(){
			submit_form(form_data, url);
		})
	})
	$(".edit_speed_modal_form").on("submit", function(e) {
		e.preventDefault();
		var form_data = $(this).serialize();
		var url = '/character/' + slug + '/edit_speed/'
		$('.modal.in').modal('hide').on("hidden.bs.modal", function(){
			submit_form(form_data, url);
		})
	})
	$(".edit_attack_bonus_modal_form").on("submit", function(e){
		e.preventDefault()
		var form_data = $(this).serialize();
		var url = '/character/' + slug + '/edit_base_attack/'
		$('.modal.in').modal('hide').on("hidden.bs.modal", function(){
			submit_form(form_data, url);
		})

	})
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
	$(".skill_modal_form_save_button").on("click", function(e){
		e.preventDefault();
		var form_data = $(this).closest("form").serialize();
		var skill_modal = $(this).closest(".modal")
		var this_modal = skill_modal.attr("data-type")
		if (this_modal == "edit_craft_or_profession"){
			var url = '/character/' + slug + '/edit_multiskill/'; 
//			var skill_domain = skill_modal.find("#multiskill_domain").html()
//			var skill_type = skill_modal.find("#skill_type").html()
//			form_data += "&skill_domain=" + encodeURIComponent(skill_domain);
//			form_data += "&skill_type=" + encodeURIComponent(skill_type);
		}
		else if (this_modal == "add_craft_or_profession_modal"){
			var url = '/character/' + slug + '/add_multiskill/';
		}
		else {
			var url = '/character/' + slug + '/edit_skills/';
			form_data += "&which_form=skills_form"

		}
//		form_data += "&modal=" + encodeURIComponent(this_modal);
		$('.modal.in').modal('hide').on("hidden.bs.modal", function(){
			submit_form.call(this, form_data, url);
		})	
	})
	$(".edit_max_ranks_button").on("click", function(e){
		e.preventDefault();
		var url = '/character/' + slug + '/edit_skills/';
		var form_data = $(this).closest(".edit_max_ranks_form").serialize();
		form_data += "&which_form=max_ranks_form";
		submit_form.call(this, form_data, url) 	
	})
	$(".base_class_delete").on("click", function(e){
		e.preventDefault();
		var class_name = $(this).closest(".modal").attr("data-type")
		var url = '/character/' + slug + '/delete_base_class/'
		var form_data = "&class_name=" + encodeURIComponent(class_name);
		$('.modal.in').modal('hide').on("hidden.bs.modal", function(){
			submit_form(form_data, url);
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
			html: true,
			container: 'body',
			delay: 000,
			animation: false,
			trigger: "hover",
			placement: "auto top",
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
function bind_other_jquery_magic(){
	$(".combatstat_container")
		.mouseover(function(){
			$(this).find("h4").addClass("combat_mouseover")
		})
		.mouseleave(function(){
			$(this).find("h4").removeClass("combat_mouseover")
		})
	$(".ability_container").on("click", function(e) {
		e.stopPropagation();
		e.preventDefault();
		$("#edit_abilities_modal").modal()
	})
	$(".open_add_base_class_modal").on("click", function(e){
		e.preventDefault();
		$("#add_base_class_modal").modal()
	})
	$(".base_class_container").on("click", function(e){
		e.stopPropagation();
		e.preventDefault();
		var which_class = $(this).attr("data-modal")
		var which_class_modal = "#" + which_class + "_modal"
		$(which_class_modal).modal()
	})
	$(".health_container").on("click", function(e) {
		e.stopPropagation();
		e.preventDefault();
		$("#health_modal").modal()	
	})
	$(".initiative_container").on("click", function(e) {
		e.stopPropagation();
		e.preventDefault();
		$("#initiative_modal").modal()	
	})
	$(".speed_container").on("click", function(e) {
		e.stopPropagation();
		e.preventDefault();
		$("#speed_modal").modal()	
		
	})
	$(".character_description_main_container").on("click", function(e) {
		e.stopPropagation();
		e.preventDefault();
		$("#edit_details_modal").modal()

	})
	$(".modal_base_class_attack_bonus_container").on("click", function(e){
		e.stopPropagation();
		e.preventDefault();
		var which_class = $(this).attr("data-modal")
		var which_class_modal = "#" + which_class + "_modal"
		$('.modal.in').modal('hide').on("hidden.bs.modal", function(){
			$(which_class_modal).modal()
		})
	})
	$(".base_attack_container").on("click", function(){
		$("#attack_bonus_modal").modal()
	})

	$(".skill_housing")
		//sexy rollover colors
		.mouseover(function(){
			$(this).addClass("skill_clicked")
		})
		.mouseleave(function(){
			$(this).removeClass("skill_clicked")
		})

		// create popovers
				
		.on("click", function(){
			if (!$(this).hasClass("craft_or_profession_housing")){
			var skill = $(this).find(".skill_name span").html()
			var modal_id = "#" + skill + "_modal"
			$(modal_id).modal()	
			}
		})

	//Gray out Trained Skills without ranks
	$(".skill_housing").each(function(index){
	        if ($(this).hasClass("trained_skill") && $(this).find(".skill_ranks").find(".skill_component_number").html() <= 0){
			$(this).css("background-color","#E9E9E9")
		};
		if ($(this).hasClass("armor_penalty") && $(this).find(".armor_penalty_container").find(".skill_component_number").html() > 0) {
			$(this).find(".skill_total").css("color","red")
			$(this).find(".armor_penalty_container").css("color","red")
		}
	})

	$(".add_craft_or_profession").on("click", function(){
		$("#add_craft_or_profession_modal").modal()
	})
	$(".craft_or_profession_housing").on("click", function(){
		var which_one = $(this).attr("id")
		$("#" + which_one +"_modal" ).modal()
	})
	$(".ranks_total").popover({
		html: true,
		container: 'body',
		delay: 000,
		animation: false,
		trigger: "click",
		placement: "auto top",
		content: $(".max_ranks_form_popover").html()
	})
	$(".max_ranks_form_popover").hide()
}
	
$(document).on("pjax:success", function(){
	console.log("pjax has succeeded")
	//redo bindings after pseudo page refresh
	bind_jquery_submit_logic()
	bind_other_jquery_magic()


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
