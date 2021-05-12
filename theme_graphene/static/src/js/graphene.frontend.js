odoo.define('theme_graphene.frontend', function (require) {
    'use strict';

    var base = require('web_editor.base');
    var sAnimation = require('website.content.snippets.animation');

    base.ready().then(function () {
        var graph_top_content   = false,
            $wrapwrap           = $("#wrapwrap"),
            $wrap               = $("#wrap"),
            $win                = $(window);

        $wrapwrap.find('.o_header_affix').removeAttr('id');
        // Top content layout
        if ($wrap.find(".move_to_top, #title.blog_header > .cover.cover_full").length > 0) {
            graph_top_content = true;
            $wrapwrap.addClass("top_content");
        }

        // Clean vertical align
        $(".v-align").filter(function () {
            return $(this).parent().is(":not(.slide)");
        }).addClass("preserve3d");

        $win.load(function () {})
            // Resize
            .on("resize", function () {
                if (graph_top_content) {
                    var $s = $wrap.find(".move_to_top, #title.blog_header > .cover.cover_full");
                    $wrap.css("margin-top", ($s.outerHeight() * 0.8));
                }
            })
            .trigger("resize");
    });

    // Ripple animation
    sAnimation.registry.graph_links = sAnimation.Class.extend({
        selector: ".btn, .dropdown-menu li a",

        start: function () {
            var btn = this.$target;

            btn
            .css({ position: 'relative', overflow: 'hidden'})
            .bind('mousedown', function (e) {
                var ripple;
                if (btn.find('.graph-ripple').length === 0) {
                    ripple = $('<span class="graph-ripple"/>');
                    btn.prepend(ripple);
                } else {
                    ripple = btn.find('.graph-ripple');
                }
                ripple.removeClass('graph-ripple-animated');

                if (!ripple.height() && !ripple.width()) {
                    var diameter = Math.max(btn.outerWidth(), btn.outerHeight());
                    ripple.css({ height: diameter, width: diameter });
                }

                var x = e.pageX - btn.offset().left - ripple.width() / 2;
                var y = e.pageY - btn.offset().top - ripple.height() / 2;

                ripple
                    .css({ top: y + 'px',left: x + 'px'})
                    .addClass('graph-ripple-animated');

                setTimeout(function () {
                    ripple.removeClass('graph-ripple-animated');
                }, 351);
            });

            return this._super.apply(this, arguments);
        },
    });
});
