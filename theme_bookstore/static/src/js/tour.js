/** @odoo-module */

import * as wTourUtils from '@website/js/tours/tour_utils';
import { _t } from "@web/core/l10n/translation";

const snippets = [
    {
        id: 's_banner',
        name: 'Banner',
        groupName: "Intro",
    },
    {
        id: 's_key_images',
        name: 'Key Images',
        groupName: "Columns",
    },
    {
        id: 's_title',
        name: 'Title',
        groupName: "Text",
    },
    {
        id: 's_accordion_image',
        name: 'Accordion Image',
        groupName: "Content",
    },
    {
        id: 's_cta_box',
        name: 'CTA Box',
        groupName: "Content",
    },
];

wTourUtils.registerThemeHomepageTour("bookstore_tour", () => [
    wTourUtils.assertCssVariable('--color-palettes-name', '"default-26"'),
    ...wTourUtils.dragNDrop(snippets[0]),
    ...wTourUtils.clickOnText(snippets[0], 'h1'),
    wTourUtils.goBackToBlocks(),
    ...wTourUtils.dragNDrop(snippets[1]),
    ...wTourUtils.dragNDrop(snippets[2]),
    ...wTourUtils.dragNDrop(snippets[3]),
    ...wTourUtils.dragNDrop(snippets[4]),
    ...wTourUtils.clickOnSnippet(snippets[4]),
    wTourUtils.changeOption('ContainerWidth', 'we-button-group.o_we_user_value_widget', _t('width')),
    wTourUtils.goBackToBlocks(),
]);
