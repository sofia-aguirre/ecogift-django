$(document).ready(function() {

// var carHi= $('#carousel').css('height');
// $('#carousel-overlay').css('height', carHi);

$('.prod-img').mouseover(function(){
  var imgSrc= $(this).attr('src');
  $('#prod-zoom').attr('src', imgSrc);
});

$('.prod-img').mouseout(function(){
  var nextSrc= $('.prod-img')[0].attr('src');
  $('#prod-zoom').attr('src', nextSrc);
});

});