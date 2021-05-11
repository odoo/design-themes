odoo.define('snippet_google_map.s_google_map_frontend', function (require) {
    'use strict';

    var sAnimation = require('website.content.snippets.animation');
    var googleScriptLoaded = $.Deferred();

    sAnimation.registry.s_google_map = sAnimation.Class.extend({
        selector: 'section.s_google_map',

        start: function () {
            var defs = [this._super.apply(this, arguments)];
            if (typeof google !== 'object' || typeof google.maps !== 'object') {
                if (!sAnimation.registry.s_google_map.isScriptLoading) {
                    sAnimation.registry.s_google_map.isScriptLoading = true;
                    window.odoo_snippet_google_map_redraw_all = function odoo_snippet_google_map_redraw_all() {
                        _.each($('section.s_google_map'), function (map) {
                            $(map).data('snippet-view') && $(map).data('snippet-view').redraw();
                        });
                        sAnimation.registry.s_google_map.isScriptLoading = false;
                        googleScriptLoaded.resolve();
                    };

                    defs.push(this._rpc({
                        route: '/website/google_maps_api_key',
                    }).then(function (data) {
                        var key_param = '';
                        var data_json = JSON.parse(data);
                        if (data_json.google_maps_api_key !== '') {
                            key_param = '&key=' + data_json.google_maps_api_key;
                        }
                        $('head').append($('<script/>', {
                            type: "text/javascript",
                            src: "https://maps.googleapis.com/maps/api/js?v=3.exp&libraries=places&callback=odoo_snippet_google_map_redraw_all" + key_param,
                        }));
                    }));
                }
            } else {
                this.redraw();
            }
            return $.when.apply($, defs);
        },

        redraw: function () {
            // Define a default map's colors set
            var std = [];
            new google.maps.StyledMapType(std, {name: "Std Map"});

            // Default options, will be overwritten by the user
            var myOptions = {
                zoom: 12,
                center: new google.maps.LatLng(50.854975,4.3753899),
                mapTypeId: google.maps.MapTypeId.ROADMAP,
                panControl: false,
                zoomControl: false,
                mapTypeControl: false,
                streetViewControl: false,
                scrollwheel: false,
                mapTypeControlOptions: {
                    mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'map_style']
                }
            };

            // Render Map
            var mapC = this.$target.find('.map_container');
            var map = new google.maps.Map(mapC.get(0), myOptions);

            // Update GPS position
            var p = this.$target.attr('data-map-gps').substring(1).slice(0, -1).split(',');
            var gps = new google.maps.LatLng(p[0], p[1]);
            map.setCenter(gps);

            // Update Map on screen resize
            google.maps.event.addDomListener(window, 'resize', function () {
                map.setCenter(gps);
            });

            // Create Marker & Infowindow
            if (this.$target.attr('data-pin-style') === "flat") {
                new google.maps.Marker({
                    map: map,
                    animation: google.maps.Animation.DROP,
                    position: new google.maps.LatLng(p[0],p[1]),
                    icon: "/snippet_google_map/static/src/img/marker.png",
                });
            } else {
                new google.maps.Marker({
                    map: map,
                    animation: google.maps.Animation.DROP,
                    position: new google.maps.LatLng(p[0], p[1])
                });
            }

            map.setMapTypeId(google.maps.MapTypeId[this.$target.attr('data-map-type')]); // Update Map Type
            map.setZoom(parseInt(this.$target.attr('data-map-zoom'))); // Update Map Zoom

            // Update Map Color
            if (this.$target.attr('data-map-color') !== "") {
                this.update_map_color(map);
            }
        },

        update_map_color: function (map) {
            var mapColor = eval("this." + this.$target.attr('data-map-color'));
            var thisMap = new google.maps.StyledMapType(mapColor, {name: "Styled Map"});
            map.mapTypes.set('map_style', thisMap);
            map.setMapTypeId('map_style');
        },
    });

    // This prototype permit to save if the google maps script is already loading or not.
    // This script cannot be loaded 2 times, so if we have 2 snippets in the same view
    // we don't want to call 2 times the scripts because the first one is not finished.
    // And we cannot put in in an asset because we don't want to load this script on each
    // page, but only page with a google maps snippet...
    sAnimation.registry.s_google_map.prototype.isScriptLoading = false;

    return {
        googleScriptLoaded: googleScriptLoaded,
    };
});
