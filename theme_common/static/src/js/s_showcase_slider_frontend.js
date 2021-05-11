odoo.define('theme_common.s_showcase_slider_frontend', function (require) {
    'use strict';

    var s_animation = require('web_editor.snippets.animation');
    var session = require('web.session');

    s_animation.registry.s_showcase_slider = s_animation.Class.extend({
        selector: ".s_showcase_slider",

        start: function () {
            var self = this;
            var container = self.$target;
            // create slider pagination
            var sliderPagination = self.createSliderPagination(container);
            self.bindEvents(container, sliderPagination);
        },

        bindEvents: function (container, sliderPagination) {
            var self = this;

            container.find('.s_ss_slider').bind('click.s_ss', function (event) {
                //enlarge slider images
                if ( !container.hasClass('active') && $(event.target).is('.s_ss_slider')) {
                    container.removeClass('active');
                    container.addClass('active').one('webkitTransitionEnd otransitionend oTransitionEnd msTransitionEnd transitionend', function () {
                        $('body,html').animate({'scrollTop':container.offset().top - 70}, 200);
                    });
                }
            });

            container.find('.s_ss_close').bind('click.s_ss', function (e) {
                container.removeClass('active');
            });

            container.find('.s_ss_next').bind('click.s_ss', function (e) {
                self.nextSlide(container, sliderPagination);
            });

            container.find('.s_ss_prev').bind('click.s_ss', function (e) {
                self.prevSlide(container, sliderPagination);
            });

            sliderPagination.bind('click.s_ss', function () {
                var selectedDot = $(this);
                if (!selectedDot.hasClass('selected')) {
                    var selectedPosition = selectedDot.index(),
                        activePosition = container.find('.s_ss_slider .selected').index();
                    if ( activePosition < selectedPosition) {
                        self.nextSlide(container, sliderPagination, selectedPosition);
                    } else {
                        self.prevSlide(container, sliderPagination, selectedPosition);
                    }
                }
            });

            //keyboard slider navigation
            $(document).keyup(function (event) {
                if (event.which=='37' && $('.active').length > 0 && !$('.active .s_ss_slider .selected').is(':first-child')) {
                    self.prevSlide($('.active'), $('.active').find('.s_ss_slider_pagination li'));
                } else if ( event.which=='39' && $('.active').length && !$('.active .s_ss_slider .selected').is(':last-child')) {
                    self.nextSlide($('.active'), $('.active').find('.s_ss_slider_pagination li'));
                } else if (event.which=='27') {
                    container.removeClass('active');
                }
            });
        },

        createSliderPagination: function ($container) {
            var wrapper = $('<ul class="s_ss_slider_pagination"></ul>').insertAfter($container.find('.s_ss_slider_navigation'));
            $container.find('.s_ss_slider li').each(function (index) {
                var dotWrapper = (index == 0) ? $('<li class="selected"></li>') : $('<li></li>'),
                    dot = $('<a href="#0"></a>').appendTo(dotWrapper);
                dotWrapper.appendTo(wrapper);
                dot.text(index+1);
            });
            return wrapper.children('li');
        },

        nextSlide: function ($container, $pagination, $n) {
            var self = this,
                    visibleSlide = $container.find('.s_ss_slider .selected'),
                    navigationDot = $container.find('.s_ss_slider_pagination .selected');

            if (typeof $n === 'undefined') $n = visibleSlide.index() + 1;
            visibleSlide.removeClass('selected');
            $container.find('.s_ss_slider li').eq($n).addClass('selected').prevAll().addClass('move-left');
            navigationDot.removeClass('selected')
            $pagination.eq($n).addClass('selected');
            self.updateNavigation($container, $container.find('.s_ss_slider li').eq($n));
        },

        prevSlide: function ($container, $pagination, $n) {
            var self = this,
                    visibleSlide  = $container.find('.s_ss_slider .selected'),
                    navigationDot = $container.find('.s_ss_slider_pagination .selected');

            if (typeof $n === 'undefined') $n = visibleSlide.index() - 1;
            visibleSlide.removeClass('selected')
            $container.find('.s_ss_slider li').eq($n).addClass('selected').removeClass('move-left').nextAll().removeClass('move-left');
            navigationDot.removeClass('selected');
            $pagination.eq($n).addClass('selected');
            self.updateNavigation($container, $container.find('.s_ss_slider li').eq($n));
        },

        updateNavigation: function ($container, $active) {
            $container.find('.s_ss_prev').toggleClass('inactive', $active.is(':first-child'));
            $container.find('.s_ss_next').toggleClass('inactive', $active.is(':last-child'));
        },
    });
});
