$(function(){

    // CATEGORIES
    var category_list = "#products_grid_before"
    if ($(".oe_website_sale " + category_list).length) {
        // Close the category using the arrow
        $(category_list).on('click', '.close-icon', function(event) {
            $(event.target).closest('li').removeClass('active');
        });

        // Open the category using the arrow
        $(category_list).on('click', '.open-icon', function(event) {
            // Close the others
            $(category_list + " li").removeClass('active');
            // Open this one's hierarchy
            $(event.target).parents('li').each(function(parent){
                $(this).addClass('active');
            });
        });

        // Open the current category tab
        var category_re = /\/shop\/category\/.*-/;
        if (category_re.test(window.location.pathname)) {
            var category_id = window.location.pathname.replace(category_re, '');
            var category_li = $('li:has(a[data-oe-model="product.public.category"][data-oe-id=' + category_id + '])')
            category_li.addClass('active')
        }
    }
});
