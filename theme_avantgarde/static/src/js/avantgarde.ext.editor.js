odoo.define('theme_avantgarde.ext.editor', function (require) {
    'use strict';

    var ajax = require('web.ajax');
    var core = require('web.core');
    var s_options = require('web_editor.snippets.options');

    s_options.registry.s_css_slider_slide.include({
        newSlideUrl: "/theme_avantgarde/static/src/img/theme_samples/sample_2.jpg",
    });
});
