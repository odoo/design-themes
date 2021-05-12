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

        map: function (type, value, $li) {
            if (type !== 'click') return;
            var self = this;

            this.dialog = new Dialog(null, {
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
                        self.$target.data("snippet-view").redraw();
                    }},
                    {text: _t("Cancel"), close: true}
                ],
                $content: $(core.qweb.render("snippet_google_map.s_google_map_modal"))
            });

            this.dialog.opened().then((function () {
                this.$("#pin_address").val(self.$target.attr('data-pin-address'));
                this.$("#pin_style").val(self.$target.attr('data-pin-style'));
                this.$("#placeBk").val(self.$target.attr('data-map-gps'));
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

        map_type: function (type, value, $li) {
            if (type !== 'click') return;
            this.$target.attr('data-map-type', value);
            this.$target.attr('data-map-color', "");
            this.$target.data('snippet-view').redraw();
        },

        map_color: function (type, value, $li) {
            if (type !== 'click') return;
            this.$target.attr('data-map-color', value);
            this.$target.data('snippet-view').redraw();
        },

        map_zoom: function (type, value, $li) {
            if (type !== 'click') return;
            this.$target.attr('data-map-zoom', value);
            this.$target.data('snippet-view').redraw();
        },

        map_gps: function (type, value, $li) {
            this.$target.attr('data-map-gps', value);
            this.$target.data('snippet-view').redraw();
        },

        set_active: function () {
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

        drop_and_build_snippet: function () {
            this._super.apply(this, arguments);
            this.map('click', null, null);
        },
    });
});
