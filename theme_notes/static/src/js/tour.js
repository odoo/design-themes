odoo.define("theme_notes.tour.notes", function (require) {
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
        id: 's_image_text',
        name: 'Image - Text',
    },
    {
        id: 's_media_list',
        name: 'Media List',
    },
    {
        id: 's_company_team',
        name: 'Team',
    },
];

wTourUtils.registerThemeHomepageTour("notes_tour", [
    wTourUtils.dragNDrop(snippets[0]),
    wTourUtils.clickOnText(snippets[0], 'h2'),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[1]),
    wTourUtils.dragNDrop(snippets[2]),
    wTourUtils.dragNDrop(snippets[3]),
    wTourUtils.clickOnSnippet(snippets[3]),
    wTourUtils.changeOption('ContainerWidth', 'we-button-group.o_we_user_value_widget', _t('width')),
    wTourUtils.clickOnSave(),
]);
});
