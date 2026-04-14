/** @odoo-module */

import * as wTourUtils from '@website/js/tours/tour_utils';

const snippets = [
    {
        id: 's_discovery',
        name: 'Discovery',
        groupName: "Intro",
    },
    {
        id: 's_freegrid',
        name: 'Free grid',
        groupName: "Columns",
    },
    {
        id: 's_image_text_overlap',
        name: 'Image - Text Overlap',
        groupName: "Content",
    },
    {
        id: 's_process_steps',
        name: 'Steps',
        groupName: "Content",
    },
    {
        id: 's_bento_grid',
        name: 'Bento Grid',
        groupName: "Catalog",
    },
    {
        id: 's_reviews_wall',
        name: 'Reviews Wall',
        groupName: "People",
    },
    {
        id: 's_attributes_horizontal',
        name: 'Horizontal Attributes',
        groupName: "Catalog",
    },
    {
        id: 's_faq_collapse',
        name: 'FAQ Block',
        groupName: "Text",
    },
];

wTourUtils.registerThemeHomepageTour("pawtastic_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', 'default-light-14'),
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
