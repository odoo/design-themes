odoo.define('theme_graphene.editor', function (require) {
    'use strict';

    var Editor = require('web_editor.snippet.editor').Editor;
    var s_options = require('web_editor.snippets.options');

    // Typography
    s_options.registry.typo_style = s_options.Class.extend({
        selectClass: function (previewMode, value, $li) {
            this._super(previewMode, value, $li);
            var self = this;
            var hasWrapper = this.$target.parent().is('.s_typo_style_wrapper');

            if (value === 'title-boxed' || value === 'title-underlined') {
                if (!hasWrapper) {
                    this.$target.wrap('<div class="title-parent s_typo_style_wrapper"/>');
                }

                //trigg transition
                this.$target.addClass('o_animate o_hold').removeClass('o_visible').css('visibility', 'visible');
                _.defer(function () {
                    self.$target.addClass('o_visible').removeClass('o_hold');
                });
            } else {
                this.$target.removeClass('o_animate o_hold');
                if (hasWrapper) {
                    this.$target.unwrap();
                } else {
                    // Compatibility (before the title-parent class was not put
                    // on a wrapper but on the existing parent)
                    this.$target.parent().removeClass('title-parent');
                }
            }
        },
        cleanForSave: function () {
            this.$target.removeClass("o_visible");
        },
    });

    Editor.include({
        _onDragAndDropStart: function () {
            this.$target.addClass("oe_snippet_body");
            return this._super.apply(this, arguments);
        },
        _onDragAndDropStop: function () {
            this.$target.removeClass("oe_snippet_body");
            return this._super.apply(this, arguments);
        },
    });

    // Top Banner Options
    s_options.registry.graphene_top_banner_options = s_options.Class.extend({

        //----------------------------------------------------------------------
        // Public
        //----------------------------------------------------------------------

        /**
         * @override
         */
        onFocus: function () {
            this.$overlay.data('$optionsSection').find('.oe_snippet_clone, .oe_snippet_move')
                .toggleClass('d-none', this.$target.hasClass('move_to_top'));
        },
        /**
         * @override
         */
        onRemove: function () {
            this.$target.removeClass('move_to_top');
            this._toggleTransparentMenu(false);
        },

        //----------------------------------------------------------------------
        // Options
        //----------------------------------------------------------------------

        /**
         * @override
         */
        selectClass: function (previewMode, value, $li) {
            this._super(previewMode, value, $li);
            $('.move_to_top').not(this.$target).removeClass('move_to_top');
            this._toggleTransparentMenu(value === 'move_to_top');
        },

        //----------------------------------------------------------------------
        // Private
        //----------------------------------------------------------------------

        /**
         * @override
         */
        _toggleTransparentMenu: function (enable) {
            var self = this;
            this.trigger_up('action_demand', {
                actionName: 'toggle_page_option',
                params: [{name: 'header_overlay', value: enable}],
                onSuccess: function () {
                    self.trigger_up('action_demand', {
                        actionName: 'toggle_page_option',
                        params: [{name: 'header_color', value: ''}],
                    });
                    self._refreshPublicWidgets();
                    $('html, body').animate({scrollTop: enable ? 0 : (self.$target.offset.top + 100)}, 1000);
                    self.onFocus();
                },
            });
        },
    });
});
