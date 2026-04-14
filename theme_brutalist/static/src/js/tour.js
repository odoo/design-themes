/** @odoo-module */

import * as wTourUtils from '@website/js/tours/tour_utils';

const snippets = [
    {
        id: 's_framed_intro',
        name: 'Framed Intro',
        groupName: "Intro",
    },
    {
        id: 's_awards_list',
        name: 'Awards List',
        groupName: "Text",
    },
    {
        id: 's_title',
        name: 'Title',
        groupName: "Text",
    },
    {
        id: 's_wavy_grid',
        name: 'Wavy Grid',
        groupName: "Columns",
    },
    {
        id: 's_freegrid',
        name: 'Free Grid',
        groupName: "Columns",
    },
    {
        id: 's_image_punchy',
        name: 'Image Punchy',
        groupName: "Images",
    },
];

wTourUtils.registerThemeHomepageTour("brutalist_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"brutalist"'),
    ...wTourUtils.insertSnippet(snippets[0]),
    ...wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.insertSnippet(snippets[1]),
    ...wTourUtils.insertSnippet(snippets[2]),
    ...wTourUtils.insertSnippet(snippets[3]),
    ...wTourUtils.insertSnippet(snippets[4]),
    ...wTourUtils.insertSnippet(snippets[5]),
]);
