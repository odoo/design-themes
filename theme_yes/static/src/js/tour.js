odoo.define("theme_yes.tour.yes", function (require) {
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
        id: 's_picture',
        name: 'Picture',
    },
    {
        id: 's_masonry_block',
        name: 'Masonry',
    },
    {
        id: 's_three_columns',
        name: 'Columns',
    },
    {
        id: 's_quotes_carousel',
        name: 'Quotes',
    },
    {
        id: 's_call_to_action',
        name: 'Call to Action',
    },
];

wTourUtils.registerThemeHomepageTour("yes_tour", [
    wTourUtils.dragNDrop(snippets[0]),
    wTourUtils.clickOnText(snippets[0], 'h2'),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[1]),
    wTourUtils.dragNDrop(snippets[2]),
    wTourUtils.dragNDrop(snippets[3]),
    wTourUtils.dragNDrop(snippets[4]),
    wTourUtils.dragNDrop(snippets[5]),
    wTourUtils.clickOnSnippet(snippets[5]),
    wTourUtils.changeOption('minHeight', 'we-button-group.o_we_user_value_widget', _t('height')),
]);
});
