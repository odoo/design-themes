odoo.define('website_animate.o_animate_editor', function (require) {
'use strict';

var sOptions = require('web_editor.snippets.options');

function forceAnimation() {
    var $els = $();
    _.each(arguments, function (el) {
        $els = $els.add(el);
    });
    $els.css('animation-name', 'dummy');
    void $els[0].offsetWidth;
    $els.css('animation-name', '');
}

//  Animations
sOptions.registry.o_animate = sOptions.Class.extend({
    /**
     * @override
     */
    cleanForSave: function () {
        // Clean elements
        this.$target.removeClass('o_animating o_animated o_animate_preview')
                    .css({
                        'animation-name': '',
                        'animation-play-state': '',
                        'visibility': '',
                    });
        if (this.$target.hasClass('o_animate')) {
            this.$target.css('animation-play-state', 'paused');
        }

        // Clean all inView elements
        $('#wrapwrap').find('.o_animate').removeClass('o_visible');
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
