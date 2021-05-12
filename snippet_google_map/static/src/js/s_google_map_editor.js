odoo.define('snippet_google_map.s_google_map_editor', function (require) {
    'use strict';

    var ajax = require('web.ajax');
    var Dialog = require("web_editor.widget").Dialog;
    var core = require('web.core');
    var s_options = require('web_editor.snippets.options');
    var googleScriptLoaded = require("snippet_google_map.s_google_map_frontend").googleScriptLoaded;

    var _t = core._t;

    ajax.loadXML('/snippet_google_map/static/src/xml/s_google_map_modal.xml', core.qweb);

    s_options.registry.map = s_options.Class.extend({
        default_location: "(50.854975,4.3753899)",

        map: function (previewMode, value, $li) {
            var self = this;

            this.dialog = new Dialog(this, {
                size: "medium",
                title: _t("Customize your map"),
                buttons: [
                    {text: _t("Save"), classes: "btn-primary", close: true, click: function () {
                        if (!this.$("#placeBk").val()) {
                            this.$("#placeBk").val(self.default_location);
                        }
                        self.$target.attr({
                            "data-map-gps": this.$("#placeBk").val(),
                            "data-pin-style": this.$("#pin_style").val(),
                            "data-pin-address": this.$("#pin_address").val(),
                        });
                        self.trigger_up('animation_start_demand', {
                            editableMode: true,
                            $target: self.$target,
                        });
                    }},
                    {text: _t("Cancel"), close: true}
                ],
                $content: $(core.qweb.render("snippet_google_map.s_google_map_modal"))
            });

            this.dialog.opened().then((function () {
                this.$("#pin_address").val(self.$target.attr('data-pin-address'));
                this.$("#pin_style").val(self.$target.attr('data-pin-style'));
                this.$("#placeBk").val(self.$target.attr('data-map-gps'));
                self._rpc({ route: '/website/google_maps_api_key' }).then(function (data) {
                    var data_json = JSON.parse(data);
                    // show link to settings if API Key is missing
                    if (!_.str.trim(data_json.google_maps_api_key)) {
                        this.$('#snippet_google_map_settings_link').removeClass('hidden');
                    }
                }.bind(this));
                var autocomplete = new google.maps.places.Autocomplete(this.$('#pin_address').get(0), {types: ['geocode']});
                google.maps.event.addListener(autocomplete, 'place_changed', function () {
                    var place = autocomplete.getPlace();
                    self.dialog.$("#placeBk").val(place.geometry ? place.geometry.location : self.default_location);
                });
            }).bind(this.dialog));

            googleScriptLoaded.then(function () {
                self.dialog.open();
            });
        },

        map_type: function (previewMode, value, $li) {
            this.$target.attr('data-map-type', value);
            this.$target.attr('data-map-color', "");
            this.trigger_up('animation_start_demand', {
                editableMode: true,
                $target: this.$target,
            });
        },

        map_color: function (previewMode, value, $li) {
            this.$target.attr('data-map-color', value);
            this.trigger_up('animation_start_demand', {
                editableMode: true,
                $target: this.$target,
            });
        },

        map_zoom: function (previewMode, value, $li) {
            this.$target.attr('data-map-zoom', value);
            this.trigger_up('animation_start_demand', {
                editableMode: true,
                $target: this.$target,
            });
        },

        map_gps: function (previewMode, value, $li) {
            this.$target.attr('data-map-gps', value);
            this.trigger_up('animation_start_demand', {
                editableMode: true,
                $target: this.$target,
            });
        },

        _setActive: function () {
            this.$el.find('[data-map_type]')
                .removeClass('active')
                .filter('[data-map_type="'+this.$target.attr('data-map-type')+'"]')
                .addClass('active');
            this.$el.find('[data-map_color]')
                .removeClass('active')
                .filter('[data-map_color="'+this.$target.attr('data-map-color')+'"]')
                .addClass('active');
            this.$el.find('[data-map_zoom]')
                .removeClass('active')
                .filter('[data-map_zoom="'+this.$target.attr('data-map-zoom')+'"]')
                .addClass('active');
            this.$el.find('[data-map_gps]')
                .removeClass('active')
                .filter('[data-map_gps="'+this.$target.attr('data-map-gps')+'"]')
                .addClass('active');
        },

        onBuilt: function () {
            this._super.apply(this, arguments);
            this.map('click', null, null);
        },
    });
});
