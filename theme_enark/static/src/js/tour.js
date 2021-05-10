odoo.define("theme_enark.tour.enark", function (require) {
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
        id: 's_picture',
        name: 'Picture',
    },
    {
        id: 's_text_image',
        name: 'Text - Image',
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

wTourUtils.registerThemeHomepageTour("enark_tour", [
    wTourUtils.dragNDrop(snippets[0]),
    wTourUtils.clickOnText(snippets[0], 'h1'),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[1]),
    wTourUtils.dragNDrop(snippets[2]),
    wTourUtils.dragNDrop(snippets[3]),
    wTourUtils.dragNDrop(snippets[4]),
    wTourUtils.clickOnSnippet(snippets[4]),
    wTourUtils.changeOption('minHeight', 'we-button-group.o_we_user_value_widget', _t('height')),
    wTourUtils.clickOnSave(),
]);
});
