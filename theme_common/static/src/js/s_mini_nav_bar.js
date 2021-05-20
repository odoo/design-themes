odoo.define('theme_common.s_mini_nav_bar', function (require) {
'use strict';

var publicWidget = require('web.public.widget');

publicWidget.registry.miniNavbarScroll = publicWidget.Widget.extend({
    selector: '.s_mini_nav_bar a[href*="#"]:not([href="#"])',
    events: {
        'click': '_onClick',
    },

    //----------------------------------------------------------------------
    // Handlers
    //----------------------------------------------------------------------

    /**
     * Called on click on the mini navbar link -> scroll to the section.
     *
     * @private
     */
    _onClick: function (ev) {
        var index = $(this).parent().index();
        var target = $('.o_scroll_nav').get(index);
        if (target) {
            ev.preventDefault();
            $('html,body').animate({ scrollTop: $(target).offset().top }, 1000);
        }
    },
});
});
