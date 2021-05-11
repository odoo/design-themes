odoo.define('theme_common.s_progress_bar', function (require) {
    'use strict';

    var s_options = require('web_editor.snippets.options');

    s_options.registry.progress = s_options.Class.extend({
        start: function () {
            if (this.$overlay) {
                this.bind_move_progress();
            }
            this._super();
        },

        bind_move_progress: function () {
            var self = this;
            var $e = this.$overlay.find(".o_handle.e").removeClass("readonly");
            var $parent = this.$target.parent();
            var pos = $parent.offset();
            var width = $parent.width();
            var time;
            function move(event) {
                clearTimeout(time);
                time = setTimeout(function () {
                    var value = (event.clientX - pos.left)/width*100 | 0;
                    if (value > 100 ) value = 100;
                    if (value < 0 ) value = 0;
                    self.$target.text( self.$target.text().replace(/[0-9]+/, value) );
                    self.$target.attr("data-value", value);
                    if (value < 3 ) value = 3;
                    self.$target.css("width", value + "%");
                },5);
            }
            $e.on("mousedown", function () {
                self.$overlay.addClass('d-none');
                $(document)
                    .on("mousemove", move)
                    .one("mouseup", function () {
                        self.$overlay.removeClass('d-none');
                        $(document).off("mousemove", move);
                        self.trigger_up('cover_update');
                    });
            });
        },
    });
});
