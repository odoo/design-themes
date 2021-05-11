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
            }, 50);
        },
    });

    // Simple Accordition
    s_options.registry.avant_simpleAccordition = s_options.Class.extend({
        start: function () {
            self = this;
            self.$target.find(".panel-collapse ").css("height","").addClass("in");
        },
        cleanForSave: function () {
            self = this;
            self.$target.find(".panel-collapse ").css("height","0").removeClass("in");
        },
        onClone: function () {
            var Mrand = Math.floor((Math.random() * 9999999) + 1);
            this.$target.find("div.panel-group").attr("id",Mrand);
            this.$target.find(".bar").each(function () {
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
        onFocus: function () {
          self = this;
          self.$target.fadeTo(100,0).fadeTo(200,1);
        },
        onClone: function () {
            var rand = Math.floor((Math.random() * 9999999) + 1);
            this.$target.find("a.panel-heading").attr("data-cke-saved-href","#"+rand);
            this.$target.find("div.panel-collapse.collapse").attr("id",rand);
        },
    });

    s_options.registry.avant_simpleAccordition_link = s_options.Class.extend({
        start: function () {
          self = this;
          self.$target.parent().parent().parent().find(".panel-collapse ")
            .css("height","")
            .addClass("in");
        },
        onFocus: function () {
          self = this;
          self.$target.fadeTo(100,0).fadeTo(200,1);
        },
    });

    Editor.include({
        _onDragAndDropStart: function () {
            this._super();
            this.$target.addClass("oe_snippet_body");
            return this._super.apply(this, arguments);
        },
        _onDragAndDropStop: function () {
            this._super();
            this.$target.removeClass("oe_snippet_body");
            return this._super.apply(this, arguments);
        },
    });

    // Top Banner Options
    s_options.registry.avantgarde_top_banner_options = s_options.Class.extend({
        onFocus: function () {
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

            this.$overlay.find(".oe_handle.size .size").on('mouseup', function (event) {
                event.preventDefault();
                if (self.$target.hasClass("move_to_top")) {
                    $("#wrap").css("margin-top", (self.$target.outerHeight() * 0.9));
                    self.trigger_up('cover_update');
                    $(window).trigger("resize");
                }
            });
        },
    });
});
