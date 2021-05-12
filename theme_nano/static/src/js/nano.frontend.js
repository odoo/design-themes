odoo.define('theme_nano.frontend', function (require) {
'use strict';

var sAnimation = require('website.content.snippets.animation');
require('website.content.menu');

sAnimation.registry.affixMenu.include({
    /**
     * @override
     */
    start: function () {
        var def = this._super.apply(this, arguments);
        if (this.$headerClone) {
            this.$headerClone.find('#preheader').remove();
        }
        return def;
    },
});
});
