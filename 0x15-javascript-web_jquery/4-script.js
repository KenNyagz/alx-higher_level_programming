$(document).ready(function () {
  $('#toggle_header').click(function() {
    if ($('header').hasclass('red')){
      $('header').removeclass('red').addClass('green');
    } else if ($('header').hasClass('green')) {
      $('header').removeclass('green').addClass('red');
    } else {
      $('header').addclass('red');
    }
  });
});
