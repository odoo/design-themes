odoo.define('website_animate.o_animate_frontend', function (require) {
'use strict';

const publicWidget = require('web.public.widget');

const BaseWebsiteAnimate = publicWidget.Widget.extend({

    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * @private
     */
    _reset_animation($el) {
        const animationName = $el.css("animation-name");
        $el.css({"animation-name": "dummy-none", "animation-play-state": ""})
           .removeClass("o_animated o_animating");
        // trigger a DOM reflow
        void $el[0].offsetWidth;
        $el.css({'animation-name': animationName , 'animation-play-state': 'paused'});
    },
});

publicWidget.registry.WebsiteAnimate = BaseWebsiteAnimate.extend({
    selector: '.o_animate',
    disabledInEditableMode: false,

    /**
     * @override
     */
    start() {
        // By default, elements are hidden by the css of o_animate.
        // render elements  + // We will trigger the animation then pause it in state 0.
        console.log(this.$target[0]);
        debugger;
        this._reset_animation(this.$target);
        // Then we render all the elements, the ones which are invisible
        // in state 0 (like fade_in for example) will stay invisible.
        this.$target.css("visibility", "visible");

        return this._super(...arguments);
    },

    /**
     * @override
     */
    destroy() {
        // Clean elements
        console.log("DESTROY");
        this.$target.removeClass('o_animating o_animated o_visible')
                    .css({
                        'animation': '',
                        'animation-name': '',
                        'animation-play-state': '',
                        'visibility': '',
                    });
    },
});

publicWidget.registry.WebsiteAnimateWrapwrap = BaseWebsiteAnimate.extend({
    selector: '#wrapwrap',
    disabledInEditableMode: false,

    offsetRatio: 0.3, // Dynamic offset ratio: 0.3 = (element's height/3)
    offsetMin: 10, // Minimum offset for small elements (in pixels)

    /**
     * @override
     */
    start() {
        setTimeout(() => {
            this.attach_handlers();
        });

        return this._super(...arguments);
    },

    //--------------------------------------------------------------------------
    // Public
    //--------------------------------------------------------------------------

    // Bind events and define the scrolling function
    attach_handlers() {
        let lastScroll = 0;

        $(window)
        .on('resize.o_animate', () => {
            this.windowsHeight = $(window).height();
            $().getScrollingElement().trigger("scroll");
        })
        .trigger("resize");

        $().getScrollingElement()
        .on("scroll.o_animate, slid.bs.carousel", _.throttle(() => {
            // _.throttle -> Limit the number of times the scroll function
            // can be called in a given period. (http://underscorejs.org/#throttle)
            const windowTop = $(window).scrollTop();
            const windowBottom = windowTop + this.windowsHeight;

            // Handle reverse scrolling
            const direction = (windowTop < lastScroll) ? -1 : 1;
            lastScroll = windowTop;
            console.log("scroll");

            _.each(this.$target.find(".o_animate"), el => {
                const $el = $(el);
                const elHeight = $el.height();
                const elOffset = direction * Math.max((elHeight * this.offsetRatio), this.offsetMin);
                const state = $el.css("animation-play-state");

                // We need to offset for the change in position from some animation
                // So we get the top value of the transform matrix
                const transformMatrix = $el.css('transform').replace(/[^0-9\-.,]/g, '').split(',');
                const transformOffset = transformMatrix[13] || transformMatrix[5];
                const elTop = $el.offset().top - transformOffset;

                const visible = windowBottom > (elTop + elOffset) && windowTop < (elTop + elHeight - elOffset);
                if (visible && (state === "paused")) {
                    $el.addClass("o_visible");
                    this.start_animation($el);
                } else if (!(visible) && $el.hasClass("o_animate_both_scroll") && (state === "running")) {
                    $el.removeClass("o_visible");
                    this._reset_animation($el);
                }
            });
        }, 100))
        .trigger('scroll');
    },

    // Start animation and/or update element's state
    start_animation($el) {
        // force the browser to redraw using setTimeout
        setTimeout(() => {
            $el
            .css({"animation-play-state": "running"})
            .addClass("o_animating")
            .one('webkitAnimationEnd oanimationend msAnimationEnd animationend', function (e) {
                $el.addClass("o_animated").removeClass("o_animating");
                $(window).trigger("resize");
            });
        });
    },
});

// Backward compatibility for enark animation system
publicWidget.registry.o_animate = publicWidget.Widget.extend({
    selector: '.o_animation',

    destroy() {
        this._super(...arguments);

        // Convert old classes to the new animation system
        const oldAnimationClasses = "o_animation o_displayed o_displayed_top o_displayed_middle o_displayed_bottom o_visible o_visible_top o_visible_middle o_visible_bottom";
        $(".o_fade_in").addClass("o_animate o_anim_fade_in").removeClass("o_fade_in");
        $(".o_fade_in_down").addClass("o_animate o_anim_fade_in_down").removeClass("o_fade_in_down");
        $(".o_fade_in_left").addClass("o_animate o_anim_fade_in_left").removeClass("o_fade_in_left");
        $(".o_fade_in_right").addClass("o_animate o_anim_fade_in_right").removeClass("o_fade_in_right");
        $(".o_fade_in_up").addClass("o_animate o_anim_fade_in_up").removeClass("o_fade_in_up");
        this.$target.removeClass(oldAnimationClasses);
    },
});
});
