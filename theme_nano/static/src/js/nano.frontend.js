odoo.define('theme_nano.frontend', function (require) {
'use strict';

var publicWidget = require('web.public.widget');
require('website.content.menu');

publicWidget.registry.affixMenu.include({
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
