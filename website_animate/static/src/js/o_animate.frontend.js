/** @odoo-module **/

import publicWidget from 'web.public.widget';

publicWidget.registry.WebsiteAnimate = publicWidget.Widget.extend({
    selector: '#wrapwrap',
    disabledInEditableMode: false,

    offsetRatio: 0.3, // Dynamic offset ratio: 0.3 = (element's height/3)
    offsetMin: 10, // Minimum offset for small elements (in pixels)

    /**
     * @override
     */
    start() {
        this.lastScroll = 0;
        this.$scrollingElement = $().getScrollingElement(this.ownerDocument);
        // By default, elements are hidden by the css of o_animate.
        // Render elements and trigger the animation then pause it in state 0.
        this.$animatedElements = this.$target.find('.o_animate');
        _.each(this.$animatedElements, el => {
            this._resetAnimation($(el));
        });
        // Then we render all the elements, the ones which are invisible
        // in state 0 (like fade_in for example) will stay invisible.
        this.$animatedElements.css("visibility", "visible");

        // We use addEventListener instead of jQuery because we need 'capture'.
        // Setting capture to true allows to take advantage of event bubbling
        // for events that otherwise don’t support it. (e.g. useful when
        // scrolling a modal)
        this.__onScrollWebsiteAnimate = _.throttle(this._onScrollWebsiteAnimate.bind(this), 200);
        this.$scrollingElement[0].addEventListener('scroll', this.__onScrollWebsiteAnimate, {capture: true});

        $(window).on('resize.o_animate, shown.bs.modal.o_animate, slid.bs.carousel.o_animate', () => {
            this.windowsHeight = $(window).height();
            this.$scrollingElement[0].dispatchEvent(new Event('scroll'));
        }).trigger("resize");

        return this._super(...arguments);
    },
    /**
     * @override
     */
    destroy() {
        this._super(...arguments);
        this.$target.find('.o_animate')
            .removeClass('o_animating o_animated o_animate_preview')
            .css({
                'animation-name': '',
                'animation-play-state': '',
                'visibility': '',
            });
        $(window).off('.o_animate');
        this.$scrollingElement[0].removeEventListener('scroll', this.__onScrollWebsiteAnimate, {capture: true});
        this.$scrollingElement[0].classList.remove('o_wanim_overflow_x_hidden');
    },

    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * Starts animation and/or update element's state.
     * 
     * @private
     * @param {jQuery} $el
     */
    _startAnimation($el) {
        // Forces the browser to redraw using setTimeout.
        setTimeout(() => {
            this._toggleOverflowXHidden(true);
            $el
            .css({"animation-play-state": "running"})
            .addClass("o_animating")
            .one('webkitAnimationEnd oanimationend msAnimationEnd animationend', () => {
                $el.addClass("o_animated").removeClass("o_animating");
                this._toggleOverflowXHidden(false);
                $(window).trigger("resize");
            });
        });
    },
    /**
     * @private
     * @param {jQuery} $el
     */
    _resetAnimation($el) {
        const animationName = $el.css("animation-name");
        $el.css({"animation-name": "dummy-none", "animation-play-state": ""})
           .removeClass("o_animated o_animating");

        this._toggleOverflowXHidden(false);
        // trigger a DOM reflow
        void $el[0].offsetWidth;
        $el.css({'animation-name': animationName , 'animation-play-state': 'paused'});
    },
    /**
     * Shows/hides the horizontal scrollbar (on the #wrapwrap).
     * 
     * @private
     * @param {Boolean} add
     */
    _toggleOverflowXHidden(add) {
        if (add) {
            this.$scrollingElement[0].classList.add('o_wanim_overflow_x_hidden');
        } else if (!this.$scrollingElement.find('.o_animating').length) {
            this.$scrollingElement[0].classList.remove('o_wanim_overflow_x_hidden');
        }
    },
    /**
     * Gets element top offset by not taking CSS transforms into calculations.
     * 
     * @private
     * @param {Element} el
     */
    _getElementOffsetTop(el) {
        // Loop through the DOM tree and add its parent's offset to get page offset.
        var top = 0;
        do {
            top += el.offsetTop || 0;
            el = el.offsetParent;
        } while (el);
        return top;
    },

    //--------------------------------------------------------------------------
    // Handlers
    //--------------------------------------------------------------------------

    /**
     * @private
     * @param {Event} ev
     */
    _onScrollWebsiteAnimate(ev) {
        const scroll = $(ev.currentTarget).scrollTop();
        // Handle reverse scrolling
        const direction = (scroll < this.lastScroll) ? -1 : 1;
        this.lastScroll = scroll;

        _.each(this.$target.find('.o_animate'), el => {
            const $el = $(el);
            const elHeight = $el.height();
            const elOffset = direction * Math.max((elHeight * this.offsetRatio), this.offsetMin);
            const state = $el.css("animation-play-state");

            // We need to offset for the change in position from some animation.
            // So we get the top value by not taking CSS transforms into calculations.
            const $openModal = this.$target.find('.modal:visible');
            const scrollTop = $openModal.length ? $openModal.scrollTop() : this.$scrollingElement.scrollTop();
            const elTop = this._getElementOffsetTop($el[0]) - scrollTop;

            const visible = this.windowsHeight > (elTop + elOffset) && 0 < (elTop + elHeight - elOffset);
            if (visible && state === "paused") {
                $el.addClass("o_visible");
                this._startAnimation($el);
            } else if (!visible && $el.hasClass("o_animate_both_scroll") && state === "running") {
                $el.removeClass("o_visible");
                this._resetAnimation($el);
            }
        });
    },
});
