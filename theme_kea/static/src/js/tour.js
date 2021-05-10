odoo.define("theme_kea.tour.kea", function (require) {
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
        id: 's_picture',
        name: 'Picture',
    },
    {
        id: 's_image_text',
        name: 'Image - Text',
    },
    {
        id: 's_three_columns',
        name: 'Columns',
    },
    {
        id: 's_media_list',
        name: 'Media List',
    },
    {
        id: 's_references',
        name: 'References',
    },
];

wTourUtils.registerThemeHomepageTour("kea_tour", [
    wTourUtils.dragNDrop(snippets[0]),
    wTourUtils.clickOnText(snippets[0], 'h1'),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[1]),
    wTourUtils.dragNDrop(snippets[2]),
    wTourUtils.dragNDrop(snippets[3]),
    wTourUtils.clickOnSnippet(snippets[3]),
    wTourUtils.changeOption('ContainerWidth', 'we-button-group.o_we_user_value_widget', _t('width')),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[4]),
    wTourUtils.dragNDrop(snippets[5]),
    wTourUtils.clickOnSave(),
]);
});
