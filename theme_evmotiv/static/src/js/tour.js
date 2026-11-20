/** @odoo-module */

import * as wTourUtils from '@website/js/tours/tour_utils';

const snippets = [
    {
        id: 's_cover',
        name: 'Cover',
        groupName: "Intro",
    },
];

wTourUtils.registerThemeHomepageTour("evmotiv_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"evmotiv-1"'),
    ...wTourUtils.insertSnippet(snippets[0]),
    ...wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks(),
]);
