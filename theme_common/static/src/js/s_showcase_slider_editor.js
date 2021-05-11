(function(){

  'use strict';
  var website = openerp.website;
  website.openerp_website = {};


    website.snippet.options.s_showcase_slider = website.snippet.Option.extend({
      start: function(){
        this._super();
        var self = this,
          container = self.$target;

        self.reset();
        self.$target.data('snippet-view').start();

        self.$target.find("span").bind("click.s-ss-editor", function(){
          $('body,html').animate({'scrollTop':self.$target.offset().top - 70}, 0);
        })

        setTimeout(function(){
          self.$overlay.find(".js-s_ss_addSlide").on('click', function ()    { self.addSlide(); return false; });
          self.$overlay.find(".js-s_ss_removeSlide").on('click', function () { self.removeSlide(); return false; });
        },100)
      },

      reset: function() {
        var self= this;
        self.$target.find(".s-ss-slider-pagination").remove().end()
          .find("span, .s-ss-slider").unbind("click.s-ss");
      },

      addSlide: function(){
        var self = this;
        var $currentSlide = self.$target.find(".s-ss-slider li.selected");
        var pagination = self.$target.find(".s-ss-slider-pagination");
        var $newSlide = $('<li><img class="o_not-animable" src="/website/image/theme_common.image_content_23" /></li>');
      
        $currentSlide.after($newSlide);
        self.reset();
        self.$target.data('snippet-view').start();
        self.$target.data('snippet-view').nextSlide(self.$target, pagination); 
      },

      removeSlide: function () {
        var self = this;
        var $currentSlide = self.$target.find(".s-ss-slider li.selected");
        var pagination = self.$target.find(".s-ss-slider-pagination"); 

        self.$target.data('snippet-view').prevSlide(self.$target, pagination);
        $currentSlide.remove();
        self.reset();
        self.$target.data('snippet-view').start();
      }
    })

})();