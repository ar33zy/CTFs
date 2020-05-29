function isEmpty(data)
{
  if(data === "" || !data)
   return true;
  return false;
}

function animateProgress() {
  $(".determinate").each(function() {
    $(this).animate({
      "width": $(this).attr("prog") + "%"
    }, 1000);
  });
}

function getTimeRemaining(utc_end) {
  var t = utc_end - moment.utc().valueOf();
  if(t > 0){
    var seconds = Math.floor((t / 1000) % 60);
    var minutes = Math.floor((t / 1000 / 60) % 60);
    var hours = Math.floor((t / (1000 * 60 * 60)) % 24);
    var days = Math.floor(t / (1000 * 60 * 60 * 24));
  } else {
    var seconds = 00;
    var minutes = 00;
    var hours = 00;
    var days = 00;
  }

  return {
    'total': t,
    'days': days,
    'hours': hours,
    'minutes': minutes,
    'seconds': seconds
  };
}

function initializeTimer() {

  //var utc_end = moment.utc([2019, 8, 13, 06, 00]);
  var utc_end = moment.utc($("#timer").attr("time"));
  function updateClock() {
    var t = getTimeRemaining(utc_end);

    $("#daysSpan").text(('0' + t.days).slice(-2));
    $("#hoursSpan").text(('0' + t.hours).slice(-2));
    $("#minutesSpan").text(('0' + t.minutes).slice(-2));
    $("#secondsSpan").text(('0' + t.seconds).slice(-2));

    if (t.total <= 0) {
      clearInterval(timeinterval);
    }
  }

  updateClock();
  var timeinterval = setInterval(updateClock, 1000);
}

var sponsors_timerinterval = null;
function initializeSponsors() {
  function updateSponsors(speed = "slow"){
      var rouletteclass = ".fade-roulette";
      // find all roulettes that need processing
      $(rouletteclass).each(function() {
	      // this will be the roulette we work on now
	      var $roulette = $(this);

	      // get the index of the element that is currently visible
	      var visindex = $roulette.children(':visible').index();

	      // first, fade out all the children
	      $roulette.children().fadeOut(speed).promise().done(function() {
		      // next, get a random element that is not the one we already saw
		      var sponsorcount = $roulette.children().length;
		      var i = null;
		      do {
			      i = Math.floor(sponsorcount * Math.random());
		      } while(i == null || i == visindex);
		      // finally, fade in this new element
		      $($roulette.children()[i]).fadeIn(speed);
	      });
      });
  }

  if(sponsors_timerinterval == null) {
      console.log("initializeSponsors started");
      // initial run must be fast, speed = 0
      updateSponsors(0);
  }

  sponsors_timerinterval = setInterval(updateSponsors, 20000);
}

function toast(msg){
  Materialize.toast(msg, 2000, 'rounded')
}

$(document).on('click', '#login-tab', function(event){
   $.ajax({
    url: '/login',
    type: 'GET',
    error: function(data){
      toast("Uh-oh something went wrong!")
    },
    success: function(data){
      if(data.result == true)
      {
        $('#data-content').empty();
        $('#data-content').append(data.content);
      }
      else{
        toast(data.msg)
      }
    },dataType:'json'});
});

$(document).on('click', '#register-tab', function(event){
   $.ajax({
    url: '/register',
    type: 'GET',
    error: function(data){
      toast("Uh-oh something went wrong!")
    },
    success: function(data){
      if(data.result == true)
      {
        $('#data-content').empty();
        $('#data-content').append(data.content);
      }
      else{
        toast(data.msg)
      }
    },dataType:'json'});
});

$(document).on('click', '#forgot-password-tab', function(event){
  $.ajax({
   url: '/forgot-password',
   type: 'GET',
   error: function(data){
     toast("Uh-oh something went wrong!")
   },
   success: function(data){
     if(data.result == true)
     {
       $('#data-content').empty();
       $('#data-content').append(data.content);
     }
     else{
       toast(data.msg)
     }
   },dataType:'json'});
});


function login(){
  if(isEmpty($('#login-team').val()) || isEmpty($('#login-password').val()))
  {
   toast("Fill in the credentials");
   return;
  }

  $.ajax({
   url: '/api/login',
   type: 'POST',
   data: "team="+encodeURIComponent($('#login-team').val())+"&password="+encodeURIComponent($('#login-password').val()),
   error: function(){
   },
   success: function(data){
    if(data.result == false)
    {
      toast(data.msg)
    }
    else{
      $(location).attr('href', "/dashboard");
    }
   },dataType:'json'});
}

$(document).on('click', '#login-button', function(event){
  login();
});

function register() {
  if(isEmpty($('#reg-teamname').val()) || isEmpty($('#reg-password').val()))
  {
   toast("Pick a team and password!");
   return;
  }

  if(isEmpty($('#reg-email').val()))
  {
   toast("Enter an email");
   return;
  }

   $.ajax({
    url: '/api/register',
    type: 'POST',
    data: "teamname="+encodeURIComponent($('#reg-teamname').val())+"&email="+encodeURIComponent($('#reg-email').val())+"&password="+encodeURIComponent($('#reg-password').val())+"&captcha="+$('.g-recaptcha-response').val(),
    error: function(){
    },
    success: function(data){
     if(data.result == false)
     {
      toast(data.msg);
     }
     else{
      $(location).attr('href', "/dashboard");
     }
    },dataType:'json'});
}


$(document).on('click', '#register-button', function(event){
  register();
});

function forgot_password() {
  if(isEmpty($('#email-forgot-password').val()))
  {
   toast("Enter an e-mail");
   return;
  }
  toast("If the e-mail exists, a password reset has been sent to it");

  $.ajax({
  url: '/api/forgot-password',
  type: 'POST',
  data: "email="+encodeURIComponent($('#email-forgot-password').val())+"&captcha="+$('.g-recaptcha-response').val()
  });
}

$(document).on('click', '#forgot-password-button', function(event){
  forgot_password();
});


function reset_password() {
  if(isEmpty($('#password').val()) || isEmpty($('#verify-password').val()))
  {
   toast("Enter the new password");
   return;
  }

  if($('#password').val() != $('#verify-password').val())
  {
   toast("Passwords do not match1");
   return;
  }
   $.ajax({
    url: '/api/reset-password',
    type: 'POST',
    data: "password="+encodeURIComponent($('#password').val())+"&token="+encodeURIComponent($('#reset-form').attr('token'))+"&captcha="+$('.g-recaptcha-response').val(),
    error: function(){
    },
    success: function(data){
     if(data.result == false)
     {
      toast(data.msg);
     }
     else{
      $(location).attr('href', "/dashboard");
     }
    },dataType:'json'});
}

$(document).on('click', '#reset-password-button', function(event){
  reset_password();
});

$(document).on('click', '.ctf-tr', function(event){
  $(location).attr('href', $(this).attr("team_id"));
});

$(document).ready(function() {
  gfxHandler();
});

function gfxHandler()
{
  if(localStorage.gfx === undefined)
  {
    localStorage.setItem("gfx", 1);
  }

  if(localStorage.getItem("gfx") == 1)
    $('#gfx-switch').prop('checked', true)
  else
    $('#gfx-switch').prop('checked', false)

  if(localStorage.getItem("gfx") == 1)
  {
    $('#bgvidintro').show();
    //$('#bgvidintro').get(0).play();
  }
  else
  {
    //$('#bgvidintro').get(0).pause();
    $('#bgvidintro').hide();
  }
}

$(document).on('change', '#gfx-switch', function(event){
  if($('#gfx-switch').prop('checked'))
    localStorage.setItem("gfx", 1);
  else
    localStorage.setItem("gfx", 2);
  gfxHandler();
});


function flag(){
  $.ajax({
   url: '/api/flag',
   type: 'POST',
   data: "flag="+encodeURIComponent($('#flag').val()),
   error: function(){
   },
   success: function(data){
    if(data.result == true)
    {

      $(".challbadge-" + data.id).addClass("ctf-badge-grey");
      
      $("#challbox-" + data.id).removeClass("challenge-box");
      $("#challbox-" + data.id).addClass("challenge-box-grey");
      $('#ctf-points').html(data.points + " pts");
      $('#ctf-rank').html("#" + data.rank + ", ");
      $('#flag').val("");
    }
    toast(data.msg);
   },dataType:'json'});
}


$(document).on('click', '#flag-button', function(event){
  flag();
});

$(document).on('keypress', '#flag', function(event){
  if(event.which == 13) {
    flag();
  }
});
