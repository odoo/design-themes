
(function(){
    'use strict';

    var website = openerp.website;
    website.openerp_website = {};

    // GARDENIA MAP 
    website.snippet.animationRegistry.s_google_map = website.snippet.Animation.extend({
        selector : "section.s_google_map",

        start : function() {
            var self = this;
            if (typeof google === 'object' && typeof google.maps === 'object') {
                self.redraw();
            }
        },
    
        redraw: function () {
            var self = this;

            //Define a default map's colors set
            var std = [];
            var stdMap = new google.maps.StyledMapType(std, {name: "Std Map"});

            // Default options, will be overwritten by the user 
            var myOptions = { 
                zoom:12,
                center:new google.maps.LatLng(50.854975,4.3753899),
                mapTypeId: google.maps.MapTypeId.ROADMAP,
                panControl: false,
                zoomControl: false,
                mapTypeControl: false,
                streetViewControl: false,
                scrollwheel:false,
                mapTypeControlOptions: {
                  mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'map_style']
                }
            };

            //Render Map
            var mapC    = self.$target.find('.map_container'), 
                map     = new google.maps.Map(mapC.get(0), myOptions);

            //Update GPS position
            var p   =  this.$target.attr('data-map-gps').substring(1).slice(0, -1).split(',');
            var gps =  new google.maps.LatLng( p[0],p[1] );
            map.setCenter(gps);

            //Update Map on screen resize
            google.maps.event.addDomListener(window, 'resize', function() {
                map.setCenter(gps);
            });
            google.maps.event.addDomListener(map, 'resize', function() {
                map.setCenter(gps);
            });

            //Create Marker & Infowindow 
            if(self.$target.attr('data-pin-style') == "flat") {
                var is_internetExplorer11 = navigator.userAgent.toLowerCase().indexOf('trident') > -1;
                var marker_url = (is_internetExplorer11) ? '/snippet_google_map/static/src/img/s_google_map/marker.png' : '/snippet_google_map/static/src/img/marker.svg';

                var marker = new google.maps.Marker({
                    map: map,
                    animation: google.maps.Animation.DROP,
                    position: new google.maps.LatLng(p[0],p[1] ),
                    icon: marker_url
                });
            } else {
                var marker = new google.maps.Marker({
                    map: map,
                    animation: google.maps.Animation.DROP,
                    position: new google.maps.LatLng(p[0],p[1] )
                });
            }

            //Update Map Type
            map.setMapTypeId(google.maps.MapTypeId[self.$target.attr('data-map-type')]);

            //Update Map Zoom
            map.setZoom(parseInt(self.$target.attr('data-map-zoom')));

            //Update Map Color (execute only if a map color palette is not defined)
            if(self.$target.attr('data-map-color') != ""){
                self.update_map_color(map);
            }
        },

        update_map_color: function(map){
            var self = this;
            var mapColor = eval("self." + self.$target.attr('data-map-color'));
            
            var thisMap = new google.maps.StyledMapType(mapColor, {name: "TEST"});
            map.mapTypes.set('map_style', thisMap);
            map.setMapTypeId('map_style');
            
        }


    });
})();