odoo.define('theme_treehouse.animation', function (require) {
'use strict';

var sAnimation = require('website.content.snippets.animation');
require('website.content.menu');

sAnimation.registry.backToTop = sAnimation.Class.extend({
    selector: '#copyright .top',
    events: {
        'click': '_onClick',
    },

    //--------------------------------------------------------------------------
    // Handlers
    //--------------------------------------------------------------------------

    /**
     * @private
     * @param {Event} ev
     */
    _onClick: function (ev) {
        ev.preventDefault();
        $('html, body').animate({scrollTop : 0}, 800);
    },
});

sAnimation.registry.dropdownSlide = sAnimation.Class.extend({
    selector: '.dropdown, .btn-group',
    events: {
        'hide.bs.dropdown': '_onHide',
        'show.bs.dropdown': '_onShow',
    },

    //--------------------------------------------------------------------------
    // Handlers
    //--------------------------------------------------------------------------

    /**
     * @private
     * @param {Event} ev
     */
    _onHide: function (ev) {
        ev.preventDefault();
        var self = this;
        this.$('.dropdown-menu').first().stop(true, true).slideUp('', function () {
            self.$target.removeClass('open');
        });
    },
    /**
     * @private
     */
    _onShow: function () {
        this.$('.dropdown-menu').first().stop(true, true).slideDown();
    },
});

sAnimation.registry.affixMenu.include({
    /**
     * @override
     */
    start: function () {
        var def = this._super.apply(this, arguments);
        if (this.$headerClone) {
            this.$headerClone.find('#preheader').remove();
        }
        return def;
    },
});
});
