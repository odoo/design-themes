odoo.define('theme_common.s_media_block_frontend', function (require) {
    'use strict';

    var sAnimation = require('website.content.snippets.animation');

    // MEDIABLOCK EDITOR
    sAnimation.registry.s_media_block = sAnimation.Class.extend({
        selector : "section.s_media_block",

        start: function () {
            this.start_video();
            return this._super.apply(this, arguments);
        },

        destroy: function () {
            this._super.apply(this, arguments);
            this.stop_video();
        },

        update_video_type: function () {
            var regex_url = '((?:https?:)?//([^\\s\'"<>\\\\/]+)/([^\\s\'"<>\\\\]+))';
            var match = this.src.match(new RegExp('\\ssrc=[\'"]?' + regex_url));
            match = match || this.src.match(new RegExp('^\\s*' + regex_url));
            if (!match) {
                this.video_type = "image";
                this.src = "";
                return;
            }

            var url = match[1];
            var domain = match[2];
            var path = match[3];

            match = undefined;

            var services_prefix = {
                youtube: 'https://youtu.be/',
                vimeo: 'https://vimeo.com/',
                dailymotion: 'http://dai.ly/',
            };

            if (/\.youtube(-nocookie)?\./.test(domain)) {
                this.video_type = 'youtube';
                match = path.match(/^(?:embed\/|watch\?v=)?([^\/?&#]+)/i);
            } else if (domain === "youtu.be") {
                this.video_type = 'youtube';
                match = path.match(/^([^\/?&#]+)/);
            } else if (_.str.include(domain, "vimeo.")) {
                this.video_type = 'vimeo';
                match = path.match(/^(?:video\/)?([^?&#]+)/i);
            } else if (_.str.include(domain, ".dailymotion.")) {
                this.video_type = "dailymotion";
                match = path.match(/(?:embed\/)?(?:video\/)?([^\/?&#_]+)/i);
            } else if (domain === "dai.ly") {
                this.video_type = "dailymotion";
                match = path.match(/^([^\/?&#]+)/);
            }

            if (match) {
                this.src = services_prefix[this.video_type] + match[1];
            } else if (!/\ssrc=/.test(this.src)) {
                this.src = url;
                this.video_type = 'html5';
            } else {
                this.video_type = 'other';
            }

            this.$target.data('video-type', this.video_type);
        },

        start_video: function () {
            var self = this;
            var video_url;

            // mobile phones are not supported, just show the background image.
            if (jQuery.browser.mobile) { return; }

            if (!self.video_type || self.src !== self.$target.attr('src')) {
                self.src = self.$target.attr('src');
                if (!self.src) {
                    return;
                }
                self.update_video_type();
            }

            var params = _.chain(['muted', 'loop', 'autoplay', 'controls']).map(function (attribute) {
                var value = self.$target.attr(attribute);
                return [attribute, value ? 1 : value];
            }).object().value();

            var video_id = self.src.split('/')[3];

            switch (self.video_type) {
                case 'html5':
                    video_url = self.src;
                    break;
                case 'youtube':
                    video_url = "https://www.youtube.com/embed/" + video_id;
                    if ('muted' in params) params['mute'] = 1;
                    if ('loop' in params) params['playlist'] = video_id;
                    _.extend(params, {iv_load_policy: 3, rel: 0, showinfo: 0});
                    break;
                case 'vimeo':
                    video_url = "https://player.vimeo.com/video/" + video_id;
                    _.extend(params, {color: 'fff', title: 0, byline: 0, portrait: 0, badge: 0});
                    break;
                case 'dailymotion':
                    video_url = "https://www.dailymotion.com/embed/video/" + video_id;
                    if (!params["controls"]) params["chromeless"] = 1;
                    _.extend(params, {logo: 0, info: 0, related: 0, wmode: 'opaque'});
                    break;
            }

            var whenPlayerReady = (self['create_' + self.video_type + '_video'] || self['create_video']).call(self, self.$target, video_url, params);

            whenPlayerReady.then(function ($player) {
                $player.fadeTo(0, 0);
                $player.addClass('o_player').parent().addClass('o_player_wrapper');
                self.ratio = ($player.width() / $player.height());

                if (self.$target.attr('iframefit') === 'fitCont') {
                    $player.parentsUntil(self.$target).css({width: '100%', height: 'auto'});
                    if ($player.is('iframe')) {
                        $player.css('width', '100%');
                        $player.height($player.width() / self.ratio);
                    } else {
                        $player.css({width: '100%', height: 'auto'});
                    }
                } else if (self.$target.attr('iframefit') === 'fitIframe') {
                    $player.parentsUntil(self.$target).andSelf().css({width: '100%', height: '100%'});
                }

                $player.fadeTo("slow", 1);
                $player.removeClass('o_media_loading');
                $(window).trigger('resize');
            });
        },

        stop_video: function () {
            this.$target.find('.videoBox, iframe').remove();
            $(window).unbind('resize.s_media_block');
        },

        create_video: function ($container, video_url, params) {
            var def = $.Deferred();
            var $iframe;

            if (video_url) {
                $iframe = $('<iframe/>', {
                    frameborder: "0",
                    allowfullscreen: "allowfullscreen",
                    src: video_url + '?' + $.param(params),
                });
            } else {
                $iframe = $('<div/>').html(this.src).find('iframe:first').css({
                    height: "100%", width: "100%", top: 0, position: "absolute",
                });
                if ($iframe.length) {
                    $container.css('max-height', '');
                } else {
                    return def.reject();
                }
            }

            $iframe.addClass('o_media_loading o_temp_auto_element');
            $iframe.on('load', function () {
                def.resolve($iframe);
            });
            $container.append($iframe);

            return def;
        },

        create_html5_video: function ($container, video_url, params) {
            var def = $.Deferred();
            var $video_content = $('<video/>', {'class': 'videoBox d-none d-md-block o_temp_auto_element', 'preload': 'metadata'}).attr(params).attr('src', video_url);

            $video_content.addClass('o_media_loading');
            $video_content.on('canplay', function () {
                def.resolve($video_content);
            });
            $container.append($video_content);

            $video_content.get(0).load();
            if (params['autoplay']) {
                $video_content.get(0).play();
            }

            return def;
        },

        // When the visitor is logged in YouTube, the console return "Failed to execute 'postMessage'";
        // That is a known error from the side of the Youtube API.
        // Fortunately it's not blocking but unfortunatly the fix should be done by the Google team.
        YTPlayer_video: function ($container, video_url, _params) {
            var video_id = this.src.split('/')[3];
            var params = _.mapObject(_params, function (v) { return !!v; });

            var opacity      = this.$target.attr('opacity');
            var background   = this.$target.attr('background') || '';

            var timeStamp = Date.now();

            var $video_container = $('<div/>', {
                'class': 'yt_video_container '+ background,
                id: "s_media_block_" + timeStamp,
            });
            var playerParams = {
                videoURL: video_id, containment: '#s_media_block_' + timeStamp, mute: params['muted'], loop: params['loop'],
                stopMovieOnBlur: false, autoPlay: true, showYTLogo: false, opacity: opacity, showControls: false,
            };
            var $el = $('<div/>', {'class': 'player', 'data-property': JSON.stringify(playerParams)});
            var $loader = $("<span class='yt-loader'><span/></span>");
            $video_container.append($el).append($loader);

            var interval = null;
            if ($("#oe_main_menu_navbar").length > 0) { $loader.css("top", $("#oe_main_menu_navbar").outerHeight()+1); }
            $loader.animate({width: "45%"}, 800, function () {
                var el = $loader;
                interval = setInterval(function () { timer(); }, 300);
                function timer() { var w =  el.width(); el.width(w + 5); }
            });

            if (!params['autoplay']) {
                $el.one('YTPStart', function () {
                    $el.YTPPause();
                });
            }

            var def = $.Deferred();
            $el.on('YTPReady', function () {
                clearInterval(interval);
                $loader.css("width", "100%").fadeOut(500);

                def.resolve($video_container.find('iframe'));

                if (!params['controls'] && params['autoplay']) {
                    return;
                }

                var $controls = $("<span/>", {'class': 'controls'}).appendTo($video_container);

                var $btnplay = $("<span/>", {'class': 'fa fa-fw'}).appendTo($controls);
                var playing = params['autoplay'];
                $btnplay.toggleClass("fa-pause", playing).toggleClass("fa-play", !playing);
                $btnplay.on("click", play_callback);
                if (!params['controls']) {
                    $btnplay.one('click', function () {
                        $controls.remove();
                    });
                }

                if (!params['muted'] && params['controls']) {
                    var $btnMute = $("<span/>", {'class': 'fa fa-fw fa-volume-up'}).appendTo($controls);
                    $btnMute.on("click", mute_callback);
                }

                function play_callback() {
                    if (playing) {
                        $el.YTPPause();
                    } else {
                        $el.YTPPlay();
                    }
                    playing = !playing;

                    $btnplay.toggleClass("fa-pause", playing).toggleClass("fa-play", !playing);
                }
                function mute_callback() {
                    $el.YTPToggleVolume();
                    $btnMute.toggleClass("fa-volume-up").toggleClass("fa-volume-off");
                }
            });

            $container.append($video_container);
            $el.YTPlayer();

            return def;
        },
    });
});
