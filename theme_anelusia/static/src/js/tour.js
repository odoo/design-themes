/** @odoo-module */

import * as wTourUtils from '@website/js/tours/tour_utils';

const snippets = [
    {
        id: 's_splash_intro',
        name: 'Splash Intro',
        groupName: "Intro",
    },
    {
        id: 's_announcement_scroll',
        name: 'Announcement Scroll',
        groupName: "Catalog",
    },
    {
        id: 's_bento_grid',
        name: 'Bento Grid',
        groupName: "Catalog",
    },
    {
        id: 's_ecomm_categories_showcase',
        name: 'Categories Showcase',
        groupName: "Catalog",
    },
    {
        id: 's_reviews_wall',
        name: 'Reviews Wall',
        groupName: "People",
    },
    {
        id: 's_cta_box',
        name: 'Box Call to Action',
        groupName: "Content",
    },
];

wTourUtils.registerThemeHomepageTour("anelusia_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"default-25"'),
    ...wTourUtils.insertSnippet(snippets[0]),
    ...wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.insertSnippet(snippets[1]),
    ...wTourUtils.insertSnippet(snippets[2], 'top'),
    ...wTourUtils.insertSnippet(snippets[3]),
    ...wTourUtils.insertSnippet(snippets[4]),
    ...wTourUtils.clickOnSnippet(snippets[4], 'top'),
    wTourUtils.changeBackgroundColor(),
    wTourUtils.selectColorPalette(),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.insertSnippet(snippets[5]),
]);
