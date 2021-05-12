odoo.define('theme_graphene.editor', function (require) {
    'use strict';

    var Editor = require('web_editor.snippet.editor').Editor;
    var s_options = require('web_editor.snippets.options');

    // Typography
    s_options.registry.typo_style = s_options.Class.extend({
        selectClass: function (previewMode, value, $li) {
            this._super(previewMode, value, $li);
            var self = this;
            var hasWrapper = this.$target.parent().is('.s_typo_style_wrapper');

            if (value === 'title-boxed' || value === 'title-underlined') {
                if (!hasWrapper) {
                    this.$target.wrap('<div class="title-parent s_typo_style_wrapper"/>');
                }

                //trigg transition
                this.$target.addClass('o_animate o_hold').removeClass('o_visible').css('visibility', 'visible');
                _.defer(function () {
                    self.$target.addClass('o_visible').removeClass('o_hold');
                });
            } else {
                this.$target.removeClass('o_animate o_hold');
                if (hasWrapper) {
                    this.$target.unwrap();
                } else {
                    // Compatibility (before the title-parent class was not put
                    // on a wrapper but on the existing parent)
                    this.$target.parent().removeClass('title-parent');
                }
            }
        },
        cleanForSave: function () {
            this.$target.removeClass("o_visible");
        },
    });

    // Image background - Fix for mediablock
    s_options.registry.background.include({
        selectClass: function (previewMode, value, $li) {
            var self = this;
            this._super(previewMode, value, $li);
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
        selectClass: function (previewMode, value, $li) {
            var self = this;
            this._super(previewMode, value, $li);
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
        _onDragAndDropStart: function () {
            this.$target.addClass("oe_snippet_body");
            return this._super.apply(this, arguments);
        },
        _onDragAndDropStop: function () {
            this.$target.removeClass("oe_snippet_body");
            return this._super.apply(this, arguments);
        },
    });

    // Top Banner Options
    s_options.registry.graphene_top_banner_options = s_options.Class.extend({
        onFocus: function () {
            var self = this;
            if (self.$target.hasClass("move_to_top")) {
                self.$overlay
                    .find(".oe_overlay_options").css("margin-top","100px").end()
                    .find(".oe_snippet_clone, .oe_snippet_move").addClass("hidden");
            } else {
                self.$overlay
                    .find(".oe_snippet_clone, .oe_snippet_move").removeClass("hidden");
            }
            self.$overlay.on('click', '.oe_snippet_remove', _.bind(this.onRemove, this));
        },
        selectClass: function (previewMode, value, $li) {
            this._super(previewMode, value, $li);
            var self = this;
            if (value === "move_to_top") {
                $(".move_to_top").removeClass("move_to_top");
                self.$target.addClass("move_to_top");
                $("#wrapwrap").addClass("top_content");
                $("#wrap").css("margin-top", (self.$target.outerHeight() * 0.9));

                $('html, body').animate({scrollTop:0}, 1000);

                self.onFocus();
            } else {
                self.$target.removeClass("move_to_top");
                $("#wrapwrap").removeClass("top_content");
                $("#wrap").css("margin-top", "");

                var offset = self.$target.offset.top;
                $('html, body').animate({scrollTop:(offset+100)}, 1000);
            }

            if (self.$target.hasClass("s_media_block")) {
                $(window).trigger("resize");
                self.trigger_up('animation_start_demand', {
                    editableMode: true,
                    $target: self.$target,
                });
            }
        },
        onRemove: function (event) {
            var self = this;
            if (self.$target.hasClass("move_to_top")) {
                $("#wrapwrap").removeClass("top_content");
                $("#wrap").css("margin-top","");
            }
        }
    });
});
