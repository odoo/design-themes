/** @odoo-module */

import * as wTourUtils from '@website/js/tours/tour_utils';
import { _t } from "@web/core/l10n/translation";

const snippets = [
    {
        id: 's_picture',
        name: 'Title - Image',
        groupName: "Images",
    },
    {
        id: 's_references',
        name: 'References',
        groupName: "People",
    },
    {
        id: 's_text_image',
        name: 'Image - Text',
        groupName: "Content",
    },
    {
        id: 's_text_image',
        name: 'Text - Image',
        groupName: "Content",
    },
    {
        id: 's_title',
        name: 'Title',
        groupName: "Text",
    },
    {
        id: 's_comparisons',
        name: 'Comparisons',
        groupName: "Content",
    },
    {
        id: 's_call_to_action',
        name: 'Call to Action',
        groupName: "Content",
    },
];

wTourUtils.registerThemeHomepageTour("odoo_experts_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"odoo-experts-1"'),
    ...wTourUtils.insertSnippet(snippets[0]),
    ...wTourUtils.insertSnippet(snippets[1]),
    ...wTourUtils.insertSnippet(snippets[2]),
    ...wTourUtils.clickOnText(snippets[2], 'h2'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.insertSnippet(snippets[3]),
    ...wTourUtils.insertSnippet(snippets[4]),
    ...wTourUtils.insertSnippet(snippets[5]),
    ...wTourUtils.clickOnSnippet(snippets[5], 'top'),
    wTourUtils.changeOption('ColoredLevelBackground', 'we-button[data-toggle-bg-shape]', _t('Background Shape')),
    wTourUtils.selectNested('we-select-page', 'BackgroundShape', ':not(.o_we_pager_controls)', _t('Background Shape')),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.insertSnippet(snippets[6]),
]);
