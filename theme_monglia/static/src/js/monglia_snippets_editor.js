(function () {
    'use strict';

    var website = openerp.website;

    // Set custom background from modal
    website.Theme.include({
        start: function () {
            this._super();
            this.$el.find('label:has(input[data-xmlid="theme_monglia.option_bg_custom"])').on('mouseup', _.bind(this.set_custom_bg, this));
            this.$el.find('label:has(input[data-xmlid="theme_monglia.option_pattern_custom"])').on('mouseup', _.bind(this.set_custom_bg, this));
        },
        change_selection: function (event, force) {
            var self = this;
            if (!force && event.originalEvent && (
                  $(event.target).is('input[data-xmlid="theme_monglia.option_bg_custom"]')
                  || $(event.target).is('input[data-xmlid="theme_monglia.option_pattern_custom"]')
                )) {
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
                var template_name = "option_bg_custom";
                var background_options = "background-size: cover; background-position: top center;";

                if ($.contains(document.getElementById("bg_pattern"), event.target)) {
                    template_name = "option_pattern_custom";
                    background_options = "background-repeat: repeat;"
                }

                $image.on('saved', this, function () {
                    var src = $image.attr('src');

                    self.$el.addClass("loading");

                    openerp.jsonRpc('/web/dataset/call', 'call', {
                        model: 'ir.model.data',
                        method: 'get_object_reference',
                        args: ["theme_monglia", template_name],
                    }).then(function (data) {

                        openerp.jsonRpc('/web/dataset/call', 'call', {
                            model: 'ir.ui.view',
                            method: 'save',
                            args: [
                                data[1],
                                "body{background-image: url('"+src+"'); " + background_options + "}",
                                "//style",
                                website.get_context()],
                        }).then(function () {

                            self.$el.removeClass("loading");
                            self.change_selection(event, true);
                        });

                    });

                });

                editor.on('cancel', this, function () {
                    if(typeof callback === "function") {
                        callback();
                    }
                });

                editor.appendTo(document.body);

            },0);
        }
    });


})();