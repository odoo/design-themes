odoo.define('theme_common.s_showcase_slider_editor.js', function (require) {
    'use strict';

    var s_options = require('web_editor.snippets.options');
    require("theme_common.s_showcase_slider_frontend");

    s_options.registry.s_showcase_slider = s_options.Class.extend({
        start: function () {
            this._super.apply(this, arguments);

            this.$target.on("transitionIsFinished", (function () {
                this.trigger_up('cover_update');
            }).bind(this));

            _.delay((function () { // FIXME ...
                this.$overlay.find(".js_s_ss_addSlide").on('click', this.addSlide.bind(this));
                this.$overlay.find(".js_s_ss_removeSlide").on('click', this.removeSlide.bind(this));
            }).bind(this), 100);
        },

        resetSlides: function (active) {
            this.trigger_up('animation_start_demand', {
                editableMode: true,
                $target: this.$target,
            });
            this.$target.toggleClass("active", !!active);
        },

        addSlide: function () {
            var $currentSlide = this.$target.find(".s_ss_slider > .selected");
            $currentSlide.after("<li><img class=\"o_not-animable\" src=\"/web/image/theme_common.image_content_23\"/></li>");
            this.resetSlides(true);
        },

        removeSlide: function () {
            if (this.$target.find(".s_ss_slider").children().length <= 1) return;

            var $currentSlide = this.$target.find(".s_ss_slider > .selected");
            $currentSlide.remove();
            this.resetSlides(true);
        },
    });
});
