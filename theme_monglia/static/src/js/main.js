odoo.define('theme_monglia.main', function (require) {
'use strict';

var publicWidget = require('web.public.widget');

publicWidget.registry.MenuSlideOpen = publicWidget.Widget.extend({
    selector: '#wrapwrap',
    events: {
        'click #menuToggle, .menu-close': '_onClickToggle',
        'click main, footer': '_onClickOutside',
    },

    //--------------------------------------------------------------------------
    // Handlers
    //--------------------------------------------------------------------------

    /**
     * @private
     */
    _onClickToggle: function (ev) {
        ev.stopPropagation();
        $(document.body).toggleClass('o_bigslide_open');
    },
    /**
     * @private
     */
    _onClickOutside: function () {
        $(document.body).removeClass('o_bigslide_open');
    },
});
});
