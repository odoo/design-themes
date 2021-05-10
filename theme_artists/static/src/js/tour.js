odoo.define("theme_artists.tour.artists", function (require) {
"use strict";

const core = require("web.core");
const _t = core._t;
const wTourUtils = require("website.tour_utils");
var tour = require("web_tour.tour");

const snippets = [
    {
        id: 's_parallax',
        name: 'Parallax',
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
    wTourUtils.clickOnSnippet(snippets[3]),
    wTourUtils.changeOption('minHeight', 'we-button-group.o_we_user_value_widget', _t('height')),
    wTourUtils.clickOnSave(),
]);
});
