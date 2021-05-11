odoo.define('theme_common.s_showcase_slider_editor.js', function (require) {
    'use strict';

    var s_options = require('web_editor.snippets.options');
    var s_animation = require("web_editor.snippets.animation");
    require("theme_common.s_showcase_slider_frontend");

    s_options.registry.s_showcase_slider = s_options.Class.extend({
        start: function () {
            this._super.apply(this, arguments);

            if (!this.$target.data("snippet-view")) {
                this.$target.data("snippet-view", new s_animation.registry.s_showcase_slider(this.$target, true));
            }

            this.$target.on("transitionIsFinished", (function () {
                this.buildingBlock.make_active(this.$target);
            }).bind(this));

            _.delay((function () { // FIXME ...
                this.$overlay.find(".js_s_ss_addSlide").on('click', this.addSlide.bind(this));
                this.$overlay.find(".js_s_ss_removeSlide").on('click', this.removeSlide.bind(this));
            }).bind(this), 100);
        },

        resetSlides: function (active) {
            this.$target.data('snippet-view').stop();
            this.$target.data('snippet-view').start();
            this.$target.toggleClass("active", !!active);
        },

        addSlide: function () {
            var $currentSlide = this.$target.find(".s_ss_slider > .selected");
            $currentSlide.after("<li><img class=\"o_not-animable\" src=\"/web/image/theme_common.image_content_23\"/></li>");
            this.resetSlides(true);
            this.$target.data('snippet-view').nextSlide();
        },

        removeSlide: function () {
            if (this.$target.find(".s_ss_slider").children().length <= 1) return;

            var $currentSlide = this.$target.find(".s_ss_slider > .selected");
            this.$target.data('snippet-view').prevSlide();
            $currentSlide.remove();
            this.resetSlides(true);
        },

        clean_for_save: function () {
            this._super.apply(this, arguments);
            this.$target.data('snippet-view').stop();
        },
    });
});
