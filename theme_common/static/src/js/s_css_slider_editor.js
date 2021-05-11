odoo.define('theme_common.s_css_slider_editor', function (require) {
    'use strict';

    var s_options = require('web_editor.snippets.options');

    s_options.registry.marginAndResize.include({
        start: function () {
            this._super();
            var self = this;
            self.$overlay.find(".oe_handle.size .size").on('mouseup', function (event) {
                event.preventDefault();
                if (self.$target.hasClass("s_css_slider")) {
                    setTimeout(function () {
                        self.$target.data('snippet-view').resizeImgs(self.$target);
                    });
                }
            });
        },
    });

    s_options.registry.s_css_slider_slide = s_options.Class.extend({
        newSlideUrl: "/web/image/theme_common.image_content_23",

        start: function () {
            var self = this;

            self.reset();
            self.$target.data('snippet-view').start(true);

            setTimeout(function () {
                self.$overlay.find(".js_s_css_slider_addSlide").on('click', function () { self.addSlide(); });
                self.$overlay.find(".js_s_css_slider_removeSlide").on('click', function () { self.removeSlide(); });
            }, 100);

            $(document.body).on("media-saved", function () {
                self.resizeImgsEditor();
            });
        },

        resizeImgsEditor: function () {
            var self = this;
            setTimeout(function () {
                self.$target.data('snippet-view').resizeImgs(self.$target);
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
            var pagination = self.$target.find(".s_css_slider_pagination");
            $currentSlide.clone().insertAfter($currentSlide).removeClass("selected");

            _.defer(function () {
                self.reset();
                self.$target.data('snippet-view').start(true);
                self.$target.data('snippet-view').nextSlide(self.$target, pagination);
            });
        },

        removeSlide: function () {
            var self = this;
            var $currentSlide = self.$target.find(".slider .slide.selected");
            var pagination = self.$target.find(".s_css_slider_pagination");

            self.$target.data('snippet-view').prevSlide(self.$target, pagination);
            $currentSlide.remove();
            _.defer(function () {
                self.reset();
                self.$target.data('snippet-view').start(true);
            });
        },

        clean_for_save: function () {
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
