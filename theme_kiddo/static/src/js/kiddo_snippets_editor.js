(function () {
    'use strict';

    var website = openerp.website;

    // Set custom background image from modal
    website.Theme.include({
        start: function () {
            var self = this;
            return this._super.apply(this, arguments).then(function() {
                self.$('label:has(input[data-xmlid="theme_kiddo.option_bg_custom"])').on('click', _.bind(self.set_custom_bg, self));
            });
        },
        change_selection: function (event, force) {
            if (!force && (event.originalEvent && $(event.target).is('input[data-xmlid="theme_kiddo.option_bg_custom"]'))) {
                this.set_custom_bg(event);
                return;
            }

            this._super(event);
        },
        set_custom_bg: function (event) {
            var self = this;

            clearTimeout(this.set_custom_bg_time);
            this.set_custom_bg_time = setTimeout(function () {
                var $image = $('<img>');
                var element = new CKEDITOR.dom.element($image[0]);
                var editor = new website.editor.MediaDialog({}, element);

                $image.on('saved', this, function () {
                    var src = $image.attr('src');

                    self.$el.addClass("loading");

                    openerp.jsonRpc('/web/dataset/call', 'call', {
                        model: 'ir.model.data',
                        method: 'get_object_reference',
                        args: ["theme_kiddo", "option_bg_custom"],
                    }).then(function (data) {
                        openerp.jsonRpc('/web/dataset/call', 'call', {
                            model: 'ir.ui.view',
                            method: 'save',
                            args: [
                                data[1],
                                "body{background-image: url('"+src+"'); background-size: cover; background-position: top center;}",
                                "//style",
                                website.get_context()
                            ],
                        }).then(function () {
                            self.$el.removeClass("loading");
                            self.change_selection(event, true);
                        });
                    });
                });

                editor.appendTo(document.body);
            }, 0);
        }
    });
})();
