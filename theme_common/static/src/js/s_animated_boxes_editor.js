odoo.define('theme_common.s_animated_boxes_editor', function (require) {
    'use strict';

    var s_options = require('web_editor.snippets.options');

    s_options.registry.s_animated_boxes = s_options.Class.extend({
        start: function () {
            var self = this;
            self.add_btn_edit_slide();
            setTimeout(function () {
                if (self.$target.find(".slide").length > 0) {
                    self.$overlay.find(".createSlide").addClass("hide");
                    self.$overlay.find(".deleteSlide").removeClass("hide");
                    self.$overlay.find(".btn-showSlide").removeClass("hide");
                } else {
                    self.$overlay.find(".createSlide").removeClass("hide");
                    self.$overlay.find(".deleteSlide").addClass("hide");
                    self.$overlay.find(".btn-showSlide").addClass("hide");
                }
            }, 100);
        },

        add_btn_edit_slide: function () {
            var self = this;
            self.$overlay.find(".oe_options").after('<a href="#" class="btn btn-default btn-sm btn-showSlide" title="Lock slide" style="width: auto; padding: 0 5px;"><i class="fa fa-toggle-off"></i>  Edit Slide</a> ');
            self.$overlay.on('click', '.btn-showSlide', _.bind(this.toggle_slide, this));
        },

        create_slide: function (type, value, $li) {
            if (type !== 'click') return;
            var self = this,
                slide = '<div class="slide editable bg-success animated text-center dur-200ms insetShadow" anim="o_anim_fade_in_down" del="0" dur="200"><div class="v-align"><h3>Your new slide</h3></div></div>';
            self.$target.append(slide);
            self.$overlay.find(".btn-showSlide").removeClass("hide");
            self.$overlay.find(".createSlide").addClass("hide");
            self.$overlay.find(".deleteSlide").removeClass("hide");
        },

        delete_slide: function (type, value, $li) {
            if (type !== 'click') return;
            var self = this;
            self.$target.find(".slide").remove();
            self.$overlay.find(".btn-showSlide").addClass("hide");
            self.$overlay.find(".createSlide").removeClass("hide");
            self.$overlay.find(".deleteSlide").addClass("hide");
        },

        toggle_slide: function () {
            var a = this.$overlay.find(".btn-showSlide"),
                i = a.find("i"),
                t = this.$target,
                s = t.find(".slide");
            if (!t.hasClass("showSlide")) {
                t.addClass("showSlide"); i.addClass("fa-toggle-on").removeClass("fa-toggle-off"); i.css("color", "#FFF");
                s.addClass("visible");
            } else {
                t.removeClass("showSlide"); i.removeClass("fa-toggle-on").addClass("fa-toggle-off"); i.css("color", "");
                s.removeClass("visible");
            }
        },
        on_focus: function () {
            this._adapt_items_height();
        },
        on_blur: function () {
            this._adapt_items_height();
        },
        clean_for_save: function() {
            this.$target.removeClass("showSlide")
                        .find(".slide").removeClass("visible");

            this._adapt_items_height();
        },
        _adapt_items_height: function () {
            var $items = this.$target.closest(".s_animated_boxes").find(".item");
            var min_height = _.reduce($items.find(".v-align"), function (memo, item) {
                return Math.max(memo, $(item).outerHeight(true) + 40);
            }, 200);
            $items.css("height", min_height);
        },
    });
});
