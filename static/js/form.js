function refreshconf1(){
	value = $( "#conf-borde" ).slider("value");
	$("#preview").css("border-width", value + "px");
}

function refreshconf2(){
	value = $( "#conf-borde-radius" ).slider("value");
	$("#preview").css("border-radius", value + "%" );
}

function load_options(){
	value = $("#options").val();
	value = value.split("\n");
	html = "";
		for(i=0;value.length>i;i++){
			if(type_poll == "radio"){
				html += "<div class='block_std-options_cris' ><input type='radio' 'name='select'> " + value[i] + "<small>votes: 0</small></div>";
			}
			else if(type_poll == "checkbox"){
				html += "<div class='block_std-options_cris' ><input type='checkbox' 'name='select'> " + value[i] + "<small>votes: 0</small></div>";
			}
			else if(type_poll == "textarea"){
				html += "<textarea rows='4'></textarea>";
				break;
			}
			//options_array.push(value[i]);
		}
	$("#subblock").html(html);
}

function upload_configuration(){
	$(".button_submit").css("display", "none");
	$("#cargando").css("display", "block");
	data = $("#formstdgenerator").serialize();
	$.ajax({
		type:"GET",
		url: "submit",
		data: data,
		success: function(data){
			$("#cargando").css("display", "none");
			$("#show input").attr("value", '<script id="generator_script_crispander" src="http://localhost:8000/render/poll/'+data.id+'/" type="text/javascript"></script>');
			$("#show #go_see").attr("href", "/polls/" + data.id + "/")
			$("#show").css("display", "block");

		},
		fail: function() {
			$(".button_submit").css("display", "block");
		}
	});
	
	return false;
}

function set_font_block(){
	val = $("#font_size_block").val();
	$("#preview #subblock").css("font-size", val + "px");
}

function set_font_title(){
	val = $("#font_size_title").val();
	$("#preview #preview_question").css("font-size", val + "px");
}