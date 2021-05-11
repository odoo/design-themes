odoo.define('theme_common.compatibility_editor', function (require) {
'use strict';

var sOptions = require('web_editor.snippets.options');

sOptions.registry.background.include({
    /**
     * @override
     */
    background: function (previewMode, value, $opt) {
        this._super.apply(this, arguments);

        var customClass = this.$target.attr('class').match(/\b(bg-img-\d+)\b/);
        if (customClass) {
            this.$target.removeClass(customClass[1]);
        }
    },
});
});
