$(document).ready(function () {
    console.log($('nav').height());
    $('body').css("padding-top",$('nav:first').height()+20);
    $('#siderbar').css('margin-top',$('nav:first').height()+20);
    $('[data-toggle="offcanvas"]').click(function () {
      $('.row-offcanvas').toggleClass('active')
    });
  });