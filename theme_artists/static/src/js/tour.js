/** @odoo-module */

import * as wTourUtils from '@website/js/tours/tour_utils';

const snippets = [
    {
        id: 's_sidegrid',
        name: 'Side Grid',
        groupName: "Intro",
    },
    {
        id: 's_product_catalog',
        name: 'Product Catalog',
        groupName: "Content",
    },
    {
        id: 's_cta_box',
        name: 'Box Call to Action',
        groupName: "Content",
    },
    {
        id: 's_title',
        name: 'Title',
        groupName: "Text",
    },
    {
        id: 's_image_frame',
        name: 'Image Frame',
        groupName: "Images",
    },
    {
        id: 's_images_wall',
        name: 'Images Wall',
        groupName: "Images",
    },
    {
        id: 's_shape_image',
        name: 'Shape Image',
        groupName: "Images",
    },
];

wTourUtils.registerThemeHomepageTour("artists_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"artists-1"'),
    ...wTourUtils.dragNDrop(snippets[0], 'top'),
    ...wTourUtils.dragNDrop(snippets[1]),
    ...wTourUtils.clickOnText(snippets[1], 'h2'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.dragNDrop(snippets[2]),
    ...wTourUtils.dragNDrop(snippets[3]),
    ...wTourUtils.clickOnText(snippets[3], 'h2'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.dragNDrop(snippets[4]),
    ...wTourUtils.dragNDrop(snippets[5]),
    ...wTourUtils.dragNDrop(snippets[6]),
]);
