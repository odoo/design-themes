/** @odoo-module */

import * as wTourUtils from '@website/js/tours/tour_utils';
import { _t } from "@web/core/l10n/translation";

const snippets = [
    {
        id: 's_split_intro',
        name: 'Split Intro',
        groupName: "Intro",
    },
    {
        id: 's_references_lite',
        name: 'References Lite',
        groupName: "People",
    },
    {
        id: 's_services_grid',
        name: 'Services Grid',
        groupName: "Columns",
    },
    {
        id: 's_hr',
        name: 'Separator',
    },
    {
        id: 's_text_image_full',
        name: 'Text - Image Full Width',
        groupName: "Content",
    },
    {
        id: 's_text_bold',
        name: 'Text Bold',
        groupName: "Text",
    },
    {
        id: 's_image_text_full',
        name: 'Image - Text Full Width',
        groupName: "Content",
    },
    {
        id: 's_company_team_detail',
        name: 'Team Detail',
        groupName: "People",
    },
    {
        id: 's_cta_centered',
        name: 'Centered Call to Action',
        groupName: "Content",
    },
];

wTourUtils.registerThemeHomepageTour("notes_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"default-21"'),
    ...wTourUtils.insertSnippet(snippets[0]),
    ...wTourUtils.clickOnText(snippets[0], 'h1'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.insertSnippet(snippets[1]),
    ...wTourUtils.insertSnippet(snippets[2]),
    ...wTourUtils.clickOnSnippet(snippets[2]),
    wTourUtils.changeOption('Services Grid', 'setContainerWidth', _t('width')),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.insertSnippet(snippets[3]),
    ...wTourUtils.insertSnippet(snippets[4]),
    ...wTourUtils.insertSnippet(snippets[5]),
    ...wTourUtils.insertSnippet(snippets[6]),
    ...wTourUtils.insertSnippet(snippets[7]),
    ...wTourUtils.insertSnippet(snippets[8]),
]);
