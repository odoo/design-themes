odoo.define("theme_odoo_experts.tour.odoo_experts", function (require) {
"use strict";

const core = require("web.core");
const _t = core._t;
const wTourUtils = require("website.tour_utils");
var tour = require("web_tour.tour");

const snippets = [
    {
        id: 's_banner',
        name: 'Banner',
    },
    {
        id: 's_image_text',
        name: 'Image - Text',
    },
    {
        id: 's_media_list',
        name: 'Media List',
    },
    {
        id: 's_call_to_action',
        name: 'Call to Action',
    },
];

wTourUtils.registerThemeHomepageTour("odoo_experts_tour", [
    wTourUtils.dragNDrop(snippets[0]),
    wTourUtils.clickOnText(snippets[0], 'h1'),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[1]),
    wTourUtils.dragNDrop(snippets[2]),
    wTourUtils.dragNDrop(snippets[3]),
    wTourUtils.clickOnSnippet(snippets[3]),
    wTourUtils.changeOption('minHeight', 'we-button-group.o_we_user_value_widget', _t('height')),
    wTourUtils.clickOnSave(),
]);
});
