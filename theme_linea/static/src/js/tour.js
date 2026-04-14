/** @odoo-module */

import * as wTourUtils from '@website/js/tours/tour_utils';

const snippets = [
    {
        id: 's_banner_product',
        name: 'Collection Banner',
        groupName: "Catalog",
    },
    {
        id: 's_title',
        name: 'Title',
        groupName: "Text",
    },
    {
        id: 's_ecomm_categories_showcase',
        name: 'Categories Grid',
        groupName: "Catalog",
    },
    {
        id: 's_masonry_block_images_template',
        name: 'Masonry',
        groupName: "Images",
    },
    {
        id: 's_announcement_scroll',
        name: 'Announcement Scroll',
        groupName: "Catalog",
    },
    {
        id: 's_image_title',
        name: 'Image Title',
        groupName: "Images",
    },
    {
        id: 's_references_lite',
        name: 'References Lite',
        groupName: "People",
    },
    {
        id: 's_opening_hours_alt',
        name: 'Opening Hours Alt',
        groupName: "Contact & Forms",
    },
];

wTourUtils.registerThemeHomepageTour("boilerplate_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"default-light-13"'),
    ...wTourUtils.insertSnippet(snippets[0]),
    ...wTourUtils.clickOnText(snippets[0], 'h2', 'top'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.insertSnippet(snippets[1]),
    ...wTourUtils.insertSnippet(snippets[2]),
    ...wTourUtils.insertSnippet(snippets[3]),
    ...wTourUtils.insertSnippet(snippets[4]),
    ...wTourUtils.insertSnippet(snippets[5]),
    ...wTourUtils.insertSnippet(snippets[6]),
    ...wTourUtils.insertSnippet(snippets[7]),
]);
