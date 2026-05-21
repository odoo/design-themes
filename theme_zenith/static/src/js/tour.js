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
        name: 'Freegrid',
        groupName: "Images",
    },
    {
        id: 's_title',
        name: 'Title',
        groupName: "Text",
    },
    {
        id: 's_floating_blocks',
        name: 'Floating Blocks',
        groupName: "Images",
    },
    {
        id: 's_announcement_scroll',
        name: 'Announcement Scroll',
        groupName: "Content",
    },
    {
        id: 's_numbers_inline',
        name: 'Numbers Inline',
        groupName: "Content",
    },
    {
        id: 's_company_team_spotlight',
        name: 'Team Spotlight',
        groupName: "People",
    },
    {
        id: 's_comparisons',
        name: 'Comparisons',
        groupName: "Content",
    },
    {
        id: 's_faq_collapse',
        name: 'FAQ',
        groupName: "Text",
    },
];

wTourUtils.registerThemeHomepageTour("zenith_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"zenith"'),
    ...wTourUtils.insertSnippet(snippets[0]),
    ...wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.insertSnippet(snippets[1]),
    ...wTourUtils.insertSnippet(snippets[2]),
    ...wTourUtils.insertSnippet(snippets[3]),
    ...wTourUtils.insertSnippet(snippets[4]),
    ...wTourUtils.insertSnippet(snippets[5]),
    ...wTourUtils.insertSnippet(snippets[6]),
    ...wTourUtils.clickOnSnippet(snippets[6], 'top'),
    wTourUtils.changeBackgroundColor(),
    wTourUtils.selectColorPalette(),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.insertSnippet(snippets[7]),
    ...wTourUtils.insertSnippet(snippets[8]),
]);
