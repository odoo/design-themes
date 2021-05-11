$(function(){
    $('#menuToggle, .menu-close').on('click', function(){
        $('body').toggleClass('o_bigslide_open');
    });
    $('main, footer').on('click', function(){
        if ($('body').hasClass('o_bigslide_open')) {
            $('body').removeClass('o_bigslide_open');
        }
    });
});