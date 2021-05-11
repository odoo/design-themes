odoo.define('theme_anelusia.main', function (require) {
    'use strict';

    require('web_editor.ready');

    // If menu is open then the page is not scrollable
    $('.navbar-header').on('click', '.navbar-toggle', function () {
        $('body').toggleClass('no-scroll');
    });
});
