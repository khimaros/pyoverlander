#!/usr/bin/env python3

import sys
import xmltodict

PRINT_OSMAND_ICON_MAP = False
if sys.argv[1] == '-m':
    PRINT_OSMAND_ICON_MAP = True
    sys.argv.pop(1)

input_path = sys.argv[1]

OSMAND_ICON_BACKGROUND = 'circle'
OSMAND_ICON_COLOR = '#e044bb'
OSMAND_ICON_MAP = {
        'Checkpoint': 'amenity_police',
        'Customs and Immigration': 'amenity_police',
        'Eco-Friendly': 'waste_disposal',
        'Established Campground': 'tourism_camp_site',
        'Financial': 'amenity_atm',
        'Fuel Station': 'fuel',
        'Hostel': 'tourism_hostel',
        'Hotel': 'tourism_hotel',
        'Informal Campsite': 'place_city',
        'Laundromat': 'shop_department_store',
        'Mechanic and Parts': 'shop_car_repair',
        'Medical': 'amenity_doctors',
        'Pet Services': 'amenity_veterinary',
        'Propane': 'amenity_fuel_lpg',
        'Restaurant': 'restaurants',
        'Sanitation Dump Station': 'sanitary_dump_station',
        'Shopping': 'shop_supermarket',
        'Short-term Parking': 'special_parking_time_limited',
        'Showers': 'waterfall',
        'Vehicle Insurance': 'driving_school',
        'Vehicle Shipping': 'special_sail_boat',
        'Vehicle Storage': 'special_subway',
        'Warning': 'special_information',
        'Water': 'amenity_drinking_water',
        'Wifi': 'internet_access_wlan',
        'Wild Camping': 'wood',
}

def print_osmand_icon_map(wpts):
    osmand_icon_map = {}
    for wpt in wpts:
        #print(wpt)
        wpt_type = wpt['type']
        osmand_icon = wpt.get('extensions', {}).get('osmand:icon')
        if osmand_icon:
            osmand_icon_map[wpt_type] = osmand_icon
    import pprint
    pprint.pprint(osmand_icon_map)


with open(input_path, 'rb') as f:
    xml = xmltodict.parse(f)

    gpx = xml.get('gpx', {})
    gpx['@xmlns:osmand'] = 'https://osmand.net'
    wpts = gpx.get('wpt', [])

    # TODO: make this a flag instead of hardcoded
    if PRINT_OSMAND_ICON_MAP:
        print_osmand_icon_map(wpts)

    else:
        for wpt in wpts:
            wpt_type = wpt['type']
            osmand_icon = OSMAND_ICON_MAP.get(wpt_type)
            if 'extensions' not in wpt:
                wpt['extensions'] = {}
            wpt['extensions']['osmand:background'] = OSMAND_ICON_BACKGROUND
            wpt['extensions']['osmand:color'] = OSMAND_ICON_COLOR
            if osmand_icon:
                wpt['extensions']['osmand:icon'] = osmand_icon

        output_data = xmltodict.unparse(xml, pretty=True, newl='\r\n')
        print(output_data)
