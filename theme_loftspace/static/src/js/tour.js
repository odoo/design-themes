/** @odoo-module */

import * as wTourUtils from '@website/js/tours/tour_utils';

const snippets = [
    {
        id: 's_banner',
        name: 'Banner',
        groupName: "Intro",
    },
    {
        id: 's_text_block',
        name: 'Text',
        groupName: "Text",
    },
    {
        id: 's_striped',
        name: 'Striped section',
        groupName: "Content",
    },
    {
        id: 's_key_images',
        name: 'Key Images',
        groupName: "Columns",
    },
    {
        id: 's_features',
        name: 'Features',
        groupName: "Content",
    },
    {
        id: 's_quotes_carousel',
        name: 'Quotes',
        groupName: "People",
    },
    {
        id: 's_faq_collapse',
        name: 'FAQ Block',
        groupName: "Text",
    },
    {
        id: 's_cta_box',
        name: 'Box Call to Action',
        groupName: "Content",
    },
];

wTourUtils.registerThemeHomepageTour("loftspace_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"graphene-2"'),
    ...wTourUtils.dragNDrop(snippets[0]),
    ...wTourUtils.clickOnText(snippets[0], 'h1'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.dragNDrop(snippets[1]),
    ...wTourUtils.dragNDrop(snippets[2]),
    ...wTourUtils.dragNDrop(snippets[3]),
    ...wTourUtils.dragNDrop(snippets[4]),
    ...wTourUtils.dragNDrop(snippets[5]),
    ...wTourUtils.dragNDrop(snippets[6]),
    ...wTourUtils.dragNDrop(snippets[7]),
    ...wTourUtils.dragNDrop(snippets[8]),
    ...wTourUtils.clickOnSnippet(snippets[4]),
    wTourUtils.changeBackgroundColor(),
    wTourUtils.selectColorPalette(),
]);
