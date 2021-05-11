odoo.define('theme_common.s_showcase_editor.js', function (require) {
    'use strict';

    var s_options = require('web_editor.snippets.options');

    s_options.registry.s_showcase = s_options.Class.extend({
        onClone: function () {
            this._reset_alignment();
        },

        onRemove: function () {
            this._reset_alignment(this.$target);
        },

        _reset_alignment: function ($exclude) {
            var $features = this.$target.closest(".s_showcase").find(".feature").not($exclude);

            // Remove classes used in the previus implementation
            $features.removeClass('col-sm-offset-2');

            // Wait until the $clone element is in place
            setTimeout(function () {
                $features.unwrap('.row');

                _.each($features, function (feat, i) {
                    var even = (i % 2 === 0);
                    $(feat)
                        .toggleClass('text-right', even)
                        .toggleClass('text-left', !even)
                        .toggleClass('col-md-offset-2', !even);
                });

                // Re-wrap in rows
                for (var i = 0; i < $features.length; i+=2) {
                    $features.slice(i, i + 2).wrapAll("<div class='row'/>");
                }
            }, 100);
        }
    });
});
