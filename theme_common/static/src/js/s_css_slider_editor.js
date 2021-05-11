odoo.define('theme_common.s_css_slider_editor', function (require) {
    'use strict';

    var s_options = require('web_editor.snippets.options');

    s_options.registry.s_css_slider_slide = s_options.Class.extend({
        newSlideUrl: "/web/image/theme_common.image_content_23",

        start: function () {
            var self = this;

            self.reset();
            this.trigger_up('widgets_start_request', {
                editableMode: true,
                $target: this.$target,
            });

            setTimeout(function () {
                self.$overlay.data('$optionsSection').find(".js_s_css_slider_addSlide").on('click', function () { self.addSlide(); });
                self.$overlay.data('$optionsSection').find(".js_s_css_slider_removeSlide").on('click', function () { self.removeSlide(); });
            }, 100);

            $(document.body).on("media-saved", function () {
                self.resizeImgsEditor();
            });
        },

        resizeImgsEditor: function () {
            var self = this;
            setTimeout(function () {
                self.trigger_up('widgets_start_request', {
                    editableMode: true,
                    $target: self.$target,
                });
            });
        },

        reset: function () {
            var self= this;
            self.$target.find(".s_css_slider_pagination").remove().end()
                .find("span").unbind("click.s_css");
        },

        addSlide: function () {
            var self = this;
            var $currentSlide = self.$target.find(".slider .slide.selected");
            $currentSlide.clone().insertAfter($currentSlide).removeClass("selected");

            _.defer(function () {
                self.reset();
                self.trigger_up('widgets_start_request', {
                    editableMode: true,
                    $target: self.$target,
                });
            });
        },

        removeSlide: function () {
            var self = this;
            var $currentSlide = self.$target.find(".slider .slide.selected");

            $currentSlide.remove();
            _.defer(function () {
                self.reset();
                self.trigger_up('widgets_start_request', {
                    editableMode: true,
                    $target: self.$target,
                });
            });
        },

        cleanForSave: function () {
            var self = this;
            self.$target
                .find(".s_css_slider_pagination").remove().end()
                .find(".navigation .prev").addClass("inactive").end()
                .find(".navigation .next").removeClass("inactive").end()
                .find(".slider .slide").removeClass("selected move-left").end()
                .find(".slider .slide").first().addClass("selected");
        },
    });
});
