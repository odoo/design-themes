(function(){
    'use strict';

    var website = openerp.website;
    website.openerp_website = {};

    website.snippet.options.collapse = website.snippet.Option.extend({
        unique_id: function () {
            return "myCollapse" + new Date().valueOf();
        },
        drop_and_build_snippet: function() {
            this.id = this.unique_id();
            this.$link.attr({"href": '#' + this.id, "aria-controls": '#' + this.id, "data-parent": '#' + this.$main_id });
            this.$content.attr("id", this.id);
        },
        on_clone: function ($clone) {
            this.id = this.unique_id();
            this.$link.attr({"href": '#' + this.id, "aria-controls": '#' + this.id});
            this.$content.attr("id", this.id);
        },
        start : function () {
            var self = this;
            this.$link = this.$target.find('.panel-heading a');
            this.$content = this.$target.find('.panel-collapse');
            this.$main_id = this.$target.closest('.panel-group').attr("id");
        },
    });

    website.snippet.options.collapse_group = website.snippet.Option.extend({

        unique_id: function () {
            return "main_myCollapse" + new Date().valueOf();
        },
        drop_and_build_snippet: function() {
            this.id = this.unique_id();
            this.$main.attr('id', this.id);
        },
        on_clone: function ($clone) {
            this.id = this.unique_id();
            this.$main.attr('id', this.id);
            this.$target.find('.panel-heading a').attr('data-parent', '#' + this.id);
        },
        start: function () {
           this.$main = this.$target.find('.panel-group');
        },
    });

})();
