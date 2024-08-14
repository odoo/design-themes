/** @odoo-module */

import wTourUtils from '@website/js/tours/tour_utils';

const snippets = [
    {
        id: 's_cover',
        name: 'Cover',
        groupName: "Intro",
    },
    {
        id: 's_image_text',
        name: 'Image - Text',
        groupName: "Content",
    },
    {
        id: 's_references',
        name: 'References',
        groupName: "People",
    },
    {
        id: 's_three_columns',
        name: 'Columns',
        groupName: "Columns",
    },
    {
        id: 's_comparisons',
        name: 'Comparisons',
        groupName: "Content",
    },
    {
        id: 's_call_to_action',
        name: 'Call to Action',
        groupName: "Content",
    },
];


wTourUtils.registerThemeHomepageTour("paptic_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"paptic-1"'),
    ...wTourUtils.dragNDrop(snippets[0], 'top'),
    ...wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.dragNDrop(snippets[1], 'top'),
    ...wTourUtils.dragNDrop(snippets[2], 'top'),
    ...wTourUtils.dragNDrop(snippets[3], 'top'),
    ...wTourUtils.dragNDrop(snippets[4], 'top'),
    ...wTourUtils.dragNDrop(snippets[5], 'top'),
]);
