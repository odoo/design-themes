$(document).ready(function () {
    /* /////// If menu is open then the page is not scrollable //////// */
    $('.navbar-header').on('click', '.navbar-toggle', function () {
        $('body').toggleClass('no-scroll');
    });
});