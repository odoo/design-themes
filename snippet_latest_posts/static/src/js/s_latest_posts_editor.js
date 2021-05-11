odoo.define('snippet_latest_posts.s_latest_posts_editor', function (require) {
    'use strict';

    var core = require('web.core');
    var s_options = require('web_editor.snippets.options');
    var s_animation = require('web_editor.snippets.animation');
    var Model = require('web.Model');

    var _t = core._t;

    // js_get_posts
    s_options.registry.js_get_posts = s_options.Class.extend({
        drop_and_build_snippet: function () {
            if (!this.$target.data('snippet-view')) {
                this.$target.data("snippet-view", new s_animation.registry.js_get_posts(this.$target));
            }
        },

        clean_for_save: function () {
            this.$target.empty();
        },
    });

    // js_get_posts limit
    s_options.registry.js_get_posts_limit = s_options.Class.extend({
        start: function () {
            var self = this;
            setTimeout(function () {
                var ul = self.$overlay.find(".snippet-option-js_get_posts_limit > ul");
                if (self.$target.attr("data-posts_limit")) {
                    var limit = self.$target.attr("data-posts_limit");
                    ul.find('li[data-posts_limit="' + limit + '"]').addClass("active");
                } else {
                    ul.find('li[data-posts_limit="3"]').addClass("active");
                }
            }, 100)
        },

        posts_limit: function (type, value, $li) {
            var self = this;
            if (type != "click") {return}
            value = parseInt(value);
            this.$target.attr("data-posts_limit",value)
                                    .data("posts_limit",value)
                                    .data('snippet-view').redrow(true);
            setTimeout(function () {
                $li.parent().find("li").removeClass("active");
                $li.addClass("active");
            }, 100);
        },
    });

    // js_get_posts Select Blog
    s_options.registry.js_get_posts_selectBlog = s_options.Class.extend({
        start: function () {
            this._super();
            var self      = this;
            var model     = new Model('blog.blog');
            var blogsList = [];

            model
            .call('search_read',
            [
                [],
                ['name','id']// attributes to get
            ],
            {} )
            .then(function (blogs) {
                self.createBlogsList(blogs)// start printing posts...
            })
            .fail(function (e) {
                // No data
                var title = _t("Oops, Houston we have a problem"),
                    msg   = $("<div contenteditable='false' class='message error text-center'><h3>"+ title +"</h3><code>"+ e.data.message + "</code></div>" );
                self.$target.append(msg)
                return;
            });
        },

        createBlogsList: function (blogs) {
            var self = this;
            var ul = null;

            setTimeout(function () {
                ul = self.$overlay.find(".snippet-option-js_get_posts_selectBlog > ul");
                $(blogs).each(function () {
                    var blog = $(this);
                    var li = $('<li data-filter_by_blog_id="' + blog[0].id + '"><a>' + blog[0].name + '</a></li>');
                    ul.append(li);
                });
                if (self.$target.attr("data-filter_by_blog_id")) {
                    var id = self.$target.attr("data-filter_by_blog_id");
                    ul.find("li[data-filter_by_blog_id=" + id  + "]").addClass("active");
                }
            },100)
        },

        filter_by_blog_id: function (type, value, $li) {
            var self = this;
            if (type == "click") {
                $li.parent().find("li").removeClass("active");
                $li.addClass("active");
                value = parseInt(value);
                self.$target.attr("data-filter_by_blog_id",value)
                                        .data("filter_by_blog_id",value)
                                        .data('snippet-view').redrow(true);
            }
        },
    });
});
