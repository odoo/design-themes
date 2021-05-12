odoo.define('snippet_latest_posts.s_latest_posts_frontend', function (require) {
    'use strict';

    var sAnimation = require('website.content.snippets.animation');

    sAnimation.registry.js_get_posts = sAnimation.Class.extend({
        selector : ".js_get_posts",

        start: function () {
            this.redrow();
            return this._super.apply(this, arguments);
        },

        destroy: function () {
            this._super.apply(this, arguments);
            this.clean();
        },

        redrow: function (debug) {
            this.clean(debug);
            this.build(debug);
        },

        clean: function (debug) {
            this.$target.empty();
        },

        build: function (debug) {
            var self     = this,
                limit    = self.$target.data("posts_limit"),
                blog_id  = self.$target.data("filter_by_blog_id"),
                template = self.$target.data("template"),
                loading  = self.$target.data("loading");

            // prevent user's editing
            self.$target.attr("contenteditable","False");

            // if no data, then use defaults values
            if (!limit) limit = 3;
            if (!template) template = 'snippet_latest_posts.media_list_template';

            // create the domain
            var domain = [['website_published', '=', true]];
            if (blog_id) {domain.push(['blog_id', '=', parseInt(blog_id)]); }

            // call posts
            this._rpc({
                route: '/snippet_latest_posts/render',
                params: {
                    template: template,
                    domain: domain,
                    limit: limit,
                },
            }).then(function (posts) {
                if (loading && loading === true) {
                    // perfrorm an intro animation
                    self.loading(posts, debug);
                } else {
                    // just print the posts
                    $(posts).appendTo(self.$target);
                }
            }).fail(function (e) {
                // debug in js console
                return;
            });
        },

        loading: function (posts, debug) {
            var self = this,
                $posts = $(posts);

            if (!$posts.first().find(".loading_container") && !$posts.first().is(".loading_container")) {
                console.log("loading_container dont exist??");
                if (debug) {
                    console.info("No '.loading_container' defined \n Please, add a 'loading_container' class to the element that must be filled by the loading bar");
                }
            } else if (!$posts.first().is(".thumb") && !$posts.first().find(".thumb")) {
                console.log("thumb dont exist??");
                if (debug) {
                    console.info("No '.thumb' defined \n Please, add a 'thumb' class to your thumbnail div");
                }
            } else {
                $posts.each(function () {
                    var $post     = $(this),
                        $load_c   = $post.find(".loading_container"),
                        $thumb    = $post.find(".thumb .o_blog_cover_image"),
                        $progress = $('<div class="progress js-loading"><div class="progress-bar" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width:0;" /></div>');

                    // prevent precessing empty post
                    if ($post.html() === undefined) {return;}

                    // if can't find loading container or thumb inside the post, then they are the post itself
                    if ($load_c.length === 0) { $load_c = $post; }
                    if ($thumb.length === 0)  { $thumb  = $post; }

                    $post.addClass("js-loading");
                    $progress.appendTo($load_c);
                    $post.appendTo(self.$target);

                    var bg = $thumb.css('background-image').replace('url("','').replace('")',''),
                        loaded = false;

                    $progress.find(".progress-bar").css("width","50%").attr("aria-valuenow","50");

                    var dummyImg = $('<img/>').attr('src', bg)
                        .load(function () {
                            // The post's background image is loaded, let's perform a gracefull intro animation
                            $progress.find(".progress-bar").find(".progress-bar").css("width","100%").attr("aria-valuenow","100");
                            setTimeout(function () {
                                self.showPost($post, $progress);
                            }, 500);
                            $(this).remove();
                            loaded = true;
                        });

                    // Show the post after 5sec without wait for thumb loading
                    setTimeout(function () {
                        if (loaded === false) {
                            dummyImg.remove();
                            self.showPost($post, $progress);
                        }
                    }, 5000);
                });
            }
        },

        showPost: function ($post, $progress) {
            $post.removeClass("js-loading");
            $progress.fadeOut(500);
        },
    });
});
