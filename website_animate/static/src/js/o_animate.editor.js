odoo.define('website_animate.o_animate_editor', function (require) {
'use strict';

var sOptions = require('web_editor.snippets.options');

function forceAnimation() {
    var $els = $();
    _.each(arguments, function (el) {
        $els = $els.add(el);
    });
    $els.css('animation-name', 'dummy');
    void $els[0].offsetWidth;
    $els.css('animation-name', '');
}

//  Animations
sOptions.registry.o_animate = sOptions.Class.extend({
    /**
     * @override
     */
    onFocus: function () {
        this._setActive(); // Needed as in charge of hiding duration/delay/...
    },
    /**
     * @override
     */
    cleanForSave: function () {
        // Clean elements
        this.$target.removeClass('o_animating o_animated o_animate_preview')
                    .css({
                        'animation': '',
                        'animation-name': '',
                        'animation-play-state': '',
                        'visibility': '',
                    });
        if (this.$target.hasClass('o_animate')) {
            this.$target.css('animation-play-state', 'paused');
        }

        // Clean all inView elements
        $('#wrapwrap').find('.o_animate').removeClass('o_visible');
    },

    //--------------------------------------------------------------------------
    // Options
    //--------------------------------------------------------------------------

    /**
     * @override
     */
    selectClass: function (previewMode, value, $opt) {
        this._super.apply(this, arguments);
        forceAnimation(this.$target);
        this.$target.toggleClass('o_animate_preview o_animate', !!value);
    },

    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * @override
     */
    _setActive: function () {
        this._super.apply(this, arguments);
        this.$overlay.data('$optionsSection').find('.snippet-option-o_animate_duration, .snippet-option-o_animate_delay, .snippet-option-o_animate_options')
                     .toggleClass('d-none', this.$el.find('.active').length === 0);
    },
});

var Common = sOptions.Class.extend({

    __animateOptionType: undefined,

    //--------------------------------------------------------------------------
    // Options
    //--------------------------------------------------------------------------

    /**
     * @override
     */
    selectClass: function (previewMode, value, $opt) {
        this._super.apply(this, arguments);

        var $timeline_delay = this.$overlay.data('$optionsSection').find('.timeline' + this.__animateOptionType + ' span[simulate="delay"]');
        var $timeline_duration = this.$overlay.data('$optionsSection').find('.timeline' + this.__animateOptionType + ' span[simulate="duration"]');

        this.$target.css({
            'animation-duration': '',
            'animation-delay': '',
        });

        var el_duration = parseFloat(this.$target.css('animation-duration').slice(0, -1));
        var el_delay = parseFloat(this.$target.css('animation-delay').slice(0, -1));
        var el_period = el_delay + el_duration;

        $timeline_duration.parent().width((el_duration*100)/el_period + '%');
        $timeline_delay.parent().width((el_delay*100)/el_period + '%');
        $timeline_duration.css('animation-duration', el_duration + 's').css('animation-delay', el_delay + 's');
        $timeline_delay.css('animation-duration', el_delay + 's');

        forceAnimation($timeline_duration, $timeline_delay, this.$target);
        this.$target.addClass('o_animate_preview');
    },
});

// Duration
sOptions.registry.o_animate_duration = Common.extend({
    __animateOptionType: '.duration',
});

// Delay
sOptions.registry.o_animate_delay = Common.extend({
    __animateOptionType: '.delay',
});
});
