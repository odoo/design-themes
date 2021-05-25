(function () {
    'use strict';

    var website = openerp.website;

    website.add_template_file('/theme_avantgarde/static/src/xml/s_media_block_modal_ext.xml');
    website.openerp_website = {};

    website.snippet.options.s_css_slider_slide.include({
        newSlideUrl: "/theme_avantgarde/static/src/img/theme_samples/sample_2.jpg"
    });
})();
