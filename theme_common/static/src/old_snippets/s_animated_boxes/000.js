odoo.define('theme_common.s_animated_boxes_frontend', function (require) {
    'use strict';

var publicWidget = require('web.public.widget');

/**
 * This is a fix for some apple devices.
 * The slide of animated boxes widget is shown on hover or click on mobile
 * devices, but iOS only activates :hover if the element targeted is
 * clickable.
 */
publicWidget.registry._fixAnimatedBoxesAppleClick = publicWidget.registry._fixAppleCollapse.extend({
    selector: '.s_animated_boxes .item',
});
});
