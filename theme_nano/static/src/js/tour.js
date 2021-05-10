odoo.define("theme_nano.tour.nano", function (require) {
"use strict";

const wTourUtils = require("website.tour_utils");
var tour = require("web_tour.tour");

const snippets = [
    {
        id: 's_carousel',
        name: 'Carousel',
    },
    {
        id: 's_features',
        name: 'Features',
    },
    {
        id: 's_image_text',
        name: 'Image - Text',
    },
    {
        id: 's_text_block',
        name: 'Text',
    },
    {
        id: 's_three_columns',
        name: 'Columns',
    },
];

wTourUtils.registerThemeHomepageTour("nano_tour", [
    wTourUtils.dragNDrop(snippets[0]),
    wTourUtils.clickOnText(snippets[0], 'h2', 'top'),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[1]),
    wTourUtils.dragNDrop(snippets[2]),
    wTourUtils.dragNDrop(snippets[3]),
    wTourUtils.dragNDrop(snippets[4]),
    wTourUtils.clickOnSnippet(snippets[4], 'top'),
    wTourUtils.changeBackgroundColor(),
    wTourUtils.selectColorPalette(),
    wTourUtils.clickOnSave(),
]);
});
