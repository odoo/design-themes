/** @odoo-module **/

import * as wTourUtils from "@website/js/tours/tour_utils";

const snippets = [
    {
        id: 's_hero_minimalist',
        name: 'Hero Minimalist',
        groupName: "Intro",
    },
    {
        id: 's_text_block_split',
        name: 'Text Split',
        groupName: "Text",
    },
    {
        id: 's_services_grid',
        name: 'Services Grid',
        groupName: "Columns",
    },
    {
        id: 's_showcase_square',
        name: 'Showcase Square',
        groupName: "Content",
    },
    {
        id: 's_references_tiles',
        name: 'References Tiles',
        groupName: "People",
    },
    {
        id: 's_parallax',
        name: 'Parallax',
        groupName: "Images",
    },
    {
        id: 's_faq_collapse_centered',
        name: 'FAQ Centered',
        groupName: "Text",
    },
];


wTourUtils.registerThemeHomepageTour("graphene_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"graphene"'),
    ...wTourUtils.insertSnippet(snippets[0]),
    ...wTourUtils.clickOnText(snippets[0], 'h1'),
    wTourUtils.goBackToBlocks(),

    ...wTourUtils.insertSnippet(snippets[1]),
    ...wTourUtils.insertSnippet(snippets[2]),
    ...wTourUtils.insertSnippet(snippets[3]),
    ...wTourUtils.insertSnippet(snippets[4]),
    ...wTourUtils.insertSnippet(snippets[5]),
    ...wTourUtils.insertSnippet(snippets[6]),

    ...wTourUtils.clickOnSnippet(snippets[4], 'top'),
    wTourUtils.changeBackgroundColor(),
    wTourUtils.selectColorPalette(),
]);
