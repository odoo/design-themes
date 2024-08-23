/** @odoo-module **/

import * as wTourUtils from "@website/js/tours/tour_utils";

const snippets = [
    {
        id: 's_cover',
        name: 'Cover',
        groupName: "Intro",
    },
    {
        id: 's_text_image',
        name: 'Text - Image',
        groupName: "Content",
    },
    {
        id: 's_numbers',
        name: 'Numbers',
        groupName: "Content",
    },
    {
        id: 's_picture',
        name: 'Title - Image',
        groupName: "Images",
    },
    {
        id: 's_comparisons',
        name: 'Comparisons',
        groupName: "Content",
    },
];


wTourUtils.registerThemeHomepageTour("graphene_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"graphene-1"'),
    ...wTourUtils.dragNDrop(snippets[0]),
    ...wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks('left'),

    ...wTourUtils.dragNDrop(snippets[1]),

    ...wTourUtils.dragNDrop(snippets[2]),
    ...wTourUtils.dragNDrop(snippets[3], 'top'),

    ...wTourUtils.dragNDrop(snippets[4], 'top'),
    ...wTourUtils.clickOnSnippet(snippets[4], 'top'),
    wTourUtils.changeBackgroundColor('left'),
    wTourUtils.selectColorPalette(),
]);
