odoo.define('theme_common.compatibility_editor', function (require) {
'use strict';

var sOptions = require('web_editor.snippets.options');

sOptions.registry.BackgroundImage.include({
    /**
     * @override
     */
    background: function (previewMode, widgetValue, params) {
        this._super.apply(this, arguments);

        var customClass = this.$target.attr('class').match(/\b(bg-img-\d+)\b/);
        if (customClass) {
            this.$target.removeClass(customClass[1]);
        }
    },
});
});
