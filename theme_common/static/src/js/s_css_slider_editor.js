(function(){

  'use strict';
  var website = openerp.website;
  website.openerp_website = {};

    website.snippet.options.marginAndResize.include({
      start: function(){
        this._super();
        var self = this;
        self.$overlay.find(".oe_handle.size .size").on('mouseup', function (event){
          event.preventDefault();
          if(self.$target.hasClass("s_css_slider")){
            setTimeout(function(){
              self.$target.data('snippet-view').resizeImgs(self.$target);
            })
          }
        });
      }
    }),


    website.snippet.options.s_css_slider_slide = website.snippet.Option.extend({
      newSlideUrl: "/website/image/theme_common.image_content_23",
      start: function(){
        var self = this,
          container = self.$target;

        self.reset();
        self.$target.data('snippet-view').start(true);

        setTimeout(function(){
          self.$overlay.find(".js-s_css_slider_addSlide").on('click', function ()    { self.addSlide();  });
          self.$overlay.find(".js-s_css_slider_removeSlide").on('click', function () { self.removeSlide();  });
        },100);

        $(document.body).on("media-saved", function(){
          self.resizeImgsEditor();
        });
      },

      resizeImgsEditor: function(){
        var self = this;
        setTimeout(function(){
          self.$target.data('snippet-view').resizeImgs(self.$target);
        })
      },

      reset: function() {
        var self= this;
        self.$target.find(".s_css_slider_pagination").remove().end()
          .find("span").unbind("click.s_css");
      },

      addSlide: function(){
        var self = this;
        var $currentSlide = self.$target.find(".slider .slide.selected");
        var pagination = self.$target.find(".s_css_slider_pagination");
        var $newSlide = $('<li><div class="info" contentEditable="false"><span class="h3" contentEditable="true">Slide Title</span><br/><span class="p" contentEditable="true">Slide Description</span></div><img class="o_not-animable" src="' + self.newSlideUrl + '" /></li>');

        $currentSlide.after($newSlide);
        self.reset();
        self.$target.data('snippet-view').start(true);
        self.$target.data('snippet-view').nextSlide(self.$target, pagination); 
      },

      removeSlide: function () {
        var self = this;
        var $currentSlide = self.$target.find(".slider .slide.selected");
        var pagination = self.$target.find(".s_css_slider_pagination"); 

        self.$target.data('snippet-view').prevSlide(self.$target, pagination);
        $currentSlide.remove();
        self.reset();
        self.$target.data('snippet-view').start(true);
      },

      clean_for_save: function(){
        var self = this;
        self.$target
          .find(".s_css_slider_pagination").remove().end()
          .find(".navigation .prev").addClass("inactive").end()
          .find(".navigation .next").removeClass("inactive").end()
          .find(".slider .slide").removeClass("selected move-left").end()
          .find(".slider .slide").first().addClass("selected");
      }
    })

})();