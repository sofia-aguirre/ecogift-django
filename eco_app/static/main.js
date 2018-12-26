$(document).ready(function() {

$('.prod-img').mouseover(function(){
  var imgSrc= $(this).attr('src');
  $('#prod-zoom').attr('src', imgSrc);
});

$('.prod-img').mouseout(function(){
  var nextSrc= $('.prod-img')[0].attr('src');
  $('#prod-zoom').attr('src', nextSrc);
});

});