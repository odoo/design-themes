(function () {
    'use strict';

    var website = openerp.website;

    // Set custom background image from modal
    website.Theme.include({
        current_theme: undefined,
        on_select: function ($inputs, event) {
            var self= this;
            this._super($inputs, event);

            var $input = $($inputs).filter('input[data-xmlid*="body_bg_image"]').length ? $($inputs).filter('input[data-xmlid*="body_bg_image"]') : $($inputs).filter('input[data-customize-bg]');
            if (!$input.length || event.isDefaultPrevented()) return;
            event.preventDefault();

            var $image = $('<img>');
            var editor = new website.editor.MediaDialog(null, $image[0], { only_images: true });

            editor.on('saved', this, function (media) {
                var src = $(media).attr('src');
                self.$el.addClass("loading");
                openerp.jsonRpc('/web/dataset/call', 'call', {
                    model: 'ir.model.data',
                    method: 'get_object_reference',
                    args: [this.$el.data('theme'), $input.data('xmlid').split('.').slice(-1)[0]],
                }).then(function (data) {
                    openerp.jsonRpc('/web/dataset/call', 'call', {
                        model: 'ir.ui.view',
                        method: 'save',
                        args: [
                            data[1],
                            "body{background-image: url('"+src+"'); background-size: cover; background-position: center;background-attachment: fixed;}",
                            "//style",
                            website.get_context()],
                    }).then(function () {
                        self.$el.removeClass("loading");
                        $input.prop("checked", true);
                        self.change_selection(event);
                    });
                });
            });
            editor.on('cancel', this, function () {
                if(typeof callback === "function") {
                    callback();
                }
            });
            editor.appendTo(document.body);
        }
    });
})();
