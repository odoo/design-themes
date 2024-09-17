/** @odoo-module */
import * as wTourUtils from '@website/js/tours/tour_utils';

const snippets = [
    {
        id: 's_sidegrid',
        name: 'Sidegrid',
        groupName: "Intro",
    },
    {
        id: 's_features_wall',
        name: 'Features Wall',
        groupName: "Columns",
    },
    {
        id: 's_masonry_block',
        name: 'Masonry',
        groupName: "Images",
    },
    {
        id: 's_carousel',
        name: 'Carousel',
        groupName: "Intro",
    },
    {
        id: 's_timeline',
        name: 'Timeline',
        groupName: "Content",
    },
    {
        id: 's_quadrant',
        name: 'Quadrant',
        groupName: "Images",
    },
];

wTourUtils.registerThemeHomepageTour("avantgarde_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"default-15"'),
    ...wTourUtils.dragNDrop(snippets[0], 'top'),
    ...wTourUtils.clickOnText(snippets[0], 'h1', 'left'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.dragNDrop(snippets[1], 'left'),
    ...wTourUtils.dragNDrop(snippets[2], 'bottom'),
    ...wTourUtils.clickOnSnippet(snippets[2], 'top'),
    wTourUtils.changePaddingSize('top'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.dragNDrop(snippets[3], 'top'),
    ...wTourUtils.dragNDrop(snippets[4], 'top'),
    ...wTourUtils.dragNDrop(snippets[5], 'top'),
]);
