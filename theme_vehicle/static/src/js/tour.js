odoo.define("theme_vehicle.tour.vehicle", function (require) {
"use strict";

const core = require("web.core");
const _t = core._t;

const wTourUtils = require("website.tour_utils");
var tour = require("web_tour.tour");

const snippets = [
    {
        id: 's_cover', //0
        name: 'Cover',
    },
    {
        id: 's_text_image', //1
        name: 'Text - Image',
    },
    {
        id: 's_image_text', //2
        name: 'Image - Text',
    },
    {
        id: 's_picture', //3
        name: 'Picture',
    },
    {
        id: 's_masonry_block', //4
        name: 'Masonry',
    },
    {
        id: 's_call_to_action', //5
        name: 'Call to Action',
    },
];

wTourUtils.registerThemeHomepageTour("vehicle_tour", [
    wTourUtils.dragNDrop(snippets[0], 'top'),
    wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[1], 'top'),
    wTourUtils.dragNDrop(snippets[2], 'top'),
    wTourUtils.dragNDrop(snippets[3], 'top'),
    wTourUtils.dragNDrop(snippets[4], 'top'),
    wTourUtils.dragNDrop(snippets[5], 'top'),
    wTourUtils.clickOnSnippet(snippets[5]),
    wTourUtils.changeBackgroundColor(),
    wTourUtils.selectColorPalette(),
]);
});
