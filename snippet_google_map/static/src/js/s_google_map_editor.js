(function(){
    'use strict';

    var website = openerp.website;

    website.add_template_file('/snippet_google_map/static/src/xml/s_google_map_modal.xml');

    website.openerp_website = {};
    
    website.snippet.options.map = website.snippet.Option.extend({
        
        map: function (type, value, $li) {
            if (type !== 'click') return;
            var self = this;  
            self.$modal = $(openerp.qweb.render("snippet_google_map.s_google_map_modal"));
            self.$modal.appendTo('body');           
            self.$modal.modal();

            self.$modal.on('shown.bs.modal', function () {
                self.$modal.find("#pin_title").val(self.$target.attr('data-pin-title'));
                self.$modal.find("#pin_style").val(self.$target.attr('data-pin-style'));
                var autocomplete = new google.maps.places.Autocomplete((self.$modal.find('#pin_address').get(0)),{ types: ['geocode'] });               
                google.maps.event.addListener(autocomplete, 'place_changed', function() {
                    var place = autocomplete.getPlace();
                    if (!place.geometry) {
                      self.$modal.find("#placeBk").val("(50.854975,4.3753899)");
                    } else {
                        self.$modal.find("#placeBk").val(place.geometry.location);
                    }
                });
            });

            self.$modal.find("#sub_map").on('click', function () {
                if (!self.$modal.find("#placeBk").val()) {
                    self.$modal.find("#placeBk").val("(50.854975,4.3753899)")
                }         
                self.$target.attr('data-map-gps', (self.$modal.find("#placeBk").val()));         
                self.$target.attr('data-pin-style', (self.$modal.find("#pin_style").val()));
                self.$modal.modal('hide');
                self.$target.data('snippet-view').redraw();             
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
            this.map('click', null, null);
        },
        start: function () {
          this.$target.data('snippet-view').redraw();
        }
    });

})();
