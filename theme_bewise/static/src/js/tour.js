odoo.define("theme_bewise.tour.bewise", function (require) {
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
        id: 's_call_to_action',
        name: 'Call to Action',
    },
    {
        id: 's_text_image',
        name: 'Text - Image',
    },
    {
        id: 's_numbers',
        name: 'Numbers',
    },
    {
        id: 's_image_text',
        name: 'Image - Text',
    },
    {
        id: 's_quotes_carousel_wrapper',
        name: 'Quotes',
    },
    {
        id: 's_company_team',
        name: 'Team',
    },
];

wTourUtils.registerThemeHomepageTour("bewise_tour", [
    wTourUtils.dragNDrop(snippets[0], 'top'),
    wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[1], 'top'),
    wTourUtils.dragNDrop(snippets[2], 'top'),
    wTourUtils.dragNDrop(snippets[3], 'top'),
    wTourUtils.dragNDrop(snippets[4], 'top'),
    wTourUtils.dragNDrop(snippets[5], 'top'),
    wTourUtils.dragNDrop(snippets[6], 'top'),
    wTourUtils.clickOnSnippet(snippets[6], 'top'),
    wTourUtils.changeOption('BackgroundShape', 'we-toggler', _t('Background Shape')),
    wTourUtils.selectNested('we-select-page', 'BackgroundShape', ':not(.o_we_pager_controls)', _t('Background Shape')),
    wTourUtils.clickOnSave(),
]);
});
