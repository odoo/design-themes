odoo.define('theme_common.s_showcase_slider_editor.js', function (require) {
    'use strict';

    var s_options = require('web_editor.snippets.options');

    s_options.registry.s_showcase_slider = s_options.Class.extend({
        start: function () {
            this._super();
            var self = this;

            self.reset();

            self.$target.find("span").bind("click.s_ss_editor", function () {
                $('body,html').animate({'scrollTop':self.$target.offset().top - 70}, 0);
            })

            setTimeout(function () {
                self.$overlay.find(".js_s_ss_addSlide").on('click', function ()    { self.addSlide(); return false; });
                self.$overlay.find(".js_s_ss_removeSlide").on('click', function () { self.removeSlide(); return false; });
            },100)
        },

        reset: function () {
            var self= this;
            self.$target.find(".s_ss_slider_pagination").remove().end()
                .find("span, .s_ss_slider").unbind("click.s_ss");
            self.$target.data('snippet-view').start();
        },

        addSlide: function () {
            var self = this;
            var $currentSlide = self.$target.find(".s_ss_slider li.selected");
            var pagination = self.$target.find(".s_ss_slider_pagination");
            var $newSlide = $('<li><img class="o_not-animable" src="/web/image/theme_common.image_content_23" /></li>');

            $currentSlide.after($newSlide);
            self.reset();
            self.$target.data('snippet-view').start();
            self.$target.data('snippet-view').nextSlide(self.$target, pagination);
        },

        removeSlide: function () {
            var self = this;
            var $currentSlide = self.$target.find(".s_ss_slider li.selected");
            var pagination = self.$target.find(".s_ss_slider_pagination");

            self.$target.data('snippet-view').prevSlide(self.$target, pagination);
            $currentSlide.remove();
            self.reset();
        },

        clean_for_save: function () {
            this.$target.removeClass('active')
        },
    });
});
