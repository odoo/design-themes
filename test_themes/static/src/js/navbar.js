odoo.define('test_themes.website_selector', function (require) {
'use strict';

const websiteNavbarData = require('website.navbar');

const TestThemesWebsiteSelector = websiteNavbarData.WebsiteNavbarActionWidget.extend({
    /**
     * @override
     */
    start: function () {
        this.$('.js_multi_website_switch[data-toggle]').tooltip({
            html: true,
            placement: 'left',
            delay: {show: 100, hide: 0},
        });
        return this._super(...arguments);
    },

});

websiteNavbarData.websiteNavbarRegistry.add(TestThemesWebsiteSelector, '#website_switcher');

return {
    TestThemesWebsiteSelector: TestThemesWebsiteSelector,
};
});
