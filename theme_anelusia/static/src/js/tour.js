odoo.define("theme_anelusia.tour.anelusia", function (require) {
"use strict";

const wTourUtils = require("website.tour_utils");
var tour = require("web_tour.tour");

const snippets = [
    {
        id: 's_cover',
        name: 'Cover',
    },
    {
        id: 's_images_wall',
        name: 'Images Wall',
    },
    {
        id: 's_media_list',
        name: 'Media List',
    },
    {
        id: 's_company_team',
        name: 'Team',
    },
];

wTourUtils.registerThemeHomepageTour("anelusia_tour", [
    wTourUtils.dragNDrop(snippets[0]),
    wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[1]),
    wTourUtils.dragNDrop(snippets[2], 'top'),
    wTourUtils.dragNDrop(snippets[3]),
    wTourUtils.clickOnSnippet(snippets[3], 'top'),
    wTourUtils.changeBackgroundColor(),
    wTourUtils.selectColorPalette(),
    wTourUtils.clickOnSave(),
]);
});
