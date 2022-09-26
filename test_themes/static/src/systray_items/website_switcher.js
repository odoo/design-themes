/** @odoo-module **/

import { patch } from 'web.utils';
import { useService } from '@web/core/utils/hooks';
import { WebsiteSwitcherSystray } from '@website/systray_items/website_switcher';

const { onMounted, useState } = owl;

patch(WebsiteSwitcherSystray.prototype, 'test_themes_website_switcher_systray', {
    setup() {
        this._super();

        this.orm = useService('orm');
        this.tooltips = useState({});

        onMounted(async () => {
            const themesWebsites = await this.orm.call('website', 'get_test_themes_websites_theme_preview');
            for (const themeId in themesWebsites) {
                this.tooltips[themeId] = {
                    tooltipTemplate: 'test_themes.ThemeTooltip',
                    tooltipPosition: 'left',
                    tooltipDelay: 100,
                    tooltipInfo: JSON.stringify({url: themesWebsites[themeId]}),
                };
            }
        });
    },
    template: 'test_themes.WebsiteSwitcherSystray',
});
