odoo.define('theme_graphene.ext.editor', function (require) {
    'use strict';

    var ajax = require('web.ajax');
    var core = require('web.core');

    ajax.loadXML('/theme_graphene/static/src/xml/s_media_block_modal_ext.xml', core.qweb);
});
