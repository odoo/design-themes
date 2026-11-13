/** @odoo-module */

import * as wTourUtils from '@website/js/tours/tour_utils';

const snippets = [
    {
        id: 's_intro_spotlight',
        name: 'Intro Spotlight',
        groupName: "Intro",
    },
    {
        id: 's_numbers_lite',
        name: 'Numbers Lite',
        groupName: "Content",
    },
    {
        id: 's_bento_features',
        name: 'Bento Features',
        groupName: "Content",
    },
    {
        id: 's_text_bold',
        name: 'Text Bold',
        groupName: "Text",
    },
    {
        id: 's_projects_grid',
        name: 'Projects Grid',
        groupName: "Content",
    },
    {
        id: 's_reviews_wall',
        name: 'Reviews Wall',
        groupName: "People",
    },
    {
        id: 's_cta_centered',
        name: 'Centered Call to Action',
        groupName: "Content",
    },
];

wTourUtils.registerThemeHomepageTour("seam_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"seam"'),
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
    ...wTourUtils.insertSnippet(snippets[6]),
]);
