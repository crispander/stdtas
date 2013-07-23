 function login() {
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