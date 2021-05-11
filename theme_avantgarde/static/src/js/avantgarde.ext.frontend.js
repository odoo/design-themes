(function(){
  'use strict';

  var website = openerp.website;
  var session = new openerp.Session();
  var _t = openerp._t;

  website.openerp_website = {};

  website.snippet.animationRegistry.s_google_map.include({
    selector: ".s_google_map",

    lightMonoMap  : [{"featureType":"administrative.locality","elementType":"all","stylers":[{"hue":"#2c2e33"},{"saturation":7},{"lightness":19},{"visibility":"on"}]},{"featureType":"landscape","elementType":"all","stylers":[{"hue":"#ffffff"},{"saturation":-100},{"lightness":100},{"visibility":"simplified"}]},{"featureType":"poi","elementType":"all","stylers":[{"hue":"#ffffff"},{"saturation":-100},{"lightness":100},{"visibility":"off"}]},{"featureType":"road","elementType":"geometry","stylers":[{"hue":"#bbc0c4"},{"saturation":-93},{"lightness":31},{"visibility":"simplified"}]},{"featureType":"road","elementType":"labels","stylers":[{"hue":"#bbc0c4"},{"saturation":-93},{"lightness":31},{"visibility":"on"}]},{"featureType":"road.arterial","elementType":"labels","stylers":[{"hue":"#bbc0c4"},{"saturation":-93},{"lightness":-2},{"visibility":"simplified"}]},{"featureType":"road.local","elementType":"geometry","stylers":[{"hue":"#e9ebed"},{"saturation":-90},{"lightness":-8},{"visibility":"simplified"}]},{"featureType":"transit","elementType":"all","stylers":[{"hue":"#e9ebed"},{"saturation":10},{"lightness":69},{"visibility":"on"}]},{"featureType":"water","elementType":"all","stylers":[{"hue":"#e9ebed"},{"saturation":-78},{"lightness":67},{"visibility":"simplified"}]}],
    lillaMap      : [{elementType: "labels", stylers: [{saturation: -20 }] }, {featureType: "poi", elementType: "labels", stylers: [{visibility: "off"}] }, {featureType: 'road.highway', elementType: 'labels', stylers: [{visibility: "off"}] }, {featureType: "road.local", elementType: "labels.icon", stylers: [{visibility: "off"}] }, {featureType: "road.arterial", elementType: "labels.icon", stylers: [{visibility: "off"}] }, {featureType: "road", elementType: "geometry.stroke", stylers: [{visibility: "off"}] }, {featureType: "transit", elementType: "geometry.fill", stylers: [{hue: '#2d313f' }, {visibility: "on"}, {lightness: 5 }, {saturation: -20 }] }, {featureType: "poi", elementType: "geometry.fill", stylers: [{hue: '#2d313f' }, {visibility: "on"}, {lightness: 5 }, {saturation: -20 }] }, {featureType: "poi.government", elementType: "geometry.fill", stylers: [{hue: '#2d313f' }, {visibility: "on"}, {lightness: 5 }, {saturation: -20 }] }, {featureType: "poi.sport_complex", elementType: "geometry.fill", stylers: [{hue: '#2d313f' }, {visibility: "on"}, {lightness: 5 }, {saturation: -20 }] }, {featureType: "poi.attraction", elementType: "geometry.fill", stylers: [{hue: '#2d313f' }, {visibility: "on"}, {lightness: 5 }, {saturation: -20 }] }, {featureType: "poi.business", elementType: "geometry.fill", stylers: [{hue: '#2d313f' }, {visibility: "on"}, {lightness: 5 }, {saturation: -20 }] }, {featureType: "transit", elementType: "geometry.fill", stylers: [{hue: '#2d313f' }, {visibility: "on"}, {lightness: 5 }, {saturation: -20 }] }, {featureType: "transit.station", elementType: "geometry.fill", stylers: [{hue: '#2d313f' }, {visibility: "on"}, {lightness: 5 }, {saturation: -20 }] }, {featureType: "landscape", stylers: [{hue: '#2d313f' }, {visibility: "on"}, {lightness: 5 }, {saturation: -20 }] }, {featureType: "road", elementType: "geometry.fill", stylers: [{hue: '#2d313f' }, {visibility: "on"}, {lightness: 5 }, {saturation: -20 }] }, {featureType: "road.highway", elementType: "geometry.fill", stylers: [{hue: '#2d313f' }, {visibility: "on"}, {lightness: 5 }, {saturation: -20 }] }, {featureType: "water", elementType: "geometry", stylers: [{hue: '#2d313f' }, {visibility: "on"}, {lightness: 5 }, {saturation: -20 }] }],
    blueMap       : [{stylers: [{ hue: "#00ffe6" }, { saturation: -20 } ] },{featureType: "road", elementType: "geometry", stylers: [{ lightness: 100 }, { visibility: "simplified" } ] },{featureType: "road", elementType: "labels", stylers: [{ visibility: "off" } ] } ],
    retroMap      : [{"featureType":"administrative","elementType":"all","stylers":[{"visibility":"on"},{"lightness":33}]},{"featureType":"landscape","elementType":"all","stylers":[{"color":"#f2e5d4"}]},{"featureType":"poi.park","elementType":"geometry","stylers":[{"color":"#c5dac6"}]},{"featureType":"poi.park","elementType":"labels","stylers":[{"visibility":"on"},{"lightness":20}]},{"featureType":"road","elementType":"all","stylers":[{"lightness":20}]},{"featureType":"road.highway","elementType":"geometry","stylers":[{"color":"#c5c6c6"}]},{"featureType":"road.arterial","elementType":"geometry","stylers":[{"color":"#e4d7c6"}]},{"featureType":"road.local","elementType":"geometry","stylers":[{"color":"#fbfaf7"}]},{"featureType":"water","elementType":"all","stylers":[{"visibility":"on"},{"color":"#acbcc9"}]}],
    flatMap       : [{"stylers":[{"visibility":"off"}]},{"featureType":"road","stylers":[{"visibility":"on"},{"color":"#ffffff"}]},{"featureType":"road.arterial","stylers":[{"visibility":"on"},{"color":"#fee379"}]},{"featureType":"road.highway","stylers":[{"visibility":"on"},{"color":"#fee379"}]},{"featureType":"landscape","stylers":[{"visibility":"on"},{"color":"#f3f4f4"}]},{"featureType":"water","stylers":[{"visibility":"on"},{"color":"#7fc8ed"}]},{},{"featureType":"road","elementType":"labels","stylers":[{"visibility":"on"}]},{"featureType":"poi.park","elementType":"geometry.fill","stylers":[{"visibility":"on"},{"color":"#83cead"}]},{"elementType":"labels","stylers":[{"visibility":"on"}]},{"featureType":"landscape.man_made","elementType":"geometry","stylers":[{"weight":0.9},{"visibility":"off"}]}],
    cobaltMap     : [{"featureType":"all","elementType":"all","stylers":[{"invert_lightness":true},{"saturation":10},{"lightness":30},{"gamma":0.5},{"hue":"#435158"}]}],
    cupertinoMap  : [{"featureType":"water","elementType":"geometry","stylers":[{"color":"#a2daf2"}]},{"featureType":"landscape.man_made","elementType":"geometry","stylers":[{"color":"#f7f1df"}]},{"featureType":"landscape.natural","elementType":"geometry","stylers":[{"color":"#d0e3b4"}]},{"featureType":"landscape.natural.terrain","elementType":"geometry","stylers":[{"visibility":"off"}]},{"featureType":"poi.park","elementType":"geometry","stylers":[{"color":"#bde6ab"}]},{"featureType":"poi","elementType":"labels","stylers":[{"visibility":"off"}]},{"featureType":"poi.medical","elementType":"geometry","stylers":[{"color":"#fbd3da"}]},{"featureType":"poi.business","stylers":[{"visibility":"off"}]},{"featureType":"road","elementType":"geometry.stroke","stylers":[{"visibility":"off"}]},{"featureType":"road","elementType":"labels","stylers":[{"visibility":"off"}]},{"featureType":"road.highway","elementType":"geometry.fill","stylers":[{"color":"#ffe15f"}]},{"featureType":"road.highway","elementType":"geometry.stroke","stylers":[{"color":"#efd151"}]},{"featureType":"road.arterial","elementType":"geometry.fill","stylers":[{"color":"#ffffff"}]},{"featureType":"road.local","elementType":"geometry.fill","stylers":[{"color":"black"}]},{"featureType":"transit.station.airport","elementType":"geometry.fill","stylers":[{"color":"#cfb2db"}]}],
    carMap        : [{"featureType":"administrative","stylers":[{"visibility":"off"}]},{"featureType":"poi","stylers":[{"visibility":"simplified"}]},{"featureType":"road","stylers":[{"visibility":"simplified"}]},{"featureType":"water","stylers":[{"visibility":"simplified"}]},{"featureType":"transit","stylers":[{"visibility":"simplified"}]},{"featureType":"landscape","stylers":[{"visibility":"simplified"}]},{"featureType":"road.highway","stylers":[{"visibility":"off"}]},{"featureType":"road.local","stylers":[{"visibility":"on"}]},{"featureType":"road.highway","elementType":"geometry","stylers":[{"visibility":"on"}]},{"featureType":"water","stylers":[{"color":"#84afa3"},{"lightness":52}]},{"stylers":[{"saturation":-77}]},{"featureType":"road"}],
    bwMap         : [{stylers: [{ hue: "#00ffe6" }, { saturation: -100 } ] },{featureType: "road", elementType: "geometry", stylers: [{ lightness: 100 }, { visibility: "simplified" } ] },{featureType: "road", elementType: "labels", stylers: [{ visibility: "off" } ] } ],

  }),

  website.snippet.animationRegistry.s_media_block.include({
    selector: ".s_media_block",

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
          
          $(function(){
          if (!jQuery.browser.mobile)
              self.youtube_video(video_id);
          });
          return;

        } else if (video_type == 'vimeo') {
          video_url = "http://player.vimeo.com/video/" + video_id + "?autoplay=1" + ";loop=1";
        } else if (video_type == 'dailymotion') {
          video_url = "http://www.dailymotion.com/embed/video/" + video_id + "?autoplay=1";
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
      }
    },

    youtube_video:function(video_id){
      var self = this;
      var $yt_muted,
          $yt_loop;

      (self.$target.attr('yt-muted'))?  $yt_muted = true :  $yt_muted = false;
      (self.$target.attr('yt-loop'))?  $yt_loop = true :  $yt_loop = false;

      var $yt_startAt = (self.$target.attr('yt-startat'));
      var $yt_stopAt  = (self.$target.attr('yt-stopat'));
      var $yt_opacity = (self.$target.attr('yt-opacity'));
      var $yt_vol     = (self.$target.attr('yt-vol'));
      var $yt_bg      = (self.$target.attr('yt-bg'));

      var timeStamp = Date.now();
      var timeStamp2 = Date.now() + 100;

      var $video_container = $('<div class="yt_video_container '+ $yt_bg +'"></div>').attr("id", "s_media_block_" + timeStamp);
      var $el = $('<div id="'+ timeStamp2 +'" class="player" data-property="{videoURL:\'http://youtu.be/' + video_id + '\',containment:\'#s_media_block_' + timeStamp +  '\',startAt:'+ $yt_startAt +',stopAt:'+ $yt_stopAt +',mute:'+ $yt_muted +',stopMovieOnBlur:false,vol:'+ $yt_vol +',autoPlay:true,showYTLogo:false,loop:'+ $yt_loop +',opacity:'+ $yt_opacity +'}"></div>/');
      var $loader = $("<span style='top:0px' class='yt-loader'><span></span></span>");
      
      $video_container.append($el).append($loader);
      self.$target.append($video_container);

 
      $("#"+ timeStamp2).YTPlayer();
      

      var interval = null;
      
      $loader.animate({width: "45%"},800, function() {
        var el = $loader;
        interval = setInterval(function(){ timer() }, 300);
        function timer() { var w =  el.width(); el.width(w + 5);}
      });  

      $("#"+ timeStamp2).on("YTPStart",function(){
        if (self.$target.find(".controls").length > 0){return}
        clearInterval(interval);
        $loader.css("width", "100%").fadeOut(500);
    
        var controls = $("<span class='controls' ><span class='btnplay fa fa-fw fa-pause' /><span class='btnMute fa fa-fw fa-volume-up' /></span>").appendTo(self.$target.find(".yt_video_container"));
        var btnplay = controls.find(".btnplay");
        var btnMute = controls.find(".btnMute");

        if($yt_muted == true){btnMute.remove();}; 
        
        function to_mute(){
          $("#"+ timeStamp2).muteYTP();
          btnMute
            .removeClass("fa-volume-up").addClass("fa-volume-off")
            .unbind("click", to_mute)
            .bind("click", to_audio)
        }
        function to_audio(){
          $("#"+ timeStamp2).unmuteYTP();
          btnMute
            .removeClass("fa-volume-off").addClass("fa-volume-up")
            .unbind("click", to_audio)
            .bind("click", to_mute)
        }
        function to_pause(){
          $("#"+ timeStamp2).pauseYTP();
          btnplay
            .removeClass("fa-pause").addClass("fa-play")
            .unbind("click", to_pause)
            .bind("click", to_play)
        }
        function to_play(){
          $("#"+ timeStamp2).playYTP();
          btnplay
            .removeClass("fa-play").addClass("fa-pause")
            .unbind("click", to_play)
            .bind("click", to_pause)
        }
        btnplay.bind("click",to_pause);
        if(!$yt_muted == true){btnMute.bind("click", to_mute)}; 
      });
    },

    stop_video: function() {
      var self = this;
      var $vid = self.$target.find('.videoBox');
      var $yt_video = self.$target.find('.yt_video_container .player');

      $(window).unbind('resize.s_media_block');
      if ($vid.length > 0) { $vid.remove();}      
      if ($yt_video.length > 0) { 
        self.$target.find('.yt_video_container').remove() 
      } else {
        var $iframe = this.$target.find('iframe');
        if ($iframe.length > 0) {  $iframe.remove();}
      }
    },
  })

})();