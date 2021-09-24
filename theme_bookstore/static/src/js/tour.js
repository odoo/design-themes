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
        id: 's_masonry_block',
        name: 'Masonry',
    },
    {
        id: 's_image_text',
        name: 'Image - Text',
    },
    {
        id: 's_picture',
        name: 'Picture',
    },
    {
        id: 's_product_list',
        name: 'Items',
    },
    {
        id: 's_call_to_action',
        name: 'Call to Action',
    },
];

wTourUtils.registerThemeHomepageTour("bookstore_tour", [
    wTourUtils.dragNDrop(snippets[0]),
    wTourUtils.clickOnText(snippets[0], 'h1'),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[1]),
    wTourUtils.dragNDrop(snippets[2]),
    wTourUtils.dragNDrop(snippets[3]),
    wTourUtils.dragNDrop(snippets[4]),
    wTourUtils.clickOnSnippet(snippets[4]),
    wTourUtils.changeOption('ContainerWidth', 'we-button-group.o_we_user_value_widget', _t('width')),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[5]),
]);
