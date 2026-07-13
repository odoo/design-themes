/** @odoo-module */

import * as wTourUtils from '@website/js/tours/tour_utils';

const snippets = [
    {
        id: 's_animated_cover',
        name: 'Animated Cover',
        groupName: "Intro",
    },
    {
        id: 's_about_bold',
        name: 'About Bold',
        groupName: "Columns",
    },
    {
        id: 's_references_tiles',
        name: 'References Tiles',
        groupName: "People",
    },
    {
        id: 's_manifesto',
        name: 'Manifesto',
        groupName: "Content",
    },
    {
        id: 's_projects_grid_minimal',
        name: 'Projects Grid Minimal',
        groupName: "Content",
    },
    {
        id: 's_reviews_wall',
        name: 'Reviews Wall',
        groupName: "People",
    },
    {
        id: 's_faq_collapse_centered',
        name: 'FAQ Centered',
        groupName: "Text",
    },
    {
        id: 's_cta_centered',
        name: 'Centered Call to Action',
        groupName: "Content",
    },
];

wTourUtils.registerThemeHomepageTour("muse_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"muse"'),
    ...wTourUtils.insertSnippet(snippets[0]),
    ...wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.insertSnippet(snippets[1]),
    ...wTourUtils.insertSnippet(snippets[2]),
    ...wTourUtils.insertSnippet(snippets[3]),
    ...wTourUtils.insertSnippet(snippets[4]),
    ...wTourUtils.insertSnippet(snippets[5]),
    ...wTourUtils.insertSnippet(snippets[6]),
    ...wTourUtils.insertSnippet(snippets[7]),
]);
