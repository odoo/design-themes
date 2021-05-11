odoo.define('theme_kiddo_sale.collapse_categories', function (require) {
    'use strict';

    var base = require('web_editor.base');

    base.ready().then(function () {
        // CATEGORIES
        var $category_list = $(".oe_website_sale #products_grid_before");
        if ($category_list.length) {
            // Close the category using the arrow
            $category_list.on('click', '.close-icon', function (event) {
                $(event.target).closest('li').removeClass('active');
            });

            // Open the category using the arrow
            $category_list.on('click', '.open-icon', function (event) {
                // Close the others
                $category_list.find("li").removeClass('active');
                // Open this one's hierarchy
                $(event.target).parents('li').each(function (parent) {
                    $(this).addClass('active');
                });
            });

            // Open the current category tab
            var location_category_regex =  /(\/shop\/category\/[^\/]*)/g;
            var location_category = window.location.pathname;
            var matches = location_category_regex.exec(location_category);
            location_category = matches ? matches[1] : location_category;
            $('h3[class="category-name"]').siblings('ul').find('li:has(a[href="' +  location_category + '"])').addClass('active');
        }
    });
});
