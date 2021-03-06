function refreshconf1(){
	value = $( "#conf-borde" ).slider("value");
	$("#preview").css("border-width", value + "px");
}

function refreshconf2(){
	value = $( "#conf-borde-radius" ).slider("value");
	$("#preview").css("border-radius", value + "%" );
}

function load_options(){
	value = $("#mytextarea").val();
	value = value.split("\n");
	html = "";
	htmlR = "";
		landscape = $("#landscape").val();
		if(landscape == "h"){
			for(i=0;value.length>i;i++){
				if(type_poll == "radio"){
					html += "<div class='block_std-options_cris' ><input type='radio' 'name='select'> " + value[i] + "</div>";
					htmlR += "<div class='block_std-options_cris' ><input type='radio' 'name='select'> " + value[i] + " <br /><div class='bar_progress_poll'></div>&nbsp;&nbsp;0(0%)</div>";
				}
				else if(type_poll == "checkbox"){
					html += "<div class='block_std-options_cris' ><input type='checkbox' 'name='select'> " + value[i] + "</div>";
					htmlR += "<div class='block_std-options_cris' ><input type='checkbox' 'name='select'> " + value[i] + "<br /><div class='bar_progress_poll'></div>&nbsp;&nbsp;0(0%)</div>";
				}
				else if(type_poll == "textarea"){
					html += "<textarea rows='4'></textarea>";
					break;
				}
				//options_array.push(value[i]);
			}
		}else{
			//size = ($("#subblock").width() / value.length) - 3;
			size = (97 / value.length);

			for(i=0;value.length>i;i++){
				if(type_poll == "radio"){
					html += "<div style='height:98%;float:left;width:"+ size +"%' class='block_std-options_cris' ><input type='radio' 'name='select'> " + value[i] + "</div>";
					htmlR += "<div style='height:98%;float:left;width:"+ size +"%' class='block_std-options_cris' ><input type='radio' 'name='select'> " + value[i] + "<br /><div class='bar_progress_poll'></div>&nbsp;&nbsp;0(0%)</div>";
				}
				else if(type_poll == "checkbox"){
					html += "<div style='height:98%;float:left;width:"+ size +"%' class='block_std-options_cris' ><input type='checkbox' 'name='select'> " + value[i] + "</div>";
					htmlR += "<div style='height:98%;float:left;width:"+ size +"%' class='block_std-options_cris' ><input type='checkbox' 'name='select'> " + value[i] + "<br /><div class='bar_progress_poll'></div>&nbsp;&nbsp;0(0%)</div>";
				}
				else if(type_poll == "textarea"){
					html += "<textarea rows='4'></textarea>";
					break;
				}
				//options_array.push(value[i]);
			}
		}
	$("#subblock").html(html);
	$("#subblock_results").html(htmlR);
}

function upload_configuration(){
	$(".button_submit").css("display", "none");
	$("#cargando").css("display", "block");
	csrf = $("input[name=csrfmiddlewaretoken]").val();
	data = $("#formstdgenerator").serialize() + "&csrfmiddlewaretoken=" + csrf;
	$.ajax({
		type:"POST",
		url: "submit/",
		data: data,
		success: function(data){
			id_poll = data.id;
			$("#cargando").css("display", "none");
			$("#show input").attr("value", '<script id="generator_script_crispander_'+ data.id +'" src="http://www.generadorencuestas.com/render/poll/'+data.id+'/" type="text/javascript"></script>');
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
	$("input[name='font_size_block']").val(val);
	$("#preview #subblock").css("font-size", val + "px");
	$("#preview #subblock_results").css("font-size", val + "px");
}

function set_font_title(){
	val = $("#font_size_title").val();
	$("input[name='font_size_title']").val(val);
	$("#preview #preview_question").css("font-size", val + "px");
}


 function login() {
	nombre = document.getElementById("question").value;
    FB.login(function(response) {
        if (response.authResponse) {
            console.log(response);
            FB.api('/me', function(response) {
                        //var body = 'Bienvenidos a la electro music encontraras, un sitio dedicado a la musica electronica http://videos-cristanmontoya.dotcloud.com';
                                var obj = {
                                    method: 'feed',
                                    name: 'Generador encuestas sociales',
                                    link: 'https://www.generadorencuestas.com/polls/' + id_poll,
                                    picture: "http://www.generadorencuestas.com/static/images/icon_polls.png",
                                    caption: 'Crea tus encuestas personalizadas y compartelas con tus amigos, y conoce la opinion del publico',
                                    description: "¿ " + nombre + "?",
                                    message: response.first_name + ' ha creado esta encuesta que quiere compartir haz click para ir a verla.',
                                };
                        FB.api('/me/feed', 'post', obj, function(response) {
                        if (!response || response.error) {
                            console.log('Error occured');
                        } else {
                            console.log('Post ID: ' + response.id);
                        }
                        });
            });
        } else {
            console.log("sin loguearse");
        }
    }, {scope: 'email,publish_stream'});
}

function testAPI() {
console.log('Bienvenido buscando informacion');
FB.api('/me', function(response) {
    console.log('Bienvenido' + response.name + '.');
});
}

function oauth_face(){
    //var body = 'Bienvenidos a la electro music encontraras, un sitio dedicado a la musica electronica <a href="http://videos-cristanmontoya.dotcloud.com/">Ir a Conocerla</a>';
    //FB.api('/me/feed', 'post', { message: body }, function(response) {
        //if (!response || response.error) {
            //console.log('Error occured');
        //} else {
            //console.log('Post ID: ' + response.id);
        //}
//});

}

function logout(){
    FB.logout(function(){
        location.href="/process/logout/";
    });
}

  // Additional JS functions here
  window.fbAsyncInit = function() {
    FB.init({
      appId      : '419360901469098', // App ID
      channelUrl : 'www.generadorencuestas.com', // Channel File
      status     : true, // check login status
      cookie     : true, // enable cookies to allow the server to access the session
      xfbml      : true  // parse XFBML
    });

  FB.getLoginStatus(function(response) {
    if (response.status === 'connected') {
    //testAPI();
    //oauth_face();
  } else if (response.status === 'not_authorized') {
        console.log("conectado pero no autorizado");
  } else {
        console.log("sin conexion a facebook");
  }
 });

  };

  // Load the SDK Asynchronously
  (function(d){
     var js, id = 'facebook-jssdk', ref = d.getElementsByTagName('script')[0];
     if (d.getElementById(id)) {return;}
     js = d.createElement('script'); js.id = id; js.async = true;
     js.src = "//connect.facebook.net/en_US/all.js";
     ref.parentNode.insertBefore(js, ref);
   }(document));


jQuery.fn.extend({
insertAtCaret: function(myValue){
  return this.each(function(i) {
    if (document.selection) {
      //For browsers like Internet Explorer
      this.focus();
      var sel = document.selection.createRange();
      sel.text = myValue;
      this.focus();
    }
    else if (this.selectionStart || this.selectionStart == '0') {
      //For browsers like Firefox and Webkit based
      var startPos = this.selectionStart;
      var endPos = this.selectionEnd;
      var scrollTop = this.scrollTop;
      this.value = this.value.substring(0, startPos)+myValue+this.value.substring(endPos,this.value.length);
      this.focus();
      this.selectionStart = startPos + myValue.length;
      this.selectionEnd = startPos + myValue.length;
      this.scrollTop = scrollTop;
    } else {
      this.value += myValue;
      this.focus();
    }
  });
}
});

$(function(){
//dialogo para creat una imagem
    $( "#dialog-form" ).dialog({
      autoOpen: false,
      height: 600,
      width: 700,
      modal: true,
      buttons: {
        "Ingresar Imagen": function() {
          im = $("#imagen_input").val();
		  size = $("#form_image_input").val();
		  if(im != ""){
			$('#mytextarea').insertAtCaret("<img src='" +im+ "' height='"+size+"' />");
			$( "#imagen_input" ).val("");
			load_options();
			$( "#dialog-form" ).dialog( "close" );
		  }
		  },
      Cancel: function() {
          $( this ).dialog( "close" );
        }
      },
      close: function() {
      }
    });

	
    $( "#dialog-form-preview" ).dialog({
      autoOpen: false,
      height: 600,
      width: 700,
      modal: true,
      buttons: {
        "Poner de nuevo en la ventana anterior": function() {
             $( this ).dialog( "close" );
		  },
      },
      close: function() {
		 datos_Actuales = $("#dialog-form-preview").html();
		 $("#dialog-form-preview").html('');
		 $("#content_preview").html(datos_Actuales);
		 $( "#dialog_preview" ).css("display", "inline-block");
      },
      show: {
        effect: "blind",
        duration: 1000
      },
      hide: {
        effect: "explode",
        duration: 1000
      },
	  modal:false
    });
	
	$(".ui-widget-overlay").attr('style','background-color: #000; opacity:1; z-index:1000;');
	
	
	//boton que habre el dialogo de crear una imagen.
	  $( "#create-image" )
		  .button({
		    icons: {
			primary: "ui-icon-image"
			},
			text: false
		  })
		  .click(function() {
			$( "#dialog-form" ).dialog( "open" );
	});

	
	//boton que habre el dialogo de 'preview'
	  $( "#dialog_preview" )
		  .button({
		    icons: {
			primary: "ui-icon-newwin"
			}
		  })
		  .click(function() {
			 datos_Actuales = $("#content_preview").html();
			 $("#content_preview").html('');
			 $("#dialog-form-preview").html(datos_Actuales);
			 //ocultar boton
			 $( "#dialog_preview" ).css("display", "none");
			$( "#dialog-form-preview" ).dialog( "open" );
			
	});
		  
	  $( "#create-br" )
		  .button({
		    icons: {
			primary: "ui-icon-carat-2-e-w"
			},
			text: false
		  })
		  .click(function() {
			$('#mytextarea').insertAtCaret("<br />");
			load_options();
          });

	  $( "#create-b" )
		  .button()
		  .click(function() {
			if(estado_bold){
				$('#mytextarea').insertAtCaret("<b>");
				estado_bold = false;
				}
			else{
				$('#mytextarea').insertAtCaret("</b>");
				estado_bold = true;
				load_options();
				}
          });

$("#imagen_input").keyup(function(){
	ima = $("#imagen_input").val();
	html = "<img src='"+ima+"' height='' />";

	$("#preview_image").html(html);
});

	//js height
	  $( "#slider_form_image_input" ).slider({
      range: "max",
	  min:10,
      max: 200,
      value: 40,
      slide: function( event, ui ){
		$( "#form_image_input" ).val( ui.value);
		$("#preview_image img").css("height", ui.value );
	  },
	  });
	  $( "#form_image_input" ).val( $( "#slider_form_image_input" ).slider( "value" ));

});

function toogle_subblocks(){
	val = $("#subblock").css("display");
	if(val != "none"){
		$("#subblock").slideUp("slow");
		$("#subblock_results").delay(800).fadeIn("slow");
		$("#info_state_subblock").html("encuesta");
	}else{
		$("#subblock").delay(800).fadeIn("slow");
		$("#subblock_results").slideUp("slow");
		$("#info_state_subblock").html("resultados");
	}
}