odoo.define('theme_graphene.editor', function (require) {
    'use strict';

    var Editor = require('web_editor.snippet.editor').Editor;
    var s_options = require('web_editor.snippets.options');

    // Typography
    s_options.registry.typo_style = s_options.Class.extend({
        select_class: function (type, value, $li) {
            this._super(type, value, $li);
            var $self = this.$target;

            if (value === "title-boxed" || value === "title-underlined") {
                // fix parent align
                $self.parent().addClass("title-parent");
                //trigg transition
                $self.addClass("o_animate").removeClass("o_visible").css('visibility', 'visible');
                setTimeout(function () {
                    $self.addClass("o_visible");
                }, 500);
            } else {
                $self.parent().removeClass("title-parent");
            }
        },
        clean_for_save: function () {
            this.$target.removeClass("o_visible");
        },
    });

    s_options.registry.no_resize = s_options.Class.extend({
        start: function () {
            self = this;
            setTimeout(function () {
                self.$overlay.find(".oe_handle_button.size").hide();
            }, 50);
        },
    });

    // Image background - Fix for mediablock
    s_options.registry.background.include({
        select_class: function (type, value, $li) {
            var self = this;
            this._super(type, value, $li);
            if (this.$target.hasClass("s_media_block")) {
                var objs = self.$target.find(".videoBox, > iframe, .yt_video_container");
                objs.stop(true,true)
                    .fadeOut(100)
                    .delay(600)
                    .fadeIn(2000);
            }
        },
    });

    // Background effects - Fix for mediablock
    s_options.registry.bg_fx = s_options.Class.extend({
        select_class: function (type, value, $li) {
            var self = this;
            this._super(type, value, $li);
            if (this.$target.hasClass("s_media_block")) {
                var objs = self.$target.find(".videoBox, > iframe, .yt_video_container");
                objs.stop(true,true)
                    .fadeOut(100)
                    .delay(600)
                    .fadeIn(2000);
            }
        },
    });

    Editor.include({
        _drag_and_drop_start: function () {
            this.$target.addClass("oe_snippet_body");
            return this._super.apply(this, arguments);
        },
        _drag_and_drop_stop: function () {
            this.$target.removeClass("oe_snippet_body");
            return this._super.apply(this, arguments);
        },
    });

    // Top Banner Options
    s_options.registry.graphene_top_banner_options = s_options.Class.extend({
        on_focus: function () {
            var self = this;
            if (self.$target.hasClass("move_to_top")) {
                self.$overlay
                    .find(".oe_overlay_options").css("margin-top","100px").end()
                    .find(".oe_snippet_clone, .oe_snippet_move").addClass("hidden");
            } else {
                self.$overlay
                    .find(".oe_snippet_clone, .oe_snippet_move").removeClass("hidden");
            }
            self.$overlay.on('click', '.oe_snippet_remove', _.bind(this.on_remove, this));
        },
        select_class: function (type, value, $li) {
            if (type !== "click") { return; }

            this._super(type, value, $li);
            var self = this;
            if (value === "move_to_top") {
                $(".move_to_top").removeClass("move_to_top");
                self.$target.addClass("move_to_top");
                $("#wrapwrap").addClass("top_content");
                $("#wrap").css("margin-top", (self.$target.outerHeight() * 0.9));

                $('html, body').animate({scrollTop:0}, 1000);

                self.on_focus();
            } else {
                self.$target.removeClass("move_to_top");
                $("#wrapwrap").removeClass("top_content");
                $("#wrap").css("margin-top", "");

                var offset = self.$target.offset.top;
                $('html, body').animate({scrollTop:(offset+100)}, 1000);
            }

            if (self.$target.hasClass("s_media_block")) {
                $(window).trigger("resize");
                self.$target.data('snippet-view').stop_video();
                self.$target.data('snippet-view').start_video();
            }
        },
        on_remove: function (event) {
            var self = this;
            if (self.$target.hasClass("move_to_top")) {
                $("#wrapwrap").removeClass("top_content");
                $("#wrap").css("margin-top","");
            }
        }
    });
});
