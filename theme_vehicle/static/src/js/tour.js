/** @odoo-module **/

import * as wTourUtils from "@website/js/tours/tour_utils";

const snippets = [
    {
        id: 's_cover',
        name: 'Cover',
        groupName: "Intro",
    },
    {
        id: 's_title',
        name: 'Title',
        groupName: "Text",
    },
    {
        id: 's_three_columns',
        name: 'Columns',
        groupName: "Columns",
    },
    {
        id: 's_picture',
        name: 'Title - Image',
        groupName: "Images",
    },
    {
        id: 's_key_images',
        name: 'Key Images',
        groupName: "Columns",
    },
    {
        id: 's_numbers_charts',
        name: 'Numbers Charts',
        groupName: "Content",
    },
    {
        id: 's_media_list',
        name: 'Media List',
        groupName: "Content",
    },
];

wTourUtils.registerThemeHomepageTour("vehicle_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"vehicle-1"'),
    ...wTourUtils.dragNDrop(snippets[0]),
    ...wTourUtils.dragNDrop(snippets[1]),
    ...wTourUtils.dragNDrop(snippets[2]),
    ...wTourUtils.dragNDrop(snippets[3]), 
    ...wTourUtils.dragNDrop(snippets[4]),
    ...wTourUtils.dragNDrop(snippets[5]),
    ...wTourUtils.dragNDrop(snippets[6]),
]);
