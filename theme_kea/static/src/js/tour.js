/** @odoo-module */

import * as wTourUtils from '@website/js/tours/tour_utils';

const snippets = [
    {
        id: 's_banner_glow',
        name: 'Banner Glow',
        groupName: "Intro",
    },
    {
        id: 's_attributes_horizontal',
        name: 'Horizontal Attributes',
        groupName: "Catalog",
    },
    {
        id: 's_cards_soft',
        name: 'Cards Soft',
        groupName: "Columns",
    },
    {
        id: 's_announcement_scroll',
        name: 'Announcement Scroll',
        groupName: "Catalog",
    },
    {
        id: 's_card_offset',
        name: 'Card Offset',
        groupName: "Images",
    },
    {
        id: 's_process_steps',
        name: 'Steps',
        groupName: "Content",
    },
    {
        id: 's_title',
        name: 'Title',
        groupName: "Text",
    },
    {
        id: 's_bento_grid',
        name: 'Bento Grid',
        groupName: "Catalog",
    },
    {
        id: 's_opening_hours',
        name: 'Opening Hours',
        groupName: "Contact & Forms",
    },
];

wTourUtils.registerThemeHomepageTour("kea_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"kea"'),
    ...wTourUtils.insertSnippet(snippets[0]),
    ...wTourUtils.clickOnText(snippets[0], 'h1'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.insertSnippet(snippets[1]),
    ...wTourUtils.insertSnippet(snippets[2]),
    ...wTourUtils.insertSnippet(snippets[3]),
    ...wTourUtils.insertSnippet(snippets[4]),
    ...wTourUtils.insertSnippet(snippets[5]),
    ...wTourUtils.insertSnippet(snippets[6]),
    ...wTourUtils.clickOnSnippet(snippets[6], 'top'),
    wTourUtils.changeBackgroundColor(),
    wTourUtils.selectColorPalette(),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.insertSnippet(snippets[7]),
    ...wTourUtils.insertSnippet(snippets[8]),
]);
