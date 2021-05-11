odoo.define("theme_graphene_blog.editor", function (require) {
    "use strict";

    var s_options = require('web_editor.snippets.options');
    require("website_blog.editor");

    var $wrapwrap = $("#wrapwrap");
    var $wrap = $("#wrap");

    // Preview blog post's cover layouts
    s_options.registry.CoverProperties.include({
        clear: function (previewMode, value, $li) {
            this._super.apply(this, arguments);
            this._preview_layout();
        },
        selectClass: function () {
            this._super.apply(this, arguments);
            this._preview_layout();
        },
        _preview_layout: function () {
            if (this.$target.hasClass("cover_full")) {
                $wrapwrap.addClass("o_header_overlay");
                $wrap.css("margin-top", this.$target.outerHeight() * 0.8);
            } else {
                $wrapwrap.removeClass("o_header_overlay");
                $wrap.css("margin-top", "");
            }
        }
    });
});
