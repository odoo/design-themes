(function(){
    'use strict';

    var website = openerp.website;

    website.add_template_file('/theme_common/static/src/xml/s_media_block_modal.xml');

    website.openerp_website = {};

    // MEDIABLOCK
    website.snippet.options.s_media_block = website.snippet.Option.extend({
        s_media_block: function (type, value, $li) {
            if (type !== 'click') return;
        },

        video_opt: function (type, value, $li) {
            if (type !== 'click')  return;
            var self = this;
            self.$modal = $(openerp.qweb.render("theme_common.s_media_block_modal"));
            self.$modal.appendTo('body');
            self.$modal.modal();

            var $header_type = self.$modal.find("#header_type"),
                $header_type_icon = self.$modal.find(".videoEnabler i"),
                $tab_html5 = self.$modal.find("#tab_html5"),
                $tab_custom = self.$modal.find("#tab_custom"),
                $mp4 = self.$modal.find("#mp4"),
                $webm = self.$modal.find("#webm"),
                $ogg = self.$modal.find("#ogg"),

                $muted = self.$modal.find("#muted"),
                $loop = self.$modal.find("#loop"),
                $controls = self.$modal.find("#controls"),
                $autoplay = self.$modal.find("#autoplay"),

                $custom_content = self.$modal.find("#custom_content"),
                $iframefit = self.$modal.find("input:radio[name=iframefit]"),

                $cancel = self.$modal.find("#cancel"),
                $sub_data = self.$modal.find("#sub_data");

            attr_to_modal();
            self.typeBK = $header_type.val(); //store the actual type

            if (!$custom_content.val()) {
                // if custom code is empty,provide an example video
                $custom_content.val('<iframe src="//player.vimeo.com/video/105977011?title=0&amp;byline=0&amp;portrait=0&amp;color=24a8bf&amp;autoplay=1&amp;loop=1" width="500" height="264" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>');
                self.$target.attr('custom_content', $custom_content.val());
            };

            update_header_type();

            $header_type.on('change',function(){
                update_header_type();
            });

            $sub_data.on('click', function() {
                modal_to_attr();
                self.$target.data('snippet-view').stop_video();
                self.$target.data('snippet-view').start_video();
            });

            $cancel.on('click', function() {
                self.$target.attr('header_type', self.typeBK );
                self.$target.data('snippet-view').stop_video();
                self.$target.data('snippet-view').start_video();
            });

            function update_header_type() {
                var val = $header_type.val();

                self.$target.attr('header_type', $header_type.val() );

                if (val == 'video') {
                    $header_type_icon.removeClass().addClass('fa fa-video-camera');
                    $tab_html5.addClass("active","trans");
                    $tab_custom.removeClass("active","trans");
                    self.$target.data('snippet-view').stop_video();
                    self.$target.data('snippet-view').start_video();
                } else if ( val == 'custom_content' )  {
                    $header_type_icon.removeClass().addClass( "fa fa-code" );
                    $tab_html5.removeClass("active","trans");
                    $tab_custom.addClass("active","trans");
                    self.$target.data('snippet-view').stop_video(); // TODO Activate Iframe
                    self.$target.data('snippet-view').start_video();
                } else {
                    $header_type_icon.removeClass().addClass( "fa fa-picture-o" );
                    $tab_html5.removeClass("active","trans");
                    $tab_custom.removeClass("active","trans");
                    self.$target.data('snippet-view').stop_video();
                }
            }

            function modal_to_attr() {
                // header type
                self.$target.attr('header_type', $header_type.val() );

                // video paths
                ($mp4.val())? self.$target.attr('mp4', $mp4.val()) : self.$target.removeAttr( "mp4" );
                ($webm.val())? self.$target.attr('webm', $webm.val()) : self.$target.removeAttr( "webm" );
                ($ogg.val())? self.$target.attr('ogg', $ogg.val()) : self.$target.removeAttr( "ogg" );

                //video options
                ($muted.attr('checked') == 'checked')? self.$target.attr('muted', $muted.val()) : self.$target.removeAttr( "muted" );
                ($loop.attr('checked') == 'checked')? self.$target.attr('loop', $loop.val()) : self.$target.removeAttr( "loop" );
                ($controls.attr('checked') == 'checked')? self.$target.attr('controls', $controls.val()) : self.$target.removeAttr( "controls" );
                ($autoplay.attr('checked') == 'checked')? self.$target.attr('autoplay', $autoplay.val()) : self.$target.removeAttr( "autoplay" );

                //custom content
                ($custom_content.val())? self.$target.attr('custom_content', $custom_content.val()) : self.$target.removeAttr( "custom_content" );

                //iframe fit mode
                self.$target.attr('iframefit', self.$modal.find('input[name=iframefit]:checked').val())
            };

            function attr_to_modal() {
                // header type
                $header_type.val(self.$target.attr('header_type'));

                // video paths
                (self.$target.attr('mp4'))? $mp4.val(self.$target.attr('mp4')) : $mp4.val('');
                (self.$target.attr('webm'))? $webm.val(self.$target.attr('webm')) : $webm.val('');
                (self.$target.attr('ogg'))? $ogg.val(self.$target.attr('ogg')) : $ogg.val('') ;

                //video options
                (self.$target.attr('muted'))? $muted.attr('checked', true) : $muted.attr('checked', false);
                (self.$target.attr('loop'))? $loop.attr('checked', true) : $loop.attr('checked', false);
                (self.$target.attr('controls'))? $controls.attr('checked', true) : $controls.attr('checked', false);
                (self.$target.attr('autoplay'))? $autoplay.attr('checked', true) : $autoplay.attr('checked', false);

                //custom content
                if (self.$target.attr('custom_content')) {$custom_content.val(self.$target.attr('custom_content'))};

                //iframe fit mode
                if (self.$target.attr('iframefit') ) {
                    $iframefit.filter('[value='+self.$target.attr('iframefit')+']').prop('checked', true);
                };
            }

            this.$modal.on('hidden.bs.modal', function () {
                $(this).remove();
            });
        },

        set_active: function () {
            this.$el.find('[data-header_type]')
                .removeClass('active')
                .filter('[data-header_type="'+this.$target.attr('data-header_type')+'"]')
                .addClass('active');
            this._super();
        },

        drop_and_build_snippet: function () {
            this.s_media_block('click', null, null);
        },

        clean_for_save: function () {
            var self= this;
            self.$target.data('snippet-view').stop_video();
        }

    })
})();