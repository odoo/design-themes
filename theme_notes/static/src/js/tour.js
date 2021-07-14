odoo.define("theme_notes.tour.notes", function (require) {
"use strict";

const core = require("web.core");
const _t = core._t;
const wTourUtils = require("website.tour_utils");
var tour = require("web_tour.tour");

const snippets = [
    {
        id: 's_carousel',
        name: 'Carousel',
    },
    {
        id: 's_masonry_block',
        name: 'Masonry',
    },
    {
        id: 's_text_image',
        name: 'Text - Image',
    },
    {
        id: 's_product_catalog',
        name: 'Pricelist',
    },
    {
        id: 's_media_list',
        name: 'Media List',
    },
    {
        id: 's_title',
        name: 'Title',
    },
    {
        id: 's_company_team',
        name: 'Team',
    },
];

wTourUtils.registerThemeHomepageTour("notes_tour", [
    wTourUtils.dragNDrop(snippets[0]),
    wTourUtils.clickOnText(snippets[0], 'h2'),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[1]),
    wTourUtils.dragNDrop(snippets[2]),
    wTourUtils.dragNDrop(snippets[3]),
    wTourUtils.dragNDrop(snippets[4]),
    wTourUtils.dragNDrop(snippets[5]),
    wTourUtils.clickOnText(snippets[5], 'h1'),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[6]),
]);
});
