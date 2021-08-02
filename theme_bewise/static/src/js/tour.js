/** @odoo-module */
import wTourUtils from 'website.tour_utils';

const core = require("web.core");
const _t = core._t;

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
        id: 's_color_blocks_2',
        name: 'Big Boxes',
    },
];

wTourUtils.registerThemeHomepageTour("bewise_tour", [
    wTourUtils.dragNDrop(snippets[0], 'top'),
    wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[1], 'top'),
    wTourUtils.dragNDrop(snippets[2], 'top'),
    wTourUtils.dragNDrop(snippets[3], 'top'),
    wTourUtils.clickOnSnippet(snippets[3], 'top'),
    wTourUtils.changeOption('BackgroundShape', 'we-toggler', _t('Background Shape')),
    wTourUtils.selectNested('we-select-page', 'BackgroundShape', ':not(.o_we_pager_controls)', _t('Background Shape')),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[4], 'top'),
    wTourUtils.dragNDrop(snippets[5], 'top'),
    wTourUtils.dragNDrop(snippets[6], 'top'),
]);
