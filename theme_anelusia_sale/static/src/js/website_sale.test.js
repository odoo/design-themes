odoo.define('theme_anelusia_sale.website_sale_test', function (require) {
    'use strict';

    var core = require('web.core');
    var Tour = require('web.Tour');

    var _t = core._t;

    var additional_step = {
        title:     _t('Click on Menu button'),
        element:   '.navbar-header span:contains("MENU")',
        waitFor:   'li:contains("Review Order")',
    };

    var last_valid_steps = [
        {
            tour: Tour.tours.shop_customize,
            title: 'check optional product is removed',
            additional_step: additional_step,
        },
        {
            tour: Tour.tours.event_buy_tickets,
            title: 'Order Now',
            additional_step: additional_step,
        },
    ];

    _.each(last_valid_steps, function (s) {
        if (s.tour) {
            var steps = s.tour.steps;
            for (var k=0; k<steps.length; k++) {
                if (steps[k].title === s.title) {
                    steps.splice(k+1, 0, s.additional_step);
                    break;
                }
            }
        }
    });
});
