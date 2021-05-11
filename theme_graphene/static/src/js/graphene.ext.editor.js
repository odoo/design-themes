(function(){
    'use strict';

    var website = openerp.website;
    var session = new openerp.Session();
    var _t = openerp._t;

    website.add_template_file('/theme_graphene/static/src/xml/s_media_block_modal_ext.xml');
    website.openerp_website = {};
    website.snippet.options.s_media_block.include({
    
        video_opt: function (type, value, $li) {
            if (type !== 'click')  return;
            var self = this;
            self.$target.data('snippet-view').stop_video();
            self.$modal = $(openerp.qweb.render("theme_graphene.s_media_block_modal_ext"));
            self.$modal.appendTo('body');           
            self.$modal.modal();

            var $header_type      = self.$modal.find("#header_type"),
                $header_type_icon = self.$modal.find(".videoEnabler i"),
                $tab_html5        = self.$modal.find("#tab_html5"),
                $tab_custom       = self.$modal.find("#tab_custom"),
                $mp4              = self.$modal.find("#mp4"),
                $webm             = self.$modal.find("#webm"),
                $ogg              = self.$modal.find("#ogg"),
                
                $muted            = self.$modal.find("#muted"),
                $loop             = self.$modal.find("#loop"),
                $controls         = self.$modal.find("#controls"),
                $autoplay         = self.$modal.find("#autoplay"),
                
                $custom_content   = self.$modal.find("#custom_content"),
                
                //youtube-options
                $yt_muted   = self.$modal.find("#yt-muted"),
                $yt_loop    = self.$modal.find("#yt-loop"),
                $yt_startat = self.$modal.find("#yt-startat"),
                $yt_stopat  = self.$modal.find("#yt-stopat"),
                
                $yt_opacity = self.$modal.find("#yt-opacity"),
                $yt_vol     = self.$modal.find("#yt-vol"),
                $yt_bg      = self.$modal.find("#yt-bg"),
                
                $iframefit  = self.$modal.find("input:radio[name=iframefit]"),
                
                $cancel     = self.$modal.find("#cancel"),
                $sub_data   = self.$modal.find("#sub_data");

            attr_to_modal();
            self.typeBK = $header_type.val(); //store de actual type 

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

                // youtube options
                ($yt_muted.attr('checked') == 'checked')? self.$target.attr('yt-muted', $yt_muted.val()) : self.$target.removeAttr( "yt-muted" );
                ($yt_loop.attr('checked') == 'checked')? self.$target.attr('yt-loop', $yt_loop.val()) : self.$target.removeAttr( "yt-loop" );
                

                ($yt_startat.val())? self.$target.attr('yt-startat', $yt_startat.val()) : self.$target.removeAttr( "yt-startat" );
                ($yt_stopat.val())? self.$target.attr('yt-stopat', $yt_stopat.val()) : self.$target.removeAttr( "yt-stopat" );
                ($yt_opacity.val())? self.$target.attr('yt-opacity', $yt_opacity.val()) : self.$target.removeAttr( "yt-opacity" );
                ($yt_vol.val())? self.$target.attr('yt-vol', $yt_vol.val()) : self.$target.removeAttr( "yt-vol" );
    
                ($yt_bg.val())? self.$target.attr('yt-bg', $yt_bg.val()) : self.$target.removeAttr( "yt-bg" );

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

                //youtube options
                (self.$target.attr('yt-muted'))? $yt_muted.attr('checked', true) : $yt_muted.attr('checked', false);
                (self.$target.attr('yt-loop'))? $yt_loop.attr('checked', true) : $yt_loop.attr('checked', false);
                (self.$target.attr('yt-startat'))? $yt_startat.val(self.$target.attr('yt-startat')) : $yt_startat.val('');
                (self.$target.attr('yt-stopat'))? $yt_stopat.val(self.$target.attr('yt-stopat')) : $yt_stopat.val('');
                
                (self.$target.attr('yt-opacity'))? $yt_opacity.val(self.$target.attr('yt-opacity')) : $yt_opacity.val('');
                (self.$target.attr('yt-vol'))? $yt_vol.val(self.$target.attr('yt-vol')) : $yt_vol.val('');
                (self.$target.attr('yt-bg'))? $yt_bg.val(self.$target.attr('yt-bg')) : $yt_bg.val('');

                //iframe fit mode           
                if (self.$target.attr('iframefit') ) {      
                    $iframefit.filter('[value='+self.$target.attr('iframefit')+']').prop('checked', true);
                };               
            }

            this.$modal.on('hidden.bs.modal', function () {
                $(this).remove();
            });
        },

    }),

    website.snippet.options.o_animate.include({
        animationName: null,

        select_class:function(type, value, $li){
            this._super(type, value, $li);
            var self = this;
            if (type == "click" && self.$target.is(".s_animated_boxes .slide")) self.processSlides(self.$target, value);
        },

        processSlides: function($el, value){
            $el.attr("graph_anim", value);
            this.animationName = value;
        },

        clean_for_save: function(){
            this._super();
            var self = this;
            if (self.$target.is(".s_animated_boxes .slide")) self.cleanSlides(self.$target);
        },

        cleanSlides: function($el){
            var self = this;
            $el.removeClass("o_animate o_animate_preview " + self.animationName);
        }
    })
})();