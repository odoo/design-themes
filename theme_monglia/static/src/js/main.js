odoo.define('theme_monglia.main', function (require) {
'use strict';

var sAnimations = require('website.content.snippets.animation');

sAnimations.registry.MenuSlideOpen = sAnimations.Class.extend({
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
