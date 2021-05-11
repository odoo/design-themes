// Affix menu

$(document).ready(function () {
    $('#affixed_nav').affix({
        offset: {
            top: $('#affixed_nav').offset().top*4
        }
    });
});