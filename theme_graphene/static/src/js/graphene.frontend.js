odoo.define('theme_graphene.frontend', function (require) {
    'use strict';

    var base = require('web_editor.base');
    var s_animation = require('web_editor.snippets.animation');
    var session = require('web.session');

    base.ready().then(function () {
        var self                = $(this),
            $graph_header       = $("#graph_header"),
            $graph_header_clone = null,
            graph_header_affix  = false,
            graph_top_content   = false,
            $wrapwrap           = $("#wrapwrap"),
            $wrap               = $("#wrap"),
            $win                = $(window),
            winH                = $(window).height(),
            winW                = $(window).width(),
            edit_bar_h          = null;

        // Top content layout
        if ($wrap.find(".move_to_top, .cover.cover_full").length > 0) {
            graph_top_content = true;
            $wrapwrap.addClass("top_content");
        }

        // Top Affix Menu
        if ($graph_header.hasClass("top_menu_affix")) {
            graph_header_affix = true;
            var $graph_header_clone = $graph_header.clone().insertAfter($graph_header).attr("id","graph_header_affix").addClass("affix");
            $graph_header_clone.find('[data-toggle="collapse"]').each(function () {
                var source = $(this),
                        coo    = source.attr("data-target"),
                        target = $graph_header_clone.find(coo),
                        c      = coo.substring(1);
                source.attr("data-target", coo + "_clone");
                target.removeClass(c).addClass(c + "_clone" );
            });
        };

        // Clean vertical align
        $(".v-align").filter(function () {
            return $(this).parent().is(":not(.slide)");
        }).addClass("preserve3d");

        $win.load(function () {})
            // Resize
            .on("resize", function () {
                winH = $(window).height(),
                winW = $(window).width();
                if ($("#oe_main_menu_navbar").length > 0) {
                    edit_bar_h = $("#oe_main_menu_navbar").outerHeight();
                    if (graph_header_affix) {$graph_header_clone.css("top", edit_bar_h)}
                }
                if (graph_top_content) {
                    var s = $wrap.find(".move_to_top, .cover.cover_full");
                    $wrap.css("margin-top", (s.height()* 0.9));
                };
                $win.trigger("scroll");
            })
            // Scroll
            .on("scroll", function () {
                if (graph_header_affix) {
                    var wOffset  = $win.scrollTop();
                    var hOffset  = $graph_header.scrollTop();
                    (wOffset > (hOffset + 300) )? $graph_header_clone.addClass("affixed") : $graph_header_clone.removeClass("affixed");
                }
            })
            .trigger("resize");
    });

    // Graphene Theme
    s_animation.registry.graph_init = s_animation.Class.extend({
        selector : "body",

        stop: function () {
            $('#graph_header_affix').remove();
        },
    });

    // Ripple animation
    s_animation.registry.graph_links = s_animation.Class.extend({
        selector: ".btn, .dropdown-menu li a",

        start: function () {
            var timeout,
                btn = this.$target;

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
        },
    });
});
