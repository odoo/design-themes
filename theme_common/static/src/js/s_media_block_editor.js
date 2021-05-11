odoo.define('theme_common.s_media_block_editor', function (require) {
    'use strict';

    var ajax = require('web.ajax');
    var core = require('web.core');
    var s_options = require('web_editor.snippets.options');

    var QWeb = core.qweb;

    ajax.loadXML('/theme_common/static/src/xml/s_media_block_modal.xml', core.qweb);

    // MEDIABLOCK EDITOR
    s_options.registry.s_media_block = s_options.Class.extend({
        s_media_block: function (type, value, $li) {
            if (type !== 'click') return;
        },

        video_opt: function (type, value, $li) {
            if (type !== 'click')  return;
            var self = this;
            self.$target.data('snippet-view').stop_video();
            self.$modal = $(QWeb.render("theme_common.s_media_block_modal"));
            self.$modal.appendTo('body').modal();

            var $src        = self.$modal.find('#media_block_src'),
                $cancel     = self.$modal.find("#cancel"),
                $sub_data   = self.$modal.find("#sub_data");
            var field_names = ['src', 'muted', 'loop', 'controls', 'autoplay', 'opacity', 'background', 'iframefit'];

            _.each(field_names, function (field_name) {
                var value = self.$target.attr(field_name);
                var $fields = self.$modal.find('[name="'+field_name+'"]');
                $fields.each(function (i, field) {
                    var $field = $(field);
                    if ($field.is(':radio, :checkbox')) {
                        $field.prop('checked', $field.val() === value);
                    } else if (!_.isUndefined(value)) {
                        $field.val(value);
                    }
                });
            });

            if (!$src.val()) {
                // if custom code is empty,provide an example video
                $src.val('<iframe src="//player.vimeo.com/video/105977011?title=0&amp;byline=0&amp;portrait=0&amp;color=24a8bf&amp;autoplay=1&amp;loop=1" width="500" height="264" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>');
                self.$target.attr('src', $src.val());
            }

            $sub_data.on('click', function () {
                _.each(field_names, function (field_name) {
                    var field = self.$modal.find('[name="'+field_name+'"]').filter(':checked, :not(:checkbox, :radio)');
                    self.$target.removeAttr(field_name).attr(field_name, field.val());
                });
                self.$target.data('snippet-view').stop_video();
                self.$target.data('snippet-view').start_video();
            });

            $cancel.on('click', function () {
                self.$target.data('snippet-view').stop_video();
                self.$target.data('snippet-view').start_video();
            });

            var update_form = function () {
                if (this.value == self.$target.data('snippet-view')) return;
                self.$target.data('snippet-view').src = this.value;
                self.$target.data('snippet-view').update_video_type();
                self.$modal.find('form').attr('data-video-type', self.$target.data('snippet-view').video_type);
            };

            $src.on('keyup', _.throttle(update_form, 700)).on('change', function () {
                update_form.call(this);
                if (self.$target.data('snippet-view') != this.value) {
                    this.value = self.$target.data('snippet-view').src;
                }
            }).keyup();

            this.$modal.on('hidden.bs.modal', function () {
                $(this).remove();
            });
        },

        drop_and_build_snippet: function () {
            this.s_media_block('click', null, null);
        },

        clean_for_save: function () {
            this.$target.data('snippet-view').stop_video();
        },
    });
});
