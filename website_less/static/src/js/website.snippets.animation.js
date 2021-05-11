// Backported from 52ca425

(function () {
    'use strict';

    var website = openerp.website;

    function load_called_template () {
        var ids_or_xml_ids = _.uniq($("[data-oe-call]").map(function () {return $(this).data('oe-call');}).get());
        if (ids_or_xml_ids.length) {
            openerp.jsonRpc('/website/multi_render', 'call', {
                'ids_or_xml_ids': ids_or_xml_ids
            }).then(function (data) {
                for (var k in data) {
                    var $data = $(data[k]);
                    // clean t-oe
                    $data.each(function () {
                        for (var k=0; k<this.attributes.length; k++) {
                            if (this.attributes[k].name.indexOf('data-oe-') === 0) {
                                $(this).removeAttr(this.attributes[k].name);
                                k--;
                            }
                        }
                    });
                    // end
                    $("[data-oe-call='"+k+"']").each(function () {
                        $(this).replaceWith($data.clone());
                    });
                }
                $(document).trigger('scroll');
            });
        }
    }

    $(document).ready(load_called_template);

    $(document).ready(function () {
        $(".o_animation")
            .removeClass("o_displayed o_displayed_top o_displayed_middle o_displayed_bottom");
        $(document)
            .on('scroll', function (event) {
                var docViewTop = $(document.body).scrollTop();
                var docViewBottom = docViewTop + $(document.body).height();

                $(".o_animation")
                    .each(function () {
                        var $el = $(this);
                        var elemTop = $el.offset().top;
                        var elemBottom = elemTop + $el.height();
                        var elemMiddle = elemTop + $el.height()*0.4;
                        var visible = elemBottom >= docViewTop && elemTop <= docViewBottom;

                        if (visible) {
                            $el.addClass("o_displayed o_visible");
                        } else {
                            $el.removeClass("o_visible");
                        }

                        if (visible && elemTop > docViewTop) {
                            $el.addClass("o_displayed_top o_visible_top");
                        } else {
                            $el.removeClass("o_visible_top");
                        }
                        if (visible && elemMiddle < docViewBottom && elemMiddle > docViewTop) {
                            $el.addClass("o_displayed_middle o_visible_middle");
                        } else {
                            $el.removeClass("o_visible_middle");
                        }
                        if (visible && elemBottom < docViewBottom) {
                            $el.addClass("o_displayed_bottom o_visible_bottom");
                        } else {
                            $el.removeClass("o_visible_bottom");
                        }

                    });
            })
            .trigger('scroll');
    });

})();
