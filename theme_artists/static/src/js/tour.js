odoo.define("theme_artists.tour.artists", function (require) {
"use strict";

const core = require("web.core");
const _t = core._t;
const wTourUtils = require("website.tour_utils");
var tour = require("web_tour.tour");

const snippets = [
    {
        id: 's_carousel_wrapper',
        name: 'Carousel',
    },
    {
        id: 's_text_image',
        name: 'Text - Image',
    },
    {
        id: 's_three_columns',
        name: 'Columns',
    },
    {
        id: 's_title',
        name: 'Title',
    },
    {
        id: 's_image_gallery',
        name: 'Images Wall',
    },
    {
        id: 's_call_to_action',
        name: 'Call to Action',
    },
];

wTourUtils.registerThemeHomepageTour("artists_tour", [
    wTourUtils.dragNDrop(snippets[0], 'top'),
    wTourUtils.dragNDrop(snippets[1]),
    wTourUtils.clickOnText(snippets[1], 'h2'),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[2]),
    wTourUtils.dragNDrop(snippets[3]),
    wTourUtils.clickOnText(snippets[3], 'h1'),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[4]),
    wTourUtils.dragNDrop(snippets[5]),
]);
});
