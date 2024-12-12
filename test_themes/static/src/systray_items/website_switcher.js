/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { useService } from '@web/core/utils/hooks';
import { WebsiteSwitcherSystray } from '@website/systray_items/website_switcher';
import { onMounted, useState } from "@odoo/owl";

patch(WebsiteSwitcherSystray.prototype, {
    setup() {
        super.setup();

        this.orm = useService('orm');
        this.tooltips = useState({});
        // Disable the notification service to avoid having a notification for each theme.
        this.notificationService = { add: () => () => null };

        onMounted(async () => {
            const themesWebsites = await this.orm.call('website', 'get_test_themes_websites_theme_preview');
            for (const themeId in themesWebsites) {
                this.tooltips[themeId] = {
                    "data-tooltip-template": 'test_themes.ThemeTooltip',
                    "data-tooltip-position": 'left',
                    "data-tooltip-delay": 100,
                    "data-tooltip-info": JSON.stringify({url: themesWebsites[themeId]}),
                };
            }
        });
    },

    getElements() {
        // Add tooltip information
        const elements = this._super();
        return elements.map((elem) => {
            elem.dataset = {
                ...elem.dataset,
                ...this.tooltips[elem.id]
            };
            return elem
        });
    },

    template: 'test_themes.WebsiteSwitcherSystray',
});
