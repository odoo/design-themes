odoo.define("theme_graphene.tour.graphene", function (require) {
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
        id: 's_text_image',
        name: 'Text - Image',
    },
    {
        id: 's_three_columns',
        name: 'Columns',
    },
    {
        id: 's_company_team',
        name: 'Team',
    },
    {
        id: 's_call_to_action',
        name: 'Call to Action',
    },
    {
        id: 's_comparisons',
        name: 'Comparisons',
    },
];


tour.register("graphene_tour", {
    url: "/",
    saveAs: "homepage",
}, [
    wTourUtils.dragNDrop(snippets[0]),
    wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks('right'),

    wTourUtils.dragNDrop(snippets[1]),
    wTourUtils.changeImage(snippets[1], 'left'),
    wTourUtils.goBackToBlocks('right'),

    wTourUtils.dragNDrop(snippets[2]),
    wTourUtils.dragNDrop(snippets[3], 'top'),

    wTourUtils.dragNDrop(snippets[4], 'top'),
    wTourUtils.clickOnSnippet(snippets[4], 'top'),
    wTourUtils.changeBackgroundColor('right'),
    wTourUtils.goBackToBlocks('right'),

    wTourUtils.dragNDrop(snippets[5]),
    wTourUtils.clickOnSnippet(snippets[5], 'top'),
    wTourUtils.changeOption('ColoredLevelBackground', 'Shape', _t('Shape')),
    wTourUtils.changeOption('BackgroundShape', 'we-toggler', _t('Background Shape')),

    wTourUtils.clickOnSave(),
]);
});
