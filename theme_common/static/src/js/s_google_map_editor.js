odoo.define('theme_common.s_google_map_editor', function (require) {
'use strict';

var Dialog = require('web_editor.widget').Dialog;
var core = require('web.core');
var sOptions = require('web_editor.snippets.options');
var googleScriptLoaded = require('theme_common.s_google_map_frontend').googleScriptLoaded;

var _t = core._t;

sOptions.registry.map = sOptions.Class.extend({
    xmlDependencies: ['/theme_common/static/src/xml/s_google_map_modal.xml'],
    defaultLocation: '(50.854975,4.3753899)',

    /**
     * @override
     */
    onBuilt: function () {
        this._super.apply(this, arguments);
        this.map('click', null, null);
    },

    //--------------------------------------------------------------------------
    // Options
    //--------------------------------------------------------------------------

    /**
     * Opens the customization dialog.
     *
     * @see this.selectClass for parameters
     */
    map: function (previewMode, value, $opt) {
        var self = this;

        this.dialog = new Dialog(this, {
            size: 'medium',
            title: _t("Customize your map"),
            buttons: [
                {text: _t("Save"), classes: 'btn-primary', close: true, click: function () {
                    if (!this.$('#placeBk').val()) {
                        this.$('#placeBk').val(self.defaultLocation);
                    }
                    self.$target.attr({
                        'data-map-gps': this.$('#placeBk').val(),
                        'data-pin-style': this.$('#pin_style').val(),
                        'data-pin-address': this.$('#pin_address').val(),
                    });
                    self.trigger_up('animation_start_demand', {
                        editableMode: true,
                        $target: self.$target,
                    });
                }},
                {text: _t("Cancel"), close: true}
            ],
            $content: $(core.qweb.render('theme_common.s_google_map_modal'))
        });

        this.dialog.opened().then((function () {
            this.$('#pin_address').val(self.$target.attr('data-pin-address'));
            this.$('#pin_style').val(self.$target.attr('data-pin-style'));
            this.$('#placeBk').val(self.$target.attr('data-map-gps'));
            var autocomplete = new google.maps.places.Autocomplete(this.$('#pin_address').get(0), {types: ['geocode']});
            google.maps.event.addListener(autocomplete, 'place_changed', function () {
                var place = autocomplete.getPlace();
                self.dialog.$('#placeBk').val(place.geometry ? place.geometry.location : self.defaultLocation);
            });
        }).bind(this.dialog));

        googleScriptLoaded.then(function () {
            self.dialog.open();
        });
    },
    /**
     * Adapts map's type.
     *
     * @see this.selectClass for parameters
     */
    mapType: function (previewMode, value, $opt) {
        this.$target.attr('data-map-type', value);
        this.$target.attr('data-map-color', '');
        this.trigger_up('animation_start_demand', {
            editableMode: true,
            $target: this.$target,
        });
    },
    /**
     * Adapts map's color.
     *
     * @see this.selectClass for parameters
     */
    mapColor: function (previewMode, value, $opt) {
        this.$target.attr('data-map-color', value);
        this.trigger_up('animation_start_demand', {
            editableMode: true,
            $target: this.$target,
        });
    },
    /**
     * Adapts map's zoom.
     *
     * @see this.selectClass for parameters
     */
    mapZoom: function (previewMode, value, $opt) {
        this.$target.attr('data-map-zoom', value);
        this.trigger_up('animation_start_demand', {
            editableMode: true,
            $target: this.$target,
        });
    },
    /**
     * Adapts map's location.
     *
     * @see this.selectClass for parameters
     */
    mapGps: function (previewMode, value, $opt) {
        this.$target.attr('data-map-gps', value);
        this.trigger_up('animation_start_demand', {
            editableMode: true,
            $target: this.$target,
        });
    },

    //--------------------------------------------------------------------------
    // Private
    //--------------------------------------------------------------------------

    /**
     * @override
     */
    _setActive: function () {
        this.$el.find('[data-map-type]')
            .removeClass('active')
            .filter('[data-map-type="' + this.$target.attr('data-map-type') + '"]')
            .addClass('active');
        this.$el.find('[data-map-color]')
            .removeClass('active')
            .filter('[data-map-color="' + this.$target.attr('data-map-color') + '"]')
            .addClass('active');
        this.$el.find('[data-map-zoom]')
            .removeClass('active')
            .filter('[data-map-zoom="' + this.$target.attr('data-map-zoom') + '"]')
            .addClass('active');
        this.$el.find('[data-map-gps]')
            .removeClass('active')
            .filter('[data-map-gps="' + this.$target.attr('data-map-gps') + '"]')
            .addClass('active');
    },
});
});
