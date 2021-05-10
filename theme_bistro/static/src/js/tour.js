odoo.define("theme_bistro.tour.bistro", function (require) {
"use strict";

const wTourUtils = require("website.tour_utils");
var tour = require("web_tour.tour");

const snippets = [
    {
        id: 's_cover',
        name: 'Cover',
    },
    {
        id: 's_features',
        name: 'Features',
    },
    {
        id: 's_picture',
        name: 'Picture',
    },
    {
        id: 's_product_catalog',
        name: 'Pricelist',
    },
    {
        id: 's_text_block',
        name: 'Text',
    },
    {
        id: 's_quotes_carousel',
        name: 'Quotes',
    },
];

wTourUtils.registerThemeHomepageTour("bistro_tour", [
    wTourUtils.dragNDrop(snippets[0]),
    wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[1]),
    wTourUtils.dragNDrop(snippets[2]),
    wTourUtils.dragNDrop(snippets[3]),
    wTourUtils.dragNDrop(snippets[4]),
    wTourUtils.dragNDrop(snippets[5]),
    wTourUtils.clickOnSnippet(snippets[5], 'top'),
    wTourUtils.changeBackgroundColor(),
    wTourUtils.selectColorPalette(),
    wTourUtils.clickOnSave(),
]);
});
