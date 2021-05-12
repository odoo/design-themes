odoo.define('theme_common.s_tabs', function (require) {
    'use strict';

    var s_options = require('web_editor.snippets.options');

    s_options.registry.tabs = s_options.Class.extend({
        unique_id: function () {
            var id = 0;
            var self = this;
            self.$target.find(".nav-tabs a").each(function () {

                var cid = 1 + parseInt($(this).attr("href").replace(/[^0123456789]/g, ''),10);
                if (id < cid) id = cid;
            });
            return "myTabs" + id;
        },

        onBuilt: function () {
            this.$target.find('.nav-tabs a').show();
            var self = this;
            this.id = this.unique_id();
            this.$link.attr("href", '#' + self.id);
            this.$content.attr("id", self.id);
        },

        onClone: function () {
            // var self = this;
            // this.id = this.unique_id();
            // this.$link.attr("href", '#' + self.id);
            // this.$content.attr("id", self.id);
        },

        start: function () {
            this.$target.find('.nav-tabs a').show();
            var self = this;
            this.$link = self.$target.find('.nav-tabs a');
            this.$content = self.$target.find('.tab-pane');
        },
    });
});
