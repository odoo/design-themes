odoo.define('theme_treehouse.animation', function (require) {
'use strict';

var publicWidget = require('web.public.widget');
require('website.content.menu');

publicWidget.registry.outlineButtonOnHover = publicWidget.Widget.extend({
    selector: '#wrapwrap',
    events: {
        'mouseenter .btn:not([class*="btn-outline-"])': '_onMouseEnter',
        'mouseleave .btn': '_onMouseLeave',
    },
    compat: {
        'success': 'beta',
        'info': 'gamma',
        'warning': 'delta',
        'danger': 'epsilon',
    },

    //--------------------------------------------------------------------------
    // Handlers
    //--------------------------------------------------------------------------

    /**
     * Called when a button is hovered -> add outline style.
     *
     * @private
     * @param {Event} ev
     */
    _onMouseEnter: function (ev) {
        var self = this;
        var $btn = $(ev.currentTarget);
        $btn.addClass('bg-transparent');
        _.each(['primary', 'secondary', 'alpha', 'beta', 'gamma', 'delta', 'epsilon', 'success', 'info', 'warning', 'danger'], function (color) {
            if ($btn.hasClass('btn-' + color)) {
                $btn.removeClass('btn-' + color);
                $btn.addClass('btn-outline-' + (self.compat[color] || color) + ' text-' + (self.compat[color] || color));
                $btn.data('outlineButtonOnHover:color', color);
            }
        });
    },
    /**
     * Called when a button is hovered -> add outline style.
     *
     * @private
     * @param {Event} ev
     */
    _onMouseLeave: function (ev) {
        var $btn = $(ev.currentTarget);
        $btn.removeClass('bg-transparent');
        var color = $btn.data('outlineButtonOnHover:color');
        if (!color) {
            return;
        }
        $btn.removeClass('btn-outline-' + (this.compat[color] || color) + ' text-' + (this.compat[color] || color));
        $btn.addClass('btn-' + color);
    },
});

publicWidget.registry.backToTop = publicWidget.Widget.extend({
    selector: '.o_footer_copyright .top',
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

publicWidget.registry.dropdownSlide = publicWidget.Widget.extend({
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
        var $menu = this.$('.dropdown-menu');
        $menu.stop(true, true).slideUp('', function () {
            self.$target.removeClass('show');
            $menu.removeClass('show');
        });
    },
    /**
     * @private
     */
    _onShow: function () {
        this.$('.dropdown-menu').first().stop(true, true).slideDown();
    },
});

publicWidget.registry.affixMenu.include({
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
