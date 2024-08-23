/** @odoo-module */

import * as wTourUtils from '@website/js/tours/tour_utils';

const snippets = [
    {
        id: 's_banner',
        name: 'Banner',
        groupName: "Intro",
    },
    {
        id: 's_three_columns',
        name: 'Columns',
        groupName: "Columns",
    },
    {
        id: 's_color_blocks_2',
        name: 'Big Boxes',
        groupName: "Content",
    },
    {
        id: 's_features',
        name: 'Features',
        groupName: "Content",
    },
    {
        id: 's_masonry_block',
        name: 'Masonry',
        groupName: "Images",
    },
    {
        id: 's_references',
        name: 'References',
        groupName: "People",
    },
];

wTourUtils.registerThemeHomepageTour("zap_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"zap-1"'),
    ...wTourUtils.dragNDrop(snippets[0]),
    ...wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.dragNDrop(snippets[1]),
    ...wTourUtils.dragNDrop(snippets[2]),
    ...wTourUtils.dragNDrop(snippets[3]),
    ...wTourUtils.dragNDrop(snippets[4]),
    ...wTourUtils.dragNDrop(snippets[5]),
    ...wTourUtils.clickOnSnippet(snippets[5], 'top'),
    wTourUtils.changeBackgroundColor(),
    wTourUtils.selectColorPalette(),
]);
