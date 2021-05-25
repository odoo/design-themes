(function(){
  'use strict';
  var website = openerp.website;
  var session_editor = new openerp.Session();
  var _t = openerp._t;

  
  // js_get_posts
  website.snippet.options.js_get_posts = website.snippet.Option.extend({
    drop_and_build_snippet: function(){
      var self = this;
      if (!self.$target.data('snippet-view')) {
        this.$target.data("snippet-view", new website.snippet.animationRegistry.js_get_posts(this.$target));
      }
    },
    clean_for_save:function(){
      this.$target.empty();
    }
  }),

  // js_get_posts limit
  website.snippet.options.js_get_posts_limit = website.snippet.Option.extend({
    start:function(){
      var self = this;
      setTimeout(function(){
        var ul = self.$overlay.find(".snippet-option-js_get_posts_limit > ul");
        if (self.$target.attr("data-posts_limit")) {
          var limit = self.$target.attr("data-posts_limit");
          ul.find('li[data-posts_limit="' + limit + '"]').addClass("active");
        } else {
          ul.find('li[data-posts_limit="3"]').addClass("active");
        }
      },100)
    },
    posts_limit:function(type, value, $li){
      var self = this;
      if(type != "click"){return}
      value = parseInt(value);
      this.$target.attr("data-posts_limit",value)
                  .data("posts_limit",value)
                  .data('snippet-view').redrow(true);
      setTimeout(function(){
        $li.parent().find("li").removeClass("active");
        $li.addClass("active");
      },100); 
    }
  }),

  // js_get_posts Select Blog
  website.snippet.options.js_get_posts_selectBlog = website.snippet.Option.extend({
    start: function() {
      this._super();
      var self      = this;
      var model     =  session_editor.model('blog.blog');
      var blogsList = [];

      model
      .call('search_read', 
      [
        [],
        ['name','id']// attributes to get
      ],  
      {} )
      .then(function(blogs){
        self.createBlogsList(blogs)// start printing posts...
      }) 
      .fail(function (e) {
        // No data
        var title = _t("Oops, Huston we have a problem"),
            msg   = $("<div contenteditable='false' class='message error text-center'><h3>"+ title +"</h3><code>"+ e.data.message + "</code></div>" );
        self.$target.append(msg)
        return;
      });
    },

    createBlogsList: function(blogs){
      var self = this;
      var ul = null;

      setTimeout(function(){
        ul = self.$overlay.find(".snippet-option-js_get_posts_selectBlog > ul");
        $(blogs).each(function(){
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

    filter_by_blog_id:function(type, value, $li){
      var self = this;
      if(type == "click"){
        $li.parent().find("li").removeClass("active");
        $li.addClass("active");
        value = parseInt(value);
        self.$target.attr("data-filter_by_blog_id",value)
                    .data("filter_by_blog_id",value)
                    .data('snippet-view').redrow(true); 
      }
    }
  })

})();
