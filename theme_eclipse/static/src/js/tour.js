/** @odoo-module */

import * as wTourUtils from '@website/js/tours/tour_utils';

const snippets = [
    {
        id: 's_discovery',
        name: 'Discovery',
        groupName: "Intro",
    },
    {
        id: 's_references',
        name: 'References',
        groupName: "People",
    },
    {
        id: 's_hr',
        name: 'Separator',
    },
    {
        id: 's_features',
        name: 'Features',
        groupName: "Content",
    },
    {
        id: 's_text_image',
        name: 'Text - Image',
        groupName: "Content",
    },
    {
        id: 's_quotes_carousel_compact',
        name: 'Quotes Compact',
        groupName: "People",
    },
    {
        id: 's_image_text',
        name: 'Image - Text',
        groupName: "Content",
    },
    {
        id: 's_key_images',
        name: 'Key Images',
        groupName: "Columns",
    },
    {
        id: 's_cta_mobile',
        name: 'CTA Mobile',
        groupName: "Content",
    },
    {
        id: 's_announcement_scroll',
        name: 'Announcement Scroll',
        groupName: "Catalog",
    },
];

wTourUtils.registerThemeHomepageTour("eclipse_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"eclipse"'),
    ...wTourUtils.insertSnippet(snippets[0]),
    ...wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.insertSnippet(snippets[1]),
    ...wTourUtils.insertSnippet(snippets[2]),
    ...wTourUtils.insertSnippet(snippets[3]),
    ...wTourUtils.clickOnSnippet(snippets[3]),
    wTourUtils.changeBackgroundColor(),
    wTourUtils.selectColorPalette(),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.insertSnippet(snippets[4]),
    ...wTourUtils.insertSnippet(snippets[5]),
    ...wTourUtils.insertSnippet(snippets[6]),
    ...wTourUtils.insertSnippet(snippets[7]),
    ...wTourUtils.insertSnippet(snippets[8]),
    ...wTourUtils.insertSnippet(snippets[9]),
]);
