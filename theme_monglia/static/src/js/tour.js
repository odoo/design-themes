/** @odoo-module */

import * as wTourUtils from '@website/js/tours/tour_utils';

const snippets = [
    {
        id: 's_cover',
        name: 'Cover',
        groupName: "Intro",
    },
    {
        id: 's_numbers_grid',
        name: 'Numbers Grid',
        groupName: "Content",
    },
    {
        id: 's_company_team_shapes',
        name: 'Team Shapes',
        groupName: "People",
    },
    {
        id: 's_text_block',
        name: 'Text',
        groupName: "Text",
    },
    {
        id: 's_freegrid',
        name: 'Free grid',
        groupName: "Columns",
    },
    {
        id: 's_cta_box',
        name: 'Box Call to Action',
        groupName: "Content",
    },
    {
        id: 's_shape_image',
        name: 'Shape image',
        groupName: "Content",
    },
    {
        id: 's_title',
        name: 'Title',
        groupName: "Text",
    },
    {
        id: 's_images_wall',
        name: 'Images Wall',
        groupName: "Images",
    },
    {
        id: 's_faq_collapse',
        name: 'FAQ',
        groupName: "text",
    },
    {
        id: 's_references',
        name: 'References',
        groupName: "People",
    },
];

wTourUtils.registerThemeHomepageTour("monglia_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"default-light-3"'),
    ...wTourUtils.dragNDrop(snippets[0]),
    ...wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.dragNDrop(snippets[1]),
    ...wTourUtils.dragNDrop(snippets[2]),
    ...wTourUtils.dragNDrop(snippets[3]),
    ...wTourUtils.dragNDrop(snippets[4]),
    ...wTourUtils.dragNDrop(snippets[5]),
    ...wTourUtils.dragNDrop(snippets[6]),
    ...wTourUtils.dragNDrop(snippets[7]),
    ...wTourUtils.dragNDrop(snippets[8]),
    ...wTourUtils.dragNDrop(snippets[9]),
    ...wTourUtils.dragNDrop(snippets[10]),
]);
