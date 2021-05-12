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

        drop_and_build_snippet: function () {
            this.$target.find('.nav-tabs a').show();
            var self = this;
            this.id = this.unique_id();
            this.$link.attr("href", '#' + self.id);
            this.$content.attr("id", self.id);
        },

        on_clone: function ($clone) {
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

// (function () {
//	'use strict';

//	var website = openerp.website;
//	website.openerp_website = {};

//     s_options.registry.tab = s_options.Class.extend({
//         unique_id: function () {
//             var id = 0;
//             $(".tabs [class*='col-']").each(function () {
//                 var tid = 1 + parseInt($(this).attr("id").replace(/[^0123456789]/g, ''),10);
//                 if (id < tid) id = tid;
//             });
//             return "tab" + id;
//         },
//         drop_and_build_snippet: function () {
//             this.id = this.unique_id();
//             this.$target.attr("id", this.id);
//             this.reset_id();
//         },
//         on_clone: function ($clone) {
//             var id = this.unique_id();
//             $clone.attr("id", id);
//         },
//         clean_for_save: function () {
//             this.$inner.find(".tab-pane").removeClass("active in")
//                 .first().addClass("active in");
//             this.$indicators.find('li').removeClass('active')
//                 .first().addClass("active");
//         },
//         start: function () {
//             // this.id = this.$target.attr("id");
//             this.$inner = this.$target.find('.tab-content');
//             this.$indicators = this.$target.find('.nav-tabs');
//         },
//         add_tab: function (type, value) {
//             if (type !== "click") return;
//             this.$indicators.find('li.active').after('<li><a data-target="#" role="tab" data-toggle="tab">A new tab</a></li>');
//             this.$inner.find('.tab-pane.active').after('<div class="tab-pane fade" id=""><p>Your content here.</p></div>');
//             this.reset_id();
//         },
//         remove_tab: function (type, value) {
//             if (type !== "click") return;
//             this.$inner.find(".active").remove();
//             this.$indicators.find(".active").remove();
//             this.$indicators.find("li:first-child").addClass('active');
//             this.$inner.find("div.tab-pane:first-child").addClass('active');
//             this.reset_id();
//         },
//         reset_id: function () {
//             var uid = this.id;
//             this.$indicators.find('li a').each(function (i) {
//                 $(this).attr("data-target", "#" + uid + i);
//             });
//             this.$inner.find('.tab-pane').each(function (i) {
//                 $(this).attr("id", "" + uid + i);
//             });
//         },
//     });
// })();
