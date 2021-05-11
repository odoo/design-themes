(function(){
	'use strict';

	var website = openerp.website;
	website.openerp_website = {};

  website.snippet.animationRegistry.s_media_block = website.snippet.Animation.extend({
    selector : "section.s_media_block",
    start: function() {
      var self = this;
      if (self.$target.attr('header_type') == ('video')) {
        self.start_video();
      }
      if (self.$target.attr('header_type') == ('custom_content')) {
        self.start_video();
      }
    },
    stop: function() {
      this.stop_video();
    },

    throttle : function (func, delay) {
      var timer = null;
      return function () {
        var context = this, args = arguments;
        if (timer == null) {
          timer = setTimeout(function () {
            func.apply(context, args);
            timer = null;
          }, delay);
        }
      };
    },

    start_video: function() {
      var self = this;
      var header_type = self.$target.attr('header_type');

      // mobile phones are not supported, just show the background image.
      if (jQuery.browser.mobile){ return; };

      if (header_type == 'video') { //Check if the user select an HTML5 video

        var mp4, webm, ogg, video;

        (self.$target.attr('mp4'))?   mp4 = '<source src="' + self.$target.attr('mp4') + '" type="video/mp4"/>' :     mp4 = null;
        (self.$target.attr('webm'))?  webm = '<source src="' + self.$target.attr('webm') + '" type="video/webm"/>' :  webm = null;
        (self.$target.attr('ogg'))?   ogg = '<source src="' + self.$target.attr('ogg') + '" type="video/ogg"/>' :     ogg = null;

        video = '<video class="videoBox hidden-xs" '
                + self.$target.attr('muted') +' '+ self.$target.attr('loop') +' '+ self.$target.attr('controls') +' '+ self.$target.attr('autoplay') +
                ' preload="metadata">'
                  + mp4 + webm + ogg +
                '</video>';

        if ((self.$target.find('.videoBox').length) == 0 ) { self.stop_video() };

        self.$target.append(video);

        self.$target.find('.videoBox').get(0).load();
        self.$target.find('.videoBox').get(0).play();

        // check if browser support objectFit
        if (document.createElement("detect").style.objectFit === "") {
          self.$target.css('max-height', '');
          self.$target.find('.videoBox').css({
            'object-fit':'cover',
            'width':'100%',
            'height':'100%',
            'object-position':'center center'
          });
        } else {
          self.position();
          self.$target.css('max-height', '');
          $(window).on('resize.s_media_block', self.throttle(function(e){
            self.position()
          }, 300));
        }


      } else if (header_type == 'custom_content') { //Check if the user add a sustom content

        self.custom_content();

      }
    },

    custom_content:function(){
      var self = this;
      var custom_content = self.$target.attr('custom_content');
      var video_id;
      var video_type;
      var video_url;

      var needle = custom_content.match(/src=["']?([^"']+)["' ]?/);

      if (needle) {

        needle = needle[1];

        if (needle.indexOf(".youtube.") != -1) {
          video_type = "youtube";
          video_id = needle.match(/\.youtube\.[a-z]+\/(embed\/|watch\?v=)?([^\/?&]+)/i)[2];
        } else if (needle.indexOf("//youtu.") != -1) {
          video_type = "youtube";
          video_id = needle.match(/youtube\.[a-z]+\/([^\/?&]+)/i)[1];
        } else if (needle.indexOf("player.vimeo.") != -1 || needle.indexOf("//vimeo.") != -1) {
          video_type = "vimeo";
          video_id = needle.match(/vimeo\.[a-z]+\/(video\/)?([^?&]+)/i)[2];
        } else if (needle.indexOf(".dailymotion.") != -1) {
          video_type = "dailymotion";
          video_id = needle.match(/dailymotion\.[a-z]+\/(embed\/)?(video\/)?([^\/?&]+)/i)[3];
        } else {
          video_type = "";
          video_id = needle;
        }

        if (video_type == 'youtube') {
          video_url = "https://www.youtube.com/embed/" + video_id + "?autoplay=1" + ";loop=1";
        } else if (video_type == 'vimeo') {
          video_url = "https://player.vimeo.com/video/" + video_id + "?autoplay=1" + ";loop=1";
        } else if (video_type == 'dailymotion') {
          video_url = "https://www.dailymotion.com/embed/video/" + video_id + "?autoplay=1";
        }

        if (video_type.length > 0 ) {
          var headerIframe = $('<iframe src="'+video_url+'" frameborder="0" allowfullscreen="allowfullscreen"></iframe>');
          self.$target.append(headerIframe);
          headerIframe = self.$target.find('iframe');
          headerIframe.fadeTo(0,0);
          if (self.$target.attr('iframefit') == 'fitCont') {
            setTimeout(function(){
              headerIframe.addClass('headerIframe');
              this.Iframeratio = (headerIframe.width() / headerIframe.height());
              self.iframeSize(this.Iframeratio);
              self.$target.css('max-height', headerIframe.width()/Iframeratio );
              headerIframe.fadeTo("slow",1);

              $(window).bind('resize.s_media_block', self.throttle(function(e){
                self.$target.css({
                  'height': headerIframe.width()/Iframeratio,
                  'max-height': headerIframe.width()/Iframeratio
                });
                self.iframeSize(this.Iframeratio);
              }, 300));

            }, 1000); // is fitCont

          } else if (self.$target.attr('iframefit') == 'fitIframe') {
            self.$target.css('max-height', '');
            headerIframe.css({'height': '100%', 'width': '100%' });
            setTimeout(function(){
              headerIframe.fadeTo("slow",1);
            }, 1000);
          }

        } else {
          var customIframe = $(custom_content).filter('iframe');
          self.$target.append(customIframe);
          self.$target.css("max-height","");
          self.$target.find("iframe").css({"height":"100%","width":"100%","top":"0","position":"absolute"});
        }

      } //  /if needle
      //} //  / if video/custom content
    },

    stop_video: function() {
      var $vid = this.$target.find('.videoBox');
      var $iframe = this.$target.find('iframe');

      $(window).unbind('resize.s_media_block');

      if ($vid) { $vid.remove();}
      if ($iframe) {  $iframe.remove();}
    },

    iframeSize: function(a) {
      var self = this;
      var headerIframe = self.$target.find('iframe'),
          ratio = a;
      headerIframe.css('width','100%');
      headerIframe.height(headerIframe.width()/ratio );

    },


    position : function() {
      var self = this;
      if (self.$target.find('.videoBox').length > 0) {
        var vid = self.$target.find('.videoBox');
        if ( vid.height() < vid.width()) { //reset video size before fit it
          vid.css('with', '100%');
          vid.css('height', 'auto');
        } else {
          vid.css('height', '100%');
          vid.css('width', 'auto');
        }

        var vidH = vid.height(),
          vidW = vid.width(),
          snippH = self.$target.outerHeight(),
          snippW = self.$target.outerWidth(),
          vidRatio = vidW / vidH,
          snippRatio = snippW / snippH;

        if (snippRatio > vidRatio) {
          vid.css('width', '100%');
          vid.css('height', 'auto');
          vid.css('left', 0);
          vid.css('top', ((vidH - snippH) / -2));
        } else {
          vid.css('height', '100%');
          vid.css('width', 'auto');
          vid.css('top', 0);
          vid.css('left', ((vidW - snippW) / -2));
        }
      };
    }


  })
})();