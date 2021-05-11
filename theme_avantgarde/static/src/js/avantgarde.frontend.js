(function(){
	'use strict';

	var website = openerp.website;

	website.openerp_website = {};


  $(document).ready(function () {
    var self               = $(this),
        $avant_header       = $("#avant_header"),
        $avant_header_clone = null,
        avant_header_affix  = false,
        avant_top_content   = false,
        $wrapwrap          = $("#wrapwrap"),
        $wrap              = $("#wrap"),
        $win               = $(window),
        winH               = $(window).height(),
        winW               = $(window).width(),
        edit_bar_h         = null;
      
      // Top Affix Menu
      if ($avant_header.hasClass("top_menu_affix")){
        avant_header_affix = true;
        var $avant_header_clone = $avant_header.clone().insertAfter($avant_header).attr("id","avant_header_affix").addClass("affix"); 
        $avant_header_clone.find('[data-toggle="collapse"]').each(function(){
          var source = $(this),
              coo    = source.attr("data-target"),
              target = $avant_header_clone.find(coo),
              c      = coo.substring(1);   
          source.attr("data-target", coo + "_clone");
          target.removeClass(c).addClass(c + "_clone" );
        })      
      };

      // Clean vertical align
      $(".v-align").filter(function(){
        return $(this).parent().is(":not(.slide)");
      }).addClass("preserve3d");

      // Top content layout 
      if($wrap.find(".move_to_top").length > 0){ 
        avant_top_content = true; 
        $wrapwrap.addClass("top_content");
      }

      $win
        .load(function() {})
        // Resize
        .on("resize", function(){
          if(avant_top_content == true){
            var s = $wrap.find(".move_to_top, .cover.js_fullheight").height();
            var hOffset = $avant_header.scrollTop() + $avant_header.height()
            $wrap.css("margin-top", ((s - hOffset) - 100)  );
          };
          $win.trigger("scroll");
        }) // Scroll
        .on("scroll", function(){
          if(avant_header_affix == true){
            var wOffset  = $win.scrollTop();
            var hOffset  = $avant_header.scrollTop();
            (wOffset > (hOffset + 300) )? $avant_header_clone.addClass("affixed") : $avant_header_clone.removeClass("affixed");
          }
        })
        .trigger("resize");
      

  }),

  // Avantgarde Theme
  website.snippet.animationRegistry.avant_init = website.snippet.Animation.extend({
    selector : "body",

    stop : function() {
      if($('#avant_header_affix').length > 0){ $('#avant_header_affix').remove();}
    }
  }),


  // Ripple animation
  website.snippet.animationRegistry.avant_links = website.snippet.Animation.extend({
    selector: ".btn, .dropdown-menu li a",

    start: function(){

      var timeout,
          btn = this.$target;

      btn
      .css({ position: 'relative', overflow: 'hidden'})
      .bind('mousedown', function(e) {
        var ripple;
        if (btn.find('.avant-ripple').length === 0) {
          ripple = $('<span class="avant-ripple"/>');
          btn.prepend(ripple);
        } else {
          ripple = btn.find('.avant-ripple');
        }
        ripple.removeClass('avant-ripple-animated');

        if (!ripple.height() && !ripple.width()) {
          var diameter = Math.max(btn.outerWidth(), btn.outerHeight());
          ripple.css({ height: diameter, width: diameter });
        }

        var x = e.pageX - btn.offset().left - ripple.width() / 2;
        var y = e.pageY - btn.offset().top - ripple.height() / 2;

        ripple
          .css({ top: y + 'px',left: x + 'px'})
          .addClass('avant-ripple-animated');

        setTimeout(function() {
          ripple.removeClass('avant-ripple-animated');
        }, 351);
      });
    },
  }),


  //masonry-block
  website.snippet.animationRegistry.masonry_block = website.snippet.Animation.extend({
    selector : ".s_masonry_block",

    start: function() {
      var self = this;
      self.resize();

      $(window).on("resize", function(){
        self.resize();
      })
    },

    resize: function() {
      var self = this,
          w = self.$target.width(),
          ww = $(window).width();
      self.$target.css("height", w/2);
    }
  })

})();



