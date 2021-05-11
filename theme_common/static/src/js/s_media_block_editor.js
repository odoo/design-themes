odoo.define('theme_common.s_media_block_editor', function (require) {
    'use strict';

    var core = require('web.core');
    var s_options = require('web_editor.snippets.options');
    require("theme_common.s_media_block_frontend");

    var QWeb = core.qweb;

    // MEDIABLOCK EDITOR

    // Image background - Fix for mediablock
    s_options.registry.background.include({
        selectClass: function (previewMode, value, $li) {
            var self = this;
            this._super(previewMode, value, $li);
            if (this.$target.hasClass("s_media_block")) {
                var objs = self.$target.find(".videoBox, > iframe, .yt_video_container");
                objs.stop(true,true)
                    .fadeOut(200)
                    .delay(300)
                    .fadeIn(2000);
            }
        },
    }),

    s_options.registry.s_media_block = s_options.Class.extend({
        xmlDependencies: ['/theme_common/static/src/xml/s_media_block_modal.xml'],
        videoOpt: function (previewMode, value, $opt) {
            var self = this;
            self.trigger_up('animation_stop_demand', {
                editableMode: true,
                $target: self.$target,
            });
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
                self.trigger_up('animation_start_demand', {
                    editableMode: true,
                    $target: self.$target,
                });
            });

            $cancel.on('click', function () {
                self.trigger_up('animation_start_demand', {
                    editableMode: true,
                    $target: self.$target,
                });
            });

            var update_form = function () {
                self.$target.attr('src', this.value);
                self.trigger_up('animation_start_demand', {
                    editableMode: true,
                    $target: self.$target,
                });
                self.$modal.find('form').attr('data-video-type', self.$target.data('video-type'));
            };

            $src
            .on('keyup', _.throttle(update_form, 700))
            .on('change', function () {
                update_form.call(this);
                this.value = self.$target.attr('src');
            })
            .keyup();

            this.$modal.on('hidden.bs.modal', function () {
                self.trigger_up('animation_start_demand', {
                    editableMode: true,
                    $target: self.$target,
                });
                $(this).remove();
            });
        },
    });
});
