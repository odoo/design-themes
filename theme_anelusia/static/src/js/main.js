odoo.define('theme_anelusia.main', function (require) {
'use strict';

var publicWidget = require('web.public.widget');
require('website.content.menu');

// FIXME

publicWidget.registry.anelusiaHeader = publicWidget.Widget.extend({
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

publicWidget.registry.affixMenu.include({
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
    // Private
    //--------------------------------------------------------------------------

    /**
     * @override
     */
    _getHeaderHeight: function () {
        return Math.max(
            this.$headerClone.find('.navbar-brand').outerHeight(true),
            this.$headerClone.find('.container').outerHeight(true)
        );
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
