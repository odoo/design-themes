/** @odoo-module */
import wTourUtils from '@website/js/tours/tour_utils';

const snippets = [
    {
        id: 's_cover',
        name: 'Cover',
        groupName: "Intro",
    },
    {
        id: 's_picture',
        name: 'Title - Image',
        groupName: "Images",
    },
    {
        id: 's_three_columns',
        name: 'Columns',
        groupName: "Columns",
    },
    {
        id: 's_text_image',
        name: 'Text - Image',
        groupName: "Content",
    },
    {
        id: 's_call_to_action',
        name: 'Call to Action',
        groupName: "Content",
    },
];

wTourUtils.registerThemeHomepageTour("avantgarde_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"avantgarde-3"'),
    ...wTourUtils.dragNDrop(snippets[0], 'top'),
    ...wTourUtils.clickOnText(snippets[0], 'h1', 'left'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.dragNDrop(snippets[1], 'left'),
    ...wTourUtils.dragNDrop(snippets[2], 'bottom'),
    ...wTourUtils.clickOnSnippet(snippets[2], 'top'),
    wTourUtils.changePaddingSize('top'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.dragNDrop(snippets[3], 'top'),
    ...wTourUtils.dragNDrop(snippets[4], 'top'),
]);
