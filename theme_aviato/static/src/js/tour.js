odoo.define("theme_aviato.tour.aviato", function (require) {
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
        id: 's_title', //3
        name: 'Title',
    },
    {
        id: 's_three_columns', //4
        name: 'Columns',
    },
    {
        id: 's_picture', //5
        name: 'Picture',
    },
];

wTourUtils.registerThemeHomepageTour("aviato_tour", [
    wTourUtils.dragNDrop(snippets[0]),
    wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[1]),
    wTourUtils.dragNDrop(snippets[2]),
    wTourUtils.dragNDrop(snippets[3]),
    wTourUtils.dragNDrop(snippets[4]),
    wTourUtils.dragNDrop(snippets[5]),
    wTourUtils.clickOnSnippet(snippets[5], 'top'),
    wTourUtils.changeOption('BackgroundShape', 'we-toggler', _t('Background Shape')),
    wTourUtils.selectNested('we-select-page', 'BackgroundShape', ':not(.o_we_pager_controls)', _t('Background Shape')),
]);
});
