odoo.define('theme_avantgarde.frontend', function (require) {
    'use strict';

    var publicWidget = require('web.public.widget');

    publicWidget.registry.AvantgardeUtils = publicWidget.Widget.extend({
        selector: '#wrapwrap',
        disabledInEditableMode: false,

        /**
         * @override
         */
        start: function () {
            this.$('.o_header_affix').removeAttr('id');

            this.$('.v-align').filter(function () {
                return $(this).parent().is(":not(.slide)");
            }).addClass("preserve3d");

            return this._super.apply(this, arguments);
        },
    });

    /**
     * Avantgarde has an extended version of the moveToTop option: it can work
     * on dynamic website pages (/shop, /blog, ...). It is also automatic for
     * "full" blog covers. The style is also different as the top content is
     * full width and goes below the #wrap element (even if that one is not fw).
     */
    publicWidget.registry.move_to_top = publicWidget.Widget.extend({
        selector: '.move_to_top, #title.blog_header > .cover.cover_full',

        /**
         * @override
         */
        start: function () {
            var self = this;
            var def = this._super.apply(this, arguments);
            $('#wrapwrap').addClass('o_header_overlay');
            $(window).on('resize.move_to_top', _.debounce(function () {
                if (self.isDestroyed()) {
                    // May happen since this is debounced
                    return;
                }
                self._adaptWrap();
            }, 250));
            setTimeout(function () {
                self._adaptWrap();
            }, 250);
            return def;
        },
        /**
         * @override
         */
        destroy: function () {
            this._super.apply(this, arguments);
            $('#wrapwrap').removeClass('o_header_overlay');
            $(window).off('.move_to_top');
            $('#wrap').css('margin-top', '');
        },

        //----------------------------------------------------------------------
        // Private
        //----------------------------------------------------------------------

        /**
         * @private
         */
        _adaptWrap: function () {
            $('#wrap').css('margin-top', this.$target.outerHeight());
        },
    });

    // Ripple animation
    publicWidget.registry.avant_links = publicWidget.Widget.extend({
        selector: ".btn, .dropdown-item",

        start: function () {
            var btn = this.$target;

            btn
            .css({ position: 'relative', overflow: 'hidden'})
            .bind('mousedown', function (e) {
                var ripple;
                if (btn.find('.avant-ripple').length === 0) {
                    ripple = $('<span class="avant-ripple"/>');
                    btn.prepend(ripple);
                } else {
                    ripple = btn.find('.avant-ripple');
                }
                ripple.removeClass('avant-ripple-animated');

                if (!ripple.height() && !ripple.width()) {
                    var diameter = Math.max(btn.outerWidth(), btn.outerHeight());
                    ripple.css({ height: diameter, width: diameter });
                }

                var x = e.pageX - btn.offset().left - ripple.width() / 2;
                var y = e.pageY - btn.offset().top - ripple.height() / 2;

                ripple
                    .css({ top: y + 'px',left: x + 'px'})
                    .addClass('avant-ripple-animated');

                setTimeout(function () {
                    ripple.removeClass('avant-ripple-animated');
                }, 351);
            });

            return this._super.apply(this, arguments);
        },
    });
});
