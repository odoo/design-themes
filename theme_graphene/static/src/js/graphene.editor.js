(function(){
    'use strict';

    var website = openerp.website;
    var session_editor = new openerp.Session();
    var _t = openerp._t;

    var animableClass  =  "o_animate";
    var previewClass   =  "o_animate_preview";
    var animatingClass =  "o_animating";
    var animatedClass  =  "o_animated";
    var inView_visible_Class = "o_visible";

    website.openerp_website = {};

    // Masonry Block
    website.snippet.options.masonry_block = website.snippet.Option.extend({
        
    }),

    // Typography
    website.snippet.options.typo_style = website.snippet.Option.extend({
        select_class: function(type, value, $li) {
            this._super(type, value, $li);
            var $self = this.$target;

            if( value == "title-boxed" || value == "title-underlined") {
                // fix parent align
                $self.parent().addClass("title-parent");
                //trigg transition
                $self.addClass("o_animate").removeClass("o_visible").css('visibility', 'visible');
                setTimeout(function(){
                    $self.addClass("o_visible");
                },500)
            } else {
                $self.parent().removeClass("title-parent");
            }
        },
        clean_for_save: function(){
            this.$target.removeClass("o_visible");
        }
    }),


    website.snippet.options.no_resize =  website.snippet.Option.extend({
        start:function(){
            self = this;
            setTimeout(function(){
                self.$overlay.find(".oe_handle_button.size").hide();
            },50)
        }
    }),



    // Simple Accordition
    website.snippet.options.graph_simpleAccordition = website.snippet.Option.extend({
        start: function () {
            self = this;
            self.$target.find(".panel-collapse ").css("height","").addClass("in");
        },
        clean_for_save: function() {
            self = this;
            self.$target.find(".panel-collapse ").css("height","0").removeClass("in");
        },
        drop_and_build_snippet: function () {
            self = this;
            self.$target.find(".panel-collapse ").css("height","").addClass("in");
        },
        on_clone: function($clone){       
            var Mrand = Math.floor((Math.random() * 9999999) + 1);      
            $clone.find("div.panel-group").attr("id",Mrand);
            $clone.find(".bar").each(function(){
                var bar = $(this);
                var rand = Math.floor((Math.random() * 9999999) + 1);      
                bar.find("a.panel-heading").attr("data-cke-saved-href","#"+rand);
                bar.find("a.panel-heading").attr("data-parent","#"+Mrand);
                bar.find("div.panel-collapse.collapse").attr("id",rand);
            })
        }
    });

    website.snippet.options.graph_simpleAccordition_bar = website.snippet.Option.extend({
        start: function () {
            self = this;
            self.$target.parent().parent().find(".panel-collapse ").css("height","").addClass("in");
        },
        on_focus: function() {
          self = this;
          self.$target.fadeTo(100,0).fadeTo(200,1);
        },
        on_clone: function($clone){    
            var rand = Math.floor((Math.random() * 9999999) + 1);      
            $clone.find("a.panel-heading").attr("data-cke-saved-href","#"+rand);
            $clone.find("div.panel-collapse.collapse").attr("id",rand);   
        }
    });

    website.snippet.options.graph_simpleAccordition_link = website.snippet.Option.extend({
        start: function () {
          self = this;
          self.$target.parent().parent().parent().find(".panel-collapse ")
            .css("height","")
            .addClass("in");
        },
        on_focus: function() {
          self = this;
          self.$target.fadeTo(100,0).fadeTo(200,1);
        }
    });

    // ANIMATED BOXES
    website.snippet.options.graphene_animated_boxes_editor = website.snippet.Option.extend({
        start: function () {
            var self = this;
            self.add_btn_edit_slide();
            setTimeout(function(){
                if (self.$target.find(".slide").length > 0) {
                    self.$overlay.find(".createSlide").addClass("hide");
                    self.$overlay.find(".deleteSlide").removeClass("hide");
                    self.$overlay.find(".btn-showSlide").removeClass("hide");
                } else {
                    self.$overlay.find(".createSlide").removeClass("hide");
                    self.$overlay.find(".deleteSlide").addClass("hide");
                    self.$overlay.find(".btn-showSlide").addClass("hide");
                }
            }, 100);
        },

        add_btn_edit_slide: function() {
            var self = this;
            self.$overlay.find(".oe_options").after('<a href="#" class="btn btn-default btn-sm btn-showSlide" title="Lock slide"><i class="fa fa-toggle-off"></i>  Edit Slide</a> ');
            self.$overlay.on('click', '.btn-showSlide', _.bind(this.toggle_slide, this));
        },

        create_slide: function(type, value, $li){
            if (type !== 'click') return;
            var self = this,
                slide = '<div class="slide editable bg-success animated text-center dur-200ms insetShadow" anim="o_anim_fade_in_down" del="0" dur="200"><div class="v-align"><h3>Your new slide</h3></div></div>';
            self.$target.append(slide);
            self.$overlay.find(".btn-showSlide").removeClass("hide");
            self.$overlay.find(".createSlide").addClass("hide");
            self.$overlay.find(".deleteSlide").removeClass("hide");
        },

        delete_slide: function(type, value, $li){
            if (type !== 'click') return;
            var self = this; 
            self.$target.find(".slide").remove();
            self.$overlay.find(".btn-showSlide").addClass("hide");
            self.$overlay.find(".createSlide").removeClass("hide");
            self.$overlay.find(".deleteSlide").addClass("hide");
        },

        toggle_slide: function(){
            var a = this.$overlay.find(".btn-showSlide"),
                i = a.find("i"),
                t = this.$target,
                s = t.find(".slide");
            if (!t.hasClass("showSlide")) { 
                t.addClass("showSlide"); i.addClass("fa-toggle-on").removeClass("fa-toggle-off"); i.css("color", "#FFF"); 
                s.addClass("visible");
            } else {
                t.removeClass("showSlide"); i.removeClass("fa-toggle-on").addClass("fa-toggle-off"); i.css("color", ""); 
                s.removeClass("visible");
            }   
        },
        clean_for_save: function(type, value, $li) {
            this.$target.removeClass("showSlide");
        }
    }),

    
    // Image background - Fix for mediablock 
    website.snippet.options.background.include({
        select_class: function(type, value, $li) {
            var self = this;
            this._super(type, value, $li);
            if (this.$target.hasClass("s_media_block")) {       
                var objs = self.$target.find(".videoBox, > iframe, .yt_video_container");
                objs.stop(true,true)
                    .fadeOut(100)
                    .delay(600)
                    .o_anim_fade_in(2000);        
            }
        }
    });

    // Background effects - Fix for mediablock 
    website.snippet.options.bg_fx = website.snippet.Option.extend({
        select_class: function(type, value, $li) {
            var self = this;
            this._super(type, value, $li);
            if (this.$target.hasClass("s_media_block")) {       
                var objs = self.$target.find(".videoBox, > iframe, .yt_video_container");
                objs.stop(true,true)
                    .fadeOut(100)
                    .delay(600)
                    .o_anim_fade_in(2000);        
            }
        }
    });

    website.snippet.Editor._drag_and_drop = website.snippet.Editor.include({
        _drag_and_drop_start: function(){
            this.$target.addClass("oe_snippet_body");
            return this._super.apply(this, arguments);
        },
        _drag_and_drop_stop: function(){
            this.$target.removeClass("oe_snippet_body")
            return this._super.apply(this, arguments);
        },
    });

    // Tob Banner snippets
    website.snippet.options.top_banner_snippets = website.snippet.Option.extend({
        selector : ".top_banner *",
        start:function(){
            var self = this;
            self.$overlay.find(".oe_overlay_options").css("margin-top", (self.$target.height()/2));         
        }
    })

    // Top Banner Options 
    website.snippet.options.graphene_top_banner_options = website.snippet.Option.extend({
        start: function(){
            this._super();
            var self = this;
            if (!self.$target.parent().is("#wrap")) {
                console.log(self)
                setTimeout(function(){
                    //self.$el.remove();        
                })
            }
        },

        on_focus:function(){
            var self = this;
            if (self.$target.hasClass("move_to_top")){
                self.$overlay
                    .find(".oe_overlay_options").css("margin-top","200px").end()
                    .find(".oe_snippet_clone, .oe_snippet_move").addClass("hidden");    
            } else {
                self.$overlay
                    .find(".oe_snippet_clone, .oe_snippet_move").removeClass("hidden");
            }
        },
        select_class: function(type, value, $li) {
            if(type != "click"){return}
            this._super(type, value, $li);
            var self = this;
            if (value == "move_to_top"){
                $(".move_to_top").removeClass("move_to_top");
                self.$target.addClass("move_to_top");
                $("#wrapwrap").addClass("top_content");
                $("#wrap").css("margin-top", (self.$target.height()* 0.9));

                $('html, body').animate({scrollTop:0}, 1000);

            } else {
                self.$target.removeClass("move_to_top");
                $("#wrapwrap").removeClass("top_content");
                $("#wrap").css("margin-top","");
                var offset = self.$target.offset.top;
                $('html, body').animate({scrollTop:(offset+100)}, 1000);
            }
            if(self.$target.hasClass("s_media_block")){
                $(window).trigger("resize");
                self.$target.data('snippet-view').stop_video();
                self.$target.data('snippet-view').start_video();
            }
        },
    }),

    // // FIX website builder overlay issues + Change margin
    website.snippet.options.marginAndResize.include({
        start: function(){
            this._super();
            var self = this;

            $(window).on("resize", function(){
                self.BuildingBlock.cover_target(self.$overlay, self.$target);
            })

            this.$overlay.find(".oe_handle.size .size").on('mouseup', function (event){
                event.preventDefault();
                if(self.$target.hasClass("move_to_top")){
                    $("#wrap").css("margin-top", (self.$target.height()* 0.9));
                    self.BuildingBlock.cover_target(self.$overlay, self.$target);
                    $(window).trigger("resize");
                }
            });
        }
    })


})();