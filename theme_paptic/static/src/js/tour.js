odoo.define("theme_paptic.tour.paptic", function (require) {
"use strict";

const core = require("web.core");
const _t = core._t;

const wTourUtils = require("website.tour_utils");
var tour = require("web_tour.tour");

const snippets = [
    {
        id: 's_cover',
        name: 'Cover',
    },
    {
        id: 's_image_text',
        name: 'Image - Text',
    },
    {
        id: 's_references',
        name: 'References',
    },
    {
        id: 's_three_columns',
        name: 'Columns',
    },
];


wTourUtils.registerThemeHomepageTour("paptic_tour", [
    wTourUtils.dragNDrop(snippets[0], 'top'),
    wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks(),

    wTourUtils.dragNDrop(snippets[1], 'top'),
    wTourUtils.dragNDrop(snippets[2], 'top'),
    wTourUtils.dragNDrop(snippets[3], 'top'),
    wTourUtils.clickOnSave(),
]);
});
