odoo.define('theme_anelusia.main', function (require) {
'use strict';

var sAnimation = require('website.content.snippets.animation');
require('website.content.menu');

// FIXME

sAnimation.registry.anelusiaHeader = sAnimation.Class.extend({
    selector: '.navbar-toggler',
    events: {
        'click': '_onToggleClick',
    },

    //--------------------------------------------------------------------------
    // Handlers
    //--------------------------------------------------------------------------

    /**
     * @private
     */
    _onToggleClick: function () {
        $('body').toggleClass('no-scroll');
        setTimeout(function () { $(window).trigger('scroll'); }, 100);
    },
});

sAnimation.registry.affixMenu.include({
    /**
     * @override
     */
    start: function () {
        var def = this._super.apply(this, arguments);
        if (this.$headerClone) {
            this.$clonedNavbarHeader = this.$headerClone.find('.navbar-toggler');
        }
        return def;
    },

    //--------------------------------------------------------------------------
    // Handlers
    //--------------------------------------------------------------------------

    /**
     * @override
     */
    _onWindowUpdate: function () {
        this._super.apply(this, arguments);

        var affixed = this.$headerClone.is('.affixed');
        var noScroll = $('body').hasClass('no-scroll');
        var hasHamburgerMenu = ($(".new-toggle").length > 0);
        this.$clonedNavbarHeader.css('background', (affixed && !noScroll && hasHamburgerMenu) ? 'rgba(0, 0, 0, 0.8)' : 'none');
    },
});
});
