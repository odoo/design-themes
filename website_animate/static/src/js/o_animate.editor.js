odoo.define('website_animate.o_animate_editor', function (require) {
'use strict';

const options = require('web_editor.snippets.options');

options.registry.o_animate = options.Class.extend({

    //--------------------------------------------------------------------------
    // Options
    //--------------------------------------------------------------------------

    /**
     * @override
     */
    async selectClass(previewMode, widgetValue, params) {
        await this._super(...arguments);
        this._forceAnimation();
        if (params.isAnimationTypeSelection) {
            this.$target.toggleClass('o_animate', !!widgetValue);
        }
    },

    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * @private
     */
    _forceAnimation() {
        this.$target.css('animation-name', 'dummy');
        // trigger a DOM reflow
        void this.$target[0].offsetWidth;
        this.$target.css('animation-name', '');
    },
});
});
