/** @odoo-module */

import * as wTourUtils from '@website/js/tours/tour_utils';

const snippets = [
    {
        id: 's_cover',
        name: 'Cover',
        groupName: "Intro",
    },
    {
        id: 's_about_bold',
        name: 'About Bold',
        groupName: "Columns",
    },
    {
        id: 's_pricelist_cafe',
        name: 'Pricelist Cafe',
        groupName: "Text",
    },
    {
        id: 's_reviews_wall',
        name: 'Reviews Wall',
        groupName: "People",
    },
    {
        id: 's_image_text_box',
        name: 'Image Text Box',
        groupName: "Content",
    },
    {
        id: 's_opening_hours_alt',
        name: 'Opening Hours Alt',
        groupName: "Contact & Forms",
    },
];

wTourUtils.registerThemeHomepageTour("bistro_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"bistro"'),
    ...wTourUtils.insertSnippet(snippets[0]),
    ...wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.insertSnippet(snippets[1]),
    ...wTourUtils.insertSnippet(snippets[2]),
    ...wTourUtils.clickOnSnippet(snippets[2]),
    wTourUtils.changeBackgroundColor(),
    wTourUtils.selectColorPalette(),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.insertSnippet(snippets[3]),
    ...wTourUtils.insertSnippet(snippets[4]),
    ...wTourUtils.insertSnippet(snippets[5]),
]);
