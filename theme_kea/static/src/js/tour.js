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

tour.register("kea_tour", {
    url: "/#",
    saveAs: "homepage",
}, [
    wTourUtils.dragNDrop(snippets[0]),
    wTourUtils.clickOnText(snippets[0], 'h1'),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[1]),
    wTourUtils.dragNDrop(snippets[2]),
    wTourUtils.dragNDrop(snippets[3]),
    wTourUtils.selectSnippetColumn(snippets[3]),
    wTourUtils.changeOption('Box', '[data-name="border_width_opt"]', _t('border')),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[4]),
    wTourUtils.dragNDrop(snippets[5]),
    wTourUtils.clickOnSave(),
]);
});
