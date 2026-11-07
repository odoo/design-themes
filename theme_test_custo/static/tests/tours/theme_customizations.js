/** @odoo-module */

import * as wTourUtils from '@website/js/tours/tour_utils';

wTourUtils.registerWebsitePreviewTour('theme_customizations', {
}, () => [
    ...wTourUtils.clickOnEditAndWaitEditMode(),
    {
        content: 'Click on footer',
        trigger: ':iframe footer',
        run: "click",
    }, {
        content: 'The theme custom footer template should be listed and selected',
        trigger: '[data-container-title="Footer"] [data-label="Template"]:has(.o-dropdown-item.active[data-action-param*="custom-theme"])',
    }, {
        content: 'Click on header',
        trigger: ':iframe header',
        run: "click",
    }, {
        content: 'The theme custom header template should be listed and selected',
        trigger: '[data-container-title="Header"] [data-label="Template"]:has(.o-dropdown-item.active[data-action-param*="custom-theme"])',
    }, {
        content: 'Click on image which has a shape',
        trigger: ':iframe #wrap .s_text_image img[data-shape]',
        run: "click",
    }, {
        content: 'The theme custom "Blob 01" shape should be listed and selected',
        trigger: '[data-container-title="Image"] [data-label="Shape"] button.btn-secondary:contains("Blob 01")',
    }, {
        content: 'Click on section which has a bg shape',
        trigger: ':iframe #wrap .s_text_block[data-oe-shape-data]',
        run: "click",
    }, {
        content: 'The theme custom "Curve 01" shape should be listed and selected',
        trigger: '[data-container-title="Text"] [data-label="Shape"] button.btn-secondary:contains("Curve 01")',
    },
]);
