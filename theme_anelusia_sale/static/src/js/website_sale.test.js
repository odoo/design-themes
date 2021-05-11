(function () {
    'use strict';
    var _t = openerp._t;

    openerp.website.ready().done(function () {

        var additional_step = {
            title:     _t('Click on Menu button'),
            element:   '.navbar-header span:contains("MENU")',
            waitFor:   'li:contains("Review Order")',
        };

        var last_valid_steps = [
            {
                tour: openerp.Tour.tours.shop_customize,
                title: 'check optional product is removed',
                additional_step: additional_step,
            },
            {
                tour: openerp.Tour.tours.event_buy_tickets,
                title: 'Order Now',
                additional_step: additional_step,
            },
        ];

        _.each(last_valid_steps, function(s) {
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
}());
