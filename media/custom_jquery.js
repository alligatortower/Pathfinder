
$(document).ready(function() {
	//bootstrap tabs
	$('#character_nav a').click(function (e) {
                e.preventDefault()
                $(this).tab('show')
		localStorage.setItem('lastTab', $(this).attr('href'));
        })
	//Posts character edits 
	bind_ajax_to_form()
});
function bind_ajax_to_form(){
        $(document).on("submit", "form",  function(event){
		var the_input = $(this).find("input[value='save']") ;
		var tab = $(the_input).attr("name");
		serialized_data = $(this).serialize();
		serialized_data += "&tab=" + encodeURIComponent(tab);
		var url = '/character/' + slug + '/edit/'; 
		$.pjax({
			type: 'POST',
			url: url, 
			data: serialized_data,
			container: "#character_stats",
			complete: function(){
			},
			error: function(){
				console.log("ajax says: POST failure");
			},
		});
		return false;
	}); 

}
$(document).on("pjax:end", function(){
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
