odoo.define("theme_avantgarde.tour.avantgarde", function (require) {
"use strict";

const wTourUtils = require("website.tour_utils");
var tour = require("web_tour.tour");

const snippets = [
    {
        id: 's_title',
        name: 'Title',
    },
    {
        id: 's_carousel',
        name: 'Carousel',
    },
    {
        id: 's_text_image',
        name: 'Image - Text',
    },
    {
        id: 's_references',
        name: 'References',
    },
    {
        id: 's_quotes_carousel',
        name: 'Quotes',
    },
];

wTourUtils.registerThemeHomepageTour("avantgarde_tour", [
    wTourUtils.dragNDrop(snippets[0], 'top'),
    wTourUtils.clickOnText(snippets[0], 'h1', 'left'),
    wTourUtils.goBackToBlocks(),

    wTourUtils.dragNDrop(snippets[1], 'left'),

    wTourUtils.dragNDrop(snippets[2], 'bottom'),
    wTourUtils.clickOnSnippet(snippets[2], 'top'),
    wTourUtils.changeBackgroundColor('top'),
    wTourUtils.selectColorPalette(),
    wTourUtils.goBackToBlocks(),

    wTourUtils.dragNDrop(snippets[3], 'top'),

    wTourUtils.dragNDrop(snippets[4], 'top'),
    wTourUtils.clickOnSave(),
]);
});
