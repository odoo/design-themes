odoo.define("theme_cobalt.tour.cobalt", function (require) {
"use strict";

const core = require("web.core");
const _t = core._t;

const wTourUtils = require("website.tour_utils");
var tour = require("web_tour.tour");

const snippets = [
    {
        id: 's_text_image',
        name: 'Image - Text',
    },
    {
        id: 's_references',
        name: 'References',
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
        id: 's_picture',
        name: 'Picture',
    },
];


tour.register("cobalt_tour", {
    url: "/#",
    saveAs: "homepage",
}, [
    wTourUtils.dragNDrop(snippets[0]),

    wTourUtils.selectHeader(),
    wTourUtils.changeOption('TopMenuVisibility', 'we-toggler', _t('transparency')),
    wTourUtils.goBackToBlocks(),

    wTourUtils.dragNDrop(snippets[1]),
    wTourUtils.dragNDrop(snippets[2]),
    wTourUtils.dragNDrop(snippets[3]),

    wTourUtils.dragNDrop(snippets[4]),
    wTourUtils.clickOnSnippet(snippets[4], 'top'),
    wTourUtils.changeOption('BackgroundShape', 'we-toggler', _t('Background Shape')),

    wTourUtils.clickOnSave(),
]);
});
