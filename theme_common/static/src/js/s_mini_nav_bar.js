(function() {
    // TODO register code in snippet animation
    $('.s_mini_nav_bar a[href*=#]:not([href=#])').on('click', function(event){
        var index = $(this).parent().index();
        var target = $('.o_scroll_nav').get(index);
        console.log(event,target);
        if(target) {
            event.preventDefault();
            $('html,body').animate({ scrollTop: $(target).offset().top }, 1000);
        }

    });
})();
