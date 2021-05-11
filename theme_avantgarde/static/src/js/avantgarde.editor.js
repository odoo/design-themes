odoo.define('theme_avantgarde.editor', function (require) {
    'use strict';

    var Editor = require('web_editor.snippet.editor').Editor;
    var s_options = require('web_editor.snippets.options');

    // Typography
    s_options.registry.typo_style = s_options.Class.extend({
    });

    // Simple Accordition
    s_options.registry.avant_simpleAccordition = s_options.Class.extend({
        start: function () {
            this.$target.find(".panel-collapse ").css("height","").addClass("in");
        },
        cleanForSave: function () {
            this.$target.find(".panel-collapse ").css("height","0").removeClass("in");
        },
        onClone: function () {
            var Mrand = Math.floor((Math.random() * 9999999) + 1);
            this.$target.find("div.panel-group").attr("id",Mrand);
            this.$target.find(".bar").each(function () {
                var bar = $(this);
                var rand = Math.floor((Math.random() * 9999999) + 1);
                bar.find("a.panel-heading").attr("data-parent","#"+Mrand);
                bar.find("div.panel-collapse.collapse").attr("id",rand);
            });
        },
    });

    s_options.registry.avant_simpleAccordition_bar = s_options.Class.extend({
        start: function () {
            this.$target.parent().parent().find(".panel-collapse ").css("height","").addClass("in");
        },
        onFocus: function () {
            this.$target.fadeTo(100,0).fadeTo(200,1);
        },
        onClone: function () {
            var rand = Math.floor((Math.random() * 9999999) + 1);
            this.$target.find("div.panel-collapse.collapse").attr("id",rand);
        },
    });

    s_options.registry.avant_simpleAccordition_link = s_options.Class.extend({
        start: function () {
            this.$target.parent().parent().parent().find(".panel-collapse ")
                .css("height","")
                .addClass("in");
        },
        onFocus: function () {
            this.$target.fadeTo(100,0).fadeTo(200,1);
        },
    });

    Editor.include({
        _onDragAndDropStart: function () {
            this._super();
            this.$target.addClass("oe_snippet_body");
            return this._super.apply(this, arguments);
        },
        _onDragAndDropStop: function () {
            this._super();
            this.$target.removeClass("oe_snippet_body");
            return this._super.apply(this, arguments);
        },
    });

    // Top Banner Options
    s_options.registry.avantgarde_top_banner_options = s_options.Class.extend({

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
