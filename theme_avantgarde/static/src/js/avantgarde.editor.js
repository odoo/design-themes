odoo.define('theme_avantgarde.editor', function (require) {
    'use strict';

    var Editor = require('web_editor.snippet.editor').Editor;
    var s_options = require('web_editor.snippets.options');

    // Typography
    s_options.registry.typo_style = s_options.Class.extend({
    });

    s_options.registry.no_resize = s_options.Class.extend({
        start: function () {
            self = this;
            setTimeout(function () {
                self.$overlay.find(".oe_handle_button.size").hide();
            }, 50)
        },
    });

    // Simple Accordition
    s_options.registry.avant_simpleAccordition = s_options.Class.extend({
        start: function () {
            self = this;
            self.$target.find(".panel-collapse ").css("height","").addClass("in");
        },
        clean_for_save: function () {
            self = this;
            self.$target.find(".panel-collapse ").css("height","0").removeClass("in");
        },
        drop_and_build_snippet: function () {
            self = this;
            self.$target.find(".panel-collapse ").css("height","").addClass("in");
        },
        on_clone: function ($clone) {
            var Mrand = Math.floor((Math.random() * 9999999) + 1);
            $clone.find("div.panel-group").attr("id",Mrand);
            $clone.find(".bar").each(function () {
                var bar = $(this);
                var rand = Math.floor((Math.random() * 9999999) + 1);
                bar.find("a.panel-heading").attr("data-cke-saved-href","#"+rand);
                bar.find("a.panel-heading").attr("data-parent","#"+Mrand);
                bar.find("div.panel-collapse.collapse").attr("id",rand);
            });
        },
    });

    s_options.registry.avant_simpleAccordition_bar = s_options.Class.extend({
        start: function () {
            self = this;
            self.$target.parent().parent().find(".panel-collapse ").css("height","").addClass("in");
        },
        on_focus: function () {
          self = this;
          self.$target.fadeTo(100,0).fadeTo(200,1);
        },
        on_clone: function ($clone) {
            var rand = Math.floor((Math.random() * 9999999) + 1);
            $clone.find("a.panel-heading").attr("data-cke-saved-href","#"+rand);
            $clone.find("div.panel-collapse.collapse").attr("id",rand);
        },
    });

    s_options.registry.avant_simpleAccordition_link = s_options.Class.extend({
        start: function () {
          self = this;
          self.$target.parent().parent().parent().find(".panel-collapse ")
            .css("height","")
            .addClass("in");
        },
        on_focus: function () {
          self = this;
          self.$target.fadeTo(100,0).fadeTo(200,1);
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
                    .o_anim_fade_in(2000);
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
                    .o_anim_fade_in(2000);
            }
        },
    });

    Editor.include({
        _drag_and_drop_start: function () {
            this._super();
            this.$target.addClass("oe_snippet_body");
            return this._super.apply(this, arguments);
        },
        _drag_and_drop_stop: function () {
            this._super();
            this.$target.removeClass("oe_snippet_body")
            return this._super.apply(this, arguments);
        },
    });

    // Top Banner Options
    s_options.registry.avantgarde_top_banner_options = s_options.Class.extend({
        start: function () {
            this._super();
            var self = this;
            if (!self.$target.parent().is("#wrap")) {
                console.log(self)
                setTimeout(function () {
                    //self.$el.remove();
                })
            }
        },
        on_focus: function () {
            var self = this;
            if (self.$target.hasClass("move_to_top")) {
                self.$overlay
                    .find(".oe_overlay_options").css("margin-top","200px").end()
                    .find(".oe_snippet_clone, .oe_snippet_move").addClass("hidden");
            } else {
                self.$overlay
                    .find(".oe_snippet_clone, .oe_snippet_move").removeClass("hidden");
            }
        },
        select_class: function (type, value, $li) {
            if (type != "click") {return}
            this._super(type, value, $li);
            var self = this;
            if (value == "move_to_top") {
                self.$target.addClass("move_to_top");
                $("#wrapwrap").addClass("top_content");
                $(".move_to_top").not(self.$target).removeClass("move_to_top");
                $("#wrap").css("margin-top", (self.$target.height()* 0.9));

                if (!self.$target.parent().is("#wrap")) {
                    self.$target.wrap("span").prependTo($("#wrap"));
                    if ($('#wrap > *:nth-child(2)').length > 0) $('#wrap > *:nth-child(2)').css("width", "100%");
                }
                if (($('#wrap > *:nth-child(2)').length > 0) && !($('#wrap > *:nth-child(2)').is('[class*="bg-"]'))) {
                    $('#wrap > *:nth-child(2)').addClass("bg-white");
                }
                $('html, body').animate({scrollTop:0}, 1000);

            } else {
                self.$target.removeClass("move_to_top");
                $("#wrapwrap").removeClass("top_content");
                //$("body").data('snippet-view').remove_top_content();
                $("#wrap").css("margin-top","");
                var offset = self.$target.offset.top;
                $('html, body').animate({scrollTop:(offset+100)}, 1000);
            }
            if (self.$target.hasClass("s_media_block")) {
                $(window).trigger("resize");
                self.$target.data('snippet-view').stop_video();
                self.$target.data('snippet-view').start_video();
            }
        },
    });

    // FIX website builder overlay issues + Change margin
    s_options.registry.marginAndResize.include({
        start: function () {
            this._super();
            var self = this;

            $(window).on("resize", function () {
                self.buildingBlock.cover_target(self.$overlay, self.$target);
            })

            this.$overlay.find(".oe_handle.size .size").on('mouseup', function (event) {
                event.preventDefault();
                if (self.$target.hasClass("move_to_top")) {
                    $("#wrap").css("margin-top", (self.$target.height()* 0.9));
                    self.buildingBlock.cover_target(self.$overlay, self.$target);
                    $(window).trigger("resize");
                }
            });
        },
    });
});
