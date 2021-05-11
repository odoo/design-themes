$(function() {
    // CATEGORIES
    var category_list = "#products_grid_before";
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
            $(event.target).parents('li').each(function(parent) {
                $(this).addClass('active');
            });
        });

        // Open the current category tab
        $('li:has(a[href="' + window.location.pathname + '"])').addClass('active');
    }
});
