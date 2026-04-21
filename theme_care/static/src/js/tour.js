/** @odoo-module */

import * as wTourUtils from '@website/js/tours/tour_utils';

const snippets = [
    {
        id: 's_splash_intro',
        name: 'Splash Intro',
        groupName: "Intro",
    },
    {
        id: 's_text_block',
        name: 'Text Block',
        groupName: "Text",
    },
    {
        id: 's_numbers',
        name: 'Numbers',
        groupName: "Content",
    },
    {
        id: 's_floating_blocks',
        name: 'Floating Cards',
        groupName: "Catalog",
    },
    {
        id: 's_text_image',
        name: 'Text - Image',
        groupName: "Content",
    },
    {
        id: 's_company_team_grid',
        name: 'Team Grid',
        groupName: "People",
    },
    {
        id: 's_masonry_block_default_template',
        name: 'Masonry',
        groupName: "Images",
    },
    {
        id: 's_reviews_wall',
        name: 'Reviews Wall',
        groupName: "People",
    },
    {
        id: 's_faq_collapse',
        name: 'FAQ Collapse',
        groupName: "Text",
    },
    {
        id: 's_cta_box',
        name: 'CTA Box',
        groupName: "Content",
    },
];

wTourUtils.registerThemeHomepageTour("care_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"care-1"'),
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
    ...wTourUtils.insertSnippet(snippets[8]),
    ...wTourUtils.insertSnippet(snippets[9]),
]);
