# PYOVERLANDER

tools for working with iOverlander tracks

## QUICK START

there are no hard dependencies except for `python3` and `make`

1. request the GPX export from [https://ioverlander.com/countries/places_by_country]
1. check your email and download the linked ZIP file to `./import/<COUNTRY>/`
1. extract the GPX file from the ZIP archive (`unzip <ZIP>`) into the same directory
1. run `make iOverlander.<COUNTRY>.gpx` to add the OSMAnd extensions
1. import the resulting file into OSMAnd on your phone

## ADVANCED

if the make driven workflow is too limiting, you can also run
`./pyoverlander.py <GPX>` to print the converted GPX to stdout.

if you have adb installed/configured and OSMand is configured to store its
tracks in `/storage/emulated/0/Android/media/net.osmand.plus/tracks/`, you
can run `make push` to push the files to your device while plugged in via USB.

## GPX FORMAT

the overall structure is as follows:

```xml
<gpx>
  <wpt ...>
    <extensions>
      <osmand:color>#e044bb</osmand:color>
      <osmand:icon>tourism_camp_site</osmand:icon>
      <osmand:background>circle</osmand:background>
    </extensions>
  </wpt>
</gpx>
```

## OSMAND ICONS

can be extracted from reference GPX

save the reference GPX from osmand to `./import/reference.gpx`

and then run `make print-osmand-icon-map`

for manual extraction, consider:

```shell
$ grep 'osmand:' ./import/reference.gpx
      <osmand:background>circle</osmand:background>
      <osmand:color>#e044bb</osmand:color>
      <osmand:icon>amenity_atm</osmand:icon>
      <osmand:icon>amenity_doctors</osmand:icon>
      <osmand:icon>amenity_drinking_water</osmand:icon>
      <osmand:icon>amenity_fuel_lpg</osmand:icon>
      <osmand:icon>amenity_police</osmand:icon>
      <osmand:icon>amenity_veterinary</osmand:icon>
      <osmand:icon>driving_school</osmand:icon>
      <osmand:icon>fuel</osmand:icon>
      <osmand:icon>internet_access_wlan</osmand:icon>
      <osmand:icon>place_city</osmand:icon>
      <osmand:icon>restaurants</osmand:icon>
      <osmand:icon>sanitary_dump_station</osmand:icon>
      <osmand:icon>shop_car_repair</osmand:icon>
      <osmand:icon>shop_department_store</osmand:icon>
      <osmand:icon>shop_supermarket</osmand:icon>
      <osmand:icon>special_information</osmand:icon>
      <osmand:icon>special_parking_time_limited</osmand:icon>
      <osmand:icon>special_sail_boat</osmand:icon>
      <osmand:icon>special_subway</osmand:icon>
      <osmand:icon>tourism_camp_site</osmand:icon>
      <osmand:icon>tourism_hostel</osmand:icon>
      <osmand:icon>tourism_hotel</osmand:icon>
      <osmand:icon>waste_disposal</osmand:icon>
      <osmand:icon>waterfall</osmand:icon>
      <osmand:icon>wood</osmand:icon>
```
