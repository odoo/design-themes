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
        id: 's_image_text',
        name: 'Image - Text',
        groupName: "Content",
    },
    {
        id: 's_picture',
        name: 'Title - Image',
        groupName: "Images",
    },
    {
        id: 's_masonry_block',
        name: 'Masonry',
        groupName: "Images",
    },
    {
        id: 's_call_to_action',
        name: 'Call to Action',
        groupName: "Content",
    },
];

wTourUtils.registerThemeHomepageTour("vehicle_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"vehicle-1"'),
    ...wTourUtils.dragNDrop(snippets[0], 'top'),
    ...wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.dragNDrop(snippets[1], 'top'),
    ...wTourUtils.dragNDrop(snippets[2], 'top'),
    ...wTourUtils.dragNDrop(snippets[3], 'top'),
    ...wTourUtils.dragNDrop(snippets[4], 'top'),
    ...wTourUtils.dragNDrop(snippets[5], 'top'),
    ...wTourUtils.clickOnSnippet(snippets[5]),
    wTourUtils.changeBackgroundColor(),
    wTourUtils.selectColorPalette(),
]);
