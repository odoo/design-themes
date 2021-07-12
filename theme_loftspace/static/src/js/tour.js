odoo.define("theme_loftspace.tour.loftspace", function (require) {
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
        id: 's_three_columns',
        name: 'Columns',
    },
    {
        id: 's_title',
        name: 'Title',
    },
    {
        id: 's_image_gallery',
        name: 'Images Wall',
    },    
    {
        id: 's_call_to_action',
        name: 'Call to Action',
    },
];

wTourUtils.registerThemeHomepageTour("loftspace_tour", [
    wTourUtils.clickOnEdit(),
    wTourUtils.selectHeader(),
    wTourUtils.changeOption('TopMenuVisibility', '.o_we_user_value_widget', _t('Header Position')),
    wTourUtils.selectNested('.o_we_user_value_widget[data-visibility="transparent"]', 'TopMenuVisibility', null, _t('position'), 'left'),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[0]),
    wTourUtils.clickOnText(snippets[0], 'h1'),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[1]),
    wTourUtils.dragNDrop(snippets[2]),
    wTourUtils.dragNDrop(snippets[3]),
    wTourUtils.dragNDrop(snippets[4]),
    wTourUtils.clickOnSnippet(snippets[4]),
    wTourUtils.changeBackgroundColor(),
    wTourUtils.selectColorPalette(),
]);
});
