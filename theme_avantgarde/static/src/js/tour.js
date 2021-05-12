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
        id: 's_image_gallery',
        name: 'Images Wall',
    },
    {
        id: 's_references',
        name: 'References',
    },
    {
        id: 's_quotes_carousel',
        name: 'Quotes',
    },
    {
        id: 's_text',
        name: 'Text',
    },
];

tour.register("avantgarde_tour", {
    url: "/",
    saveAs: "homepage",
}, [
    wTourUtils.dragNDrop(snippets[0], 'right'),
    wTourUtils.clickOnText(snippets[0], 'h1', 'left'),
    wTourUtils.goBackToBlocks(),

    wTourUtils.dragNDrop(snippets[1], 'left'),

    wTourUtils.dragNDrop(snippets[2], 'right'),
    wTourUtils.clickOnSnippet(snippets[2], 'top'),
    wTourUtils.changeBackgroundColor('right'),
    wTourUtils.goBackToBlocks(),

    wTourUtils.dragNDrop(snippets[3], 'right'),
    wTourUtils.addMedia(),

    wTourUtils.dragNDrop(snippets[4], 'top'),
    wTourUtils.dragNDrop(snippets[5], 'top'),
    wTourUtils.dragNDrop(snippets[6], 'top'),
    wTourUtils.clickOnSave(),
]);
});
