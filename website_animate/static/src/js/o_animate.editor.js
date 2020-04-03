/** @odoo-module **/

import options from 'web_editor.snippets.options';

options.registry.WebsiteAnimate = options.Class.extend({

    //--------------------------------------------------------------------------
    // Options
    //--------------------------------------------------------------------------

    /**
     * @override
     */
    async selectClass(previewMode, widgetValue, params) {
        await this._super(...arguments);
        if (params.isAnimationTypeSelection) {
            this._forceAnimation();
            this.$target.toggleClass('o_animate_preview o_animate', !!widgetValue);
        }
    },

    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * @private
     */
    _forceAnimation() {
        const $scrollingElement = $().getScrollingElement();
        this.$target.css('animation-name', 'dummy');
        // Trigger a DOM reflow.
        void this.$target[0].offsetWidth;
        this.$target.addClass('o_animating');
        $scrollingElement[0].classList.add('o_wanim_overflow_x_hidden');
        this.$target.css('animation-name', '');
        this.$target.one('webkitAnimationEnd oanimationend msAnimationEnd animationend', () => {
            $scrollingElement[0].classList.remove('o_wanim_overflow_x_hidden');
            this.$target.removeClass('o_animating');
        });
    },
});
