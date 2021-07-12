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
options.registry.o_animate = options.Class.extend({

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
