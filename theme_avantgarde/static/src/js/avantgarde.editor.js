(function(){
    'use strict';

    var website = openerp.website;


    website.openerp_website = {};


    // Typography
    website.snippet.options.typo_style = website.snippet.Option.extend({
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
    website.snippet.options.avant_simpleAccordition = website.snippet.Option.extend({
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
    }),

    website.snippet.options.avant_simpleAccordition_bar = website.snippet.Option.extend({
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
    }),

    website.snippet.options.avant_simpleAccordition_link = website.snippet.Option.extend({
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
    }),

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
    }),

    website.snippet.Editor._drag_and_drop = website.snippet.Editor.include({
        _drag_and_drop_start: function(){
            this._super();
            this.$target.addClass("oe_snippet_body");
            return this._super.apply(this, arguments);
        },
        _drag_and_drop_stop: function(){
            this._super();
            this.$target.removeClass("oe_snippet_body")
            return this._super.apply(this, arguments);
        },
    }),

    // Tob Banner snippets
    website.snippet.options.top_banner_snippets = website.snippet.Option.extend({
        selector : ".top_banner *",
        start:function(){
            var self = this;
            self.$overlay.find(".oe_overlay_options").css("margin-top", (self.$target.height()/2));         
        }
    }),

    // Top Banner Options 
    website.snippet.options.avantgarde_top_banner_options = website.snippet.Option.extend({
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

                self.on_focus();
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

    // FIX website builder overlay issues + Change margin
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