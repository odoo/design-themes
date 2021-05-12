odoo.define('theme_common.s_animated_boxes_frontend', function (require) {
    'use strict';

var sAnimations = require('website.content.snippets.animation');

/**
 * This is a fix for some apple devices.
 * The slide of animated boxes widget is shown on hover or click on mobile
 * devices, but iOS only activates :hover if the element targeted is
 * clickable.
 */
sAnimations.registry._fixAnimatedBoxesAppleClick = sAnimations.registry._fixAppleCollapse.extend({
    selector: '.s_animated_boxes .item',
});

});
