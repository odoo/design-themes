odoo.define('theme_kea.affix', function (require) {
    'use strict';

    // Affix menu

    $(document).ready(function () {
        $('.navbar-static-top .container').affix({
            offset: {
                top: $('.navbar-static-top .container').offset().top*6
            }
        });
    });

});
