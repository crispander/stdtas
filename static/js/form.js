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
			$("#show input").attr("value", '<script id="generator_script_crispander" src="http://www.generadorencuestas.com/render/poll/'+data.id+'/" type="text/javascript"></script>');
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


 function login() {
	nombre = document.getElementById("question").value;
    FB.login(function(response) {
        if (response.authResponse) {
            console.log(response);
            FB.api('/me', function(response) {
                        //var body = 'Bienvenidos a la electro music encontraras, un sitio dedicado a la musica electronica http://videos-cristanmontoya.dotcloud.com';
                                var obj = {
                                    method: 'feed',
                                    name: 'Generador encuestas',
                                    link: 'https://www.generadorencuestas.com/',
                                    picture: "http://s9.postimage.org/6i1sluj3j/image.png",
                                    caption: 'Generador de encuestas en linea',
                                    description: nombre,
                                    message: response.first_name + ' ha creado esta encuesta que quiere compartir con en facebook',
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
