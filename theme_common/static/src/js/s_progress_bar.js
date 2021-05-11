(function() {
    'use strict';

    var website = openerp.website;
    website.snippet.options.progress = website.snippet.options.colorpicker.extend({
        start: function () {
            if (this.$overlay) {
                this.bind_move_progress();
            }
            return this._super();
        },
        bind_move_progress: function () {
            var self = this;
            var $e = this.$overlay.find(".oe_handle.e").removeClass("readonly");
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
                self.$overlay.addClass("hidden");
                $(document)
                    .on("mousemove", move)
                    .one("mouseup", function () {
                        self.$overlay.removeClass("hidden");
                        $(document).off("mousemove", move);
                        self.BuildingBlock.cover_target(self.$overlay, self.$target);
                    });
            });
        },
    });
})();