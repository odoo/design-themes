/** @odoo-module */

import wTourUtils from 'website.tour_utils';

const snippets = [
    {
        id: 's_cover',
        name: 'Cover',
    },
    {
        id: 's_features',
        name: 'Features',
    },
    {
        id: 's_text_block',
        name: 'Text',
    },
    {
        id: 's_images_wall',
        name: 'Images Wall',
    },
    {
        id: 's_parallax',
        name: 'Parallax',
    },
    {
        id: 's_references',
        name: 'References',
    },
];

wTourUtils.registerThemeHomepageTour("nano_tour", [
    wTourUtils.dragNDrop(snippets[0]),
    wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[1]),
    wTourUtils.dragNDrop(snippets[2]),
    wTourUtils.clickOnSnippet(snippets[2], 'top'),
    wTourUtils.changeBackgroundColor(),
    wTourUtils.selectColorPalette(),
    wTourUtils.goBackToBlocks(),
    wTourUtils.dragNDrop(snippets[3]),
    wTourUtils.dragNDrop(snippets[4]),
    wTourUtils.dragNDrop(snippets[5]),
]);
