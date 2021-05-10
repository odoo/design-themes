odoo.define("theme_loftspace.tour.loftspace", function (require) {
"use strict";

const wTourUtils = require("website.tour_utils");
var tour = require("web_tour.tour");

const snippets = [
    {
        id: 's_cover',
        name: 'Cover',
    },
    {
        id: 's_text_image',
        name: 'Text - Image',
    },
    {
        id: 's_title',
        name: 'Title',
    },
    {
        id: 's_picture',
        name: 'Picture',
    },
    {
        id: 's_three_columns',
        name: 'Columns',
    },
    {
        id: 's_call_to_action',
        name: 'Call to Action',
    },
];

wTourUtils.registerThemeHomepageTour("loftspace_tour", [
    wTourUtils.dragNDrop(snippets[0]),
    wTourUtils.clickOnText(snippets[0], 'h1'),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[1]),
    wTourUtils.dragNDrop(snippets[2]),
    wTourUtils.dragNDrop(snippets[3]),
    wTourUtils.dragNDrop(snippets[4]),
    wTourUtils.dragNDrop(snippets[5]),
    wTourUtils.clickOnSnippet(snippets[5]),
    wTourUtils.changeBackgroundColor(),
    wTourUtils.selectColorPalette(),
    wTourUtils.clickOnSave(),
]);
});
