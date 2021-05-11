(function(){
	'use strict';

	var website = openerp.website;
	website.openerp_website = {};

    website.snippet.options.collapse = website.snippet.Option.extend({

        unique_id: function () {
            var id = 0;
            $(".panel-heading a").each(function () {
                var cid = 1 + parseInt($(this).attr("href").replace(/[^0123456789]/g, ''),10);
                if (id < cid) id = cid;
            });
            return "myCollapse" + id;
        },
        drop_and_build_snippet: function() {
            this.id = this.unique_id();
            this.$link.attr({"href": '#' + this.id, "aria-controls": '#' + this.id, "data-cke-saved-href": '#' + this.id });
            this.$content.attr("id", this.id);
        },
        on_clone: function ($clone) {
            this.id = this.unique_id();
            this.$link.attr({"href": '#' + this.id, "aria-controls": '#' + this.id, "data-cke-saved-href": '#' + this.id });
            this.$content.attr("id", this.id);
        },
        start : function () {
            var self = this;
            this.$link = this.$target.find('.panel-heading a');
            this.$content = this.$target.find('.panel-collapse');
        },
    });

})();

