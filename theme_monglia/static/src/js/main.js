odoo.define('theme_monglia.main', function (require) {
    'use strict';

    require('web_editor.ready');

    $('#menuToggle, .menu-close').on('click', function () {
        $('body').toggleClass('o_bigslide_open');
    });
    $('main, footer, nav').on('click', function () {
        if ($('body').hasClass('o_bigslide_open')) {
            $('body').removeClass('o_bigslide_open');
        }
    });
});
