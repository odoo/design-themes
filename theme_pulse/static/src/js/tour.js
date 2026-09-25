/** @odoo-module */

import * as wTourUtils from '@website/js/tours/tour_utils';

const snippets = [
    {
        id: 's_confidence',
        name: 'Confidence Hero',
        groupName: "Intro",
    },
    {
        id: 's_features_box',
        name: 'Features Box',
        groupName: "Content",
    },
    {
        id: 's_text_bold',
        name: 'Text Bold',
        groupName: "Text",
    },
    {
        id: 's_features_grid',
        name: 'Features Grid',
        groupName: "Content",
    },
    {
        id: 's_founder',
        name: 'Founder',
        groupName: "People",
    },
    {
        id: 's_achievements_list',
        name: 'Achievements List',
        groupName: "Text",
    },
    {
        id: 's_bento_features',
        name: 'Bento Features',
        groupName: "Content",
    },
    {
        id: 's_references_tiles',
        name: 'References Tiles',
        groupName: "People",
    },
    {
        // Inner content snippet: no groupName, it is dragged from #snippet_content.
        id: 's_blockquote',
        name: 'Blockquote',
    },
];

wTourUtils.registerThemeHomepageTour("pulse_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"pulse"'),
    ...wTourUtils.insertSnippet(snippets[0]),
    ...wTourUtils.clickOnText(snippets[0], 'h1', 'top'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.insertSnippet(snippets[1]),
    ...wTourUtils.insertSnippet(snippets[2]),
    ...wTourUtils.insertSnippet(snippets[3]),
    ...wTourUtils.insertSnippet(snippets[4]),
    ...wTourUtils.insertSnippet(snippets[5]),
    ...wTourUtils.insertSnippet(snippets[6]),
    ...wTourUtils.insertSnippet(snippets[7]),
    ...wTourUtils.insertSnippet(snippets[8]),
]);
