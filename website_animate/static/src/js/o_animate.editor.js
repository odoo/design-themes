odoo.define('website_animate.o_animate_editor', function (require) {
'use strict';

var sOptions = require('web_editor.snippets.options');

function forceAnimation() {
    var $els = $();
    const $scrollingElement = $().getScrollingElement();
    _.each(arguments, function (el) {
        $els = $els.add(el);
    });
    $els.css('animation-name', 'dummy');
    void $els[0].offsetWidth;
    $els.addClass('o_animating');
    $scrollingElement[0].classList.add('o_wanim_overflow_x_hidden');
    $els.css('animation-name', '');
    $els.one('webkitAnimationEnd oanimationend msAnimationEnd animationend', function (e) {
        $scrollingElement[0].classList.remove('o_wanim_overflow_x_hidden');
        $els.removeClass('o_animating');
    });
}

//  Animations
sOptions.registry.o_animate = sOptions.Class.extend({
    /**
     * @override
     */
    async onBuilt() {
        this.$target[0].classList.toggle('o_animate_preview', this.$target[0].classList.contains('o_animate'));
    },

    //--------------------------------------------------------------------------
    // Options
    //--------------------------------------------------------------------------

    /**
     * @override
     */
    selectClass: async function (previewMode, widgetValue, params) {
        await this._super.apply(this, arguments);
        forceAnimation(this.$target);
        if (params.isAnimationTypeSelection) {
            this.$target.toggleClass('o_animate_preview o_animate', !!widgetValue);
        }
    },
});
});
