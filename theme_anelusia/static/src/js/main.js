odoo.define('theme_anelusia.main', function (require) {
    'use strict';

    var base = require('web_editor.base');

    base.ready().then(function () {
        // If menu is open then the page is not scrollable
        $('.navbar-header').on('click', '.navbar-toggle', function () {
            $('body').toggleClass('no-scroll');
        });
    });
});
