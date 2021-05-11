odoo.define('theme_common.background_image', function (require) {
    'use strict';

    var ajax = require('web.ajax');
    var MediaDialog = require('web_editor.widget').MediaDialog;
    var Theme = require('website.theme');
    var weContext = require('web_editor.context');

    // Set custom background image from modal
    Theme.include({
        current_theme: undefined,

        on_select: function ($inputs, event) {
            var self= this;
            this._super($inputs, event);

            var $input = $($inputs).filter('input[data-xmlid*="body_bg_image"]').length ? $($inputs).filter('input[data-xmlid*="body_bg_image"]') : $($inputs).filter('input[data-customize-bg]');
            if (!$input.length || event.isDefaultPrevented()) return;
            event.preventDefault();

            var $image = $('<img>');
            var editor = new MediaDialog(this, {only_images: true}, null, $image[0]);

            editor.on('save', this, function (media) {
                var src = $(media).attr('src');
                self.$el.addClass("loading");
                ajax.jsonRpc('/web/dataset/call', 'call', {
                    model: 'ir.model.data',
                    method: 'get_object_reference',
                    args: [this.$el.data('theme'), $input.data('xmlid').split('.').slice(-1)[0]],
                }).then(function (data) {
                    ajax.jsonRpc('/web/dataset/call', 'call', {
                        model: 'ir.ui.view',
                        method: 'save',
                        args: [
                            data[1],
                            "body{background-image: url('"+src+"'); background-size: cover; background-position: center;background-attachment: fixed;}",
                            "//style",
                            weContext.get()],
                    }).then(function () {
                        self.$el.removeClass("loading");
                        $input.prop("checked", true);
                        self.change_selection(event);
                    });
                });
            });
            editor.on('cancel', this, function () {
                if (typeof callback === "function") {
                    callback();
                }
            });

            editor.open();
        },
    });
});
