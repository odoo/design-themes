odoo.define('your_module.carousel', function (require) {
    'use strict';

    var core = require('web.core');
    var Widget = require('web.Widget');

    var QWeb = core.qweb;

    var CarouselWidget = Widget.extend({
        template: 'carousel_template',

        init: function (parent, carousel_images) {
            this._super.apply(this, arguments);
            this.carousel_images = carousel_images;
        },
    });

    return CarouselWidget;
});
var carousel_images = [
    'theme_silon/static/src/img/product_banner/slide1.jpg',
    'theme_silon/static/src/img/product_banner/slide2.jpg',
   'theme_silon/static/src/img/product_banner/slide3.jpg'
];

var carousel = new CarouselWidget(null, carousel_images);
carousel.appendTo($('#carousel-container'));

