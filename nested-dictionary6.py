import xml.etree.ElementTree as ET

myxml = """
<ApiResponse>
<Head>
<Code>200</Code>
<Message>success</Message>
<StartDate>06/28/2021 00:00:00</StartDate>
<EndDate>06/29/2021 23:00:00</EndDate>
<Site id="2173289018">
<Longitude>-80.05582</Longitude>
<Latitude>37.23566</Latitude>
<Resolution>30</Resolution>
<elevationMeters>549.0</elevationMeters>
<elevationFeet>1801.0</elevationFeet>
<timeZone>America/New_York</timeZone>
</Site>
</Head>
<WeatherData>
<Hours>
<Hour dateHrGmt="06/28/2021 04:00:00" dateHrLwt="06/28/2021 00:00:00">
<SurfaceTemperatureFahrenheit>63.3</SurfaceTemperatureFahrenheit>
<SurfaceDewpointTemperatureFahrenheit>68.8</SurfaceDewpointTemperatureFahrenheit>
<SurfaceWetBulbTemperatureFahrenheit>50.5</SurfaceWetBulbTemperatureFahrenheit>
</Hour>
<Hour dateHrGmt="06/28/2021 05:00:00" dateHrLwt="06/28/2021 00:00:00">
<SurfaceTemperatureFahrenheit>65.5</SurfaceTemperatureFahrenheit>
<SurfaceDewpointTemperatureFahrenheit>69.9</SurfaceDewpointTemperatureFahrenheit>
<SurfaceWetBulbTemperatureFahrenheit>61.5</SurfaceWetBulbTemperatureFahrenheit>
</Hour>
</Hours>
</WeatherData>
</ApiResponse>
"""

site_data = {17045: {'metadata': {'wsi_code': 17045, 'icao_code': 'KCVG', 'name': 'COVINGTON', 'latitude': 39.05, 'longitude': -84.6667, 'list_order': 0}, 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[39.05,-84.6667]?startDate=06/28/2021&endDate=06/30/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 17912: {'metadata': {'wsi_code': 17912, 'icao_code': 'KCLE', 'name': 'CLEVELAND', 'latitude': 41.4167, 'longitude': -81.8667, 'list_order': 1}, 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[41.4167,-81.8667]?startDate=06/28/2021&endDate=06/30/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 17447: {'metadata': {'wsi_code': 17447, 'icao_code': 'KSTL', 'name': 'ST LOUIS/LAMBERT', 'latitude': 38.75, 'longitude': -90.3667, 'list_order': 2}, 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[38.75,-90.3667]?startDate=06/28/2021&endDate=06/30/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 16986: {'metadata': {'wsi_code': 16986, 'icao_code': 'KIND', 'name': 'INDIANAPOLIS', 'latitude': 39.7333, 'longitude': -86.2667, 'list_order': 3}, 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[39.7333,-86.2667]?startDate=06/28/2021&endDate=06/30/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 17246: {'metadata': {'wsi_code': 17246, 'icao_code': 'KDTW', 'name': 'DETROIT/WAYNE', 'latitude': 42.2333, 'longitude': -83.3333, 'list_order': 4}, 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[42.2333,-83.3333]?startDate=06/28/2021&endDate=06/30/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 17370: {'metadata': {'wsi_code': 17370, 'icao_code': 'KMSP', 'name': 'MINNEAPOLIS', 'latitude': 44.8833, 'longitude': -93.2167, 'list_order': 5}, 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[44.8833,-93.2167]?startDate=06/28/2021&endDate=06/30/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 17857: {'metadata': {'wsi_code': 17857, 'icao_code': 'KNYC', 'name': 'NYC/CENTRAL PARK', 'latitude': 40.7833, 'longitude': -73.9667, 'list_order': 6}, 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[40.7833,-73.9667]?startDate=06/28/2021&endDate=06/30/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 17161: {'metadata': {'wsi_code': 17161, 'icao_code': 'KBWI', 'name': 'BALTIMORE/INTL', 'latitude': 39.1833, 'longitude': -76.6667, 'list_order': 7}, 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[39.1833,-76.6667]?startDate=06/28/2021&endDate=06/30/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 18414: {'metadata': {'wsi_code': 18414, 'icao_code': 'KORF', 'name': 'NORFOLK', 'latitude': 36.9, 'longitude': -76.2, 'list_order': 8}, 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[36.9,-76.2]?startDate=06/28/2021&endDate=06/30/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 18418: {'metadata': {'wsi_code': 18418, 'icao_code': 'KRIC', 'name': 'RICHMOND', 'latitude': 37.5, 'longitude': -77.3333, 'list_order': 9}, 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[37.5,-77.3333]?startDate=06/28/2021&endDate=06/30/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 16684: {'metadata': {'wsi_code': 16684, 'icao_code': 'KDCA', 'name': 'WASHINGTON/NATL', 'latitude': 38.85, 'longitude': -77.0333, 'list_order': 10}, 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[38.85,-77.0333]?startDate=06/28/2021&endDate=06/30/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 18598: {'metadata': {'wsi_code': 18598, 'icao_code': 'KCRW', 'name': 'CHARLESTON', 'latitude': 38.3667, 'longitude': -81.6, 'list_order': 11}, 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[38.3667,-81.6]?startDate=06/28/2021&endDate=06/30/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 17684: {'metadata': {'wsi_code': 17684, 'icao_code': 'KACY', 'name': 'ATLANTIC CITY', 'latitude': 39.45, 'longitude': -74.5667, 'list_order': 12}, 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[39.45,-74.5667]?startDate=06/28/2021&endDate=06/30/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 18090: {'metadata': {'wsi_code': 18090, 'icao_code': 'KPIT', 'name': 'PITTSBURGH', 'latitude': 40.5, 'longitude': -80.2167, 'list_order': 13}, 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[40.5,-80.2167]?startDate=06/28/2021&endDate=06/30/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 18044: {'metadata': {'wsi_code': 18044, 'icao_code': 'KABE', 'name': 'ALLENTOWN', 'latitude': 40.65, 'longitude': -75.4333, 'list_order': 14}, 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[40.65,-75.4333]?startDate=06/28/2021&endDate=06/30/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 17697: {'metadata': {'wsi_code': 17697, 'icao_code': 'KEWR', 'name': 'NEWARK', 'latitude': 40.7, 'longitude': -74.1667, 'list_order': 15}, 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[40.7,-74.1667]?startDate=06/28/2021&endDate=06/30/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 17921: {'metadata': {'wsi_code': 17921, 'icao_code': 'KDAY', 'name': 'DAYTON', 'latitude': 39.9, 'longitude': -84.2, 'list_order': 16}, 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[39.9,-84.2]?startDate=06/28/2021&endDate=06/30/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 17917: {'metadata': {'wsi_code': 17917, 'icao_code': 'KCMH', 'name': 'COLUMBUS', 'latitude': 40.0, 'longitude': -82.8833, 'list_order': 17}, 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[40.0,-82.8833]?startDate=06/28/2021&endDate=06/30/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 18085: {'metadata': {'wsi_code': 18085, 'icao_code': 'KPHL', 'name': 'PHILADELPHIA', 'latitude': 39.8833, 'longitude': -75.25, 'list_order': 18}, 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[39.8833,-75.25]?startDate=06/28/2021&endDate=06/30/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 18420: {'metadata': {'wsi_code': 18420, 'icao_code': 'KROA', 'name': 'ROANOKE', 'latitude': 37.3167, 'longitude': -79.9667, 'list_order': 19}, 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[37.3167,-79.9667]?startDate=06/28/2021&endDate=06/30/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}}



def ParseFormattedDateTime(date_str):
    print("---------ParseFormattedDateTime-----------")

    #OLD: 10/17/2015 5:00:00 AM ->  2015-10-17T05:00:00Z

    #NEW1: 2015-10-17 05:00:00.0 ->  2015-10-17T05:00:00Z
    #NEW2: 10/20/2015 05:00:00

    # check if the input is in the format of "2015-10-17 05:00:00.0"

    print("Input => date_str = ", date_str)
    if date_str.find("-") != -1 :
        date_str
        date_str = re.sub(r'.(\d+)$','Z',date_str)
        date_str = re.sub('(\s)','T',date_str)
        return date_str

    #otherwise, the format is "10/20/2015 05:00:00"
    print("date_str = ", date_str)
    time_parts = date_str.split(" ")
    print("time_parts = ", time_parts)
    date = ""
    time = time_parts[1]

    date_parts = []
    date_parts = time_parts[0].split("/")
    print("date_parts = ", date_parts)

    mm = ('%02d' %int(date_parts[0]))
    dd = ('%02d' %int(date_parts[1]))
    yyyy = int(date_parts[2])
    print(f"{yyyy}-{mm}-{dd}T{time}Z")
    return f"{yyyy}-{mm}-{dd}T{time}Z"

def ParseWXA_XML(site_id,data_response):
    tree = ET.fromstring(myxml)
    root = tree
    valid_time = ''
    for record in root.iter():
        print(record.tag, record.attrib)

        if record.tag == 'Hour':
            record_hash = record.attrib['dateHrGmt']
            lvalid_time = ParseFormattedDateTime(record_hash)
            valid_time = lvalid_time
            print("valid_time = ", valid_time)
            print(f"record.tag = {record.tag} , record.attrib = {record.attrib}")
            print("record.attrib['dateHrGmt'] = ", record.attrib['dateHrGmt'])
            print("record.attrib['dateHrLwt'] = ", record.attrib['dateHrLwt'])


            if 'obs' in site_data[site_id]:
                print("obs exist")
                site_data[site_id]['obs'][valid_time] = {'dateHrGmt':record.attrib['dateHrGmt']}
                site_data[site_id]['obs'][valid_time]['dateHrLwt'] = record.attrib['dateHrLwt']

            else:
                print("no obs exist")
                site_data[site_id]['obs'] = {valid_time : {'dateHrGmt':record.attrib['dateHrGmt']}}
                site_data[site_id]['obs'][valid_time ]['dateHrLwt'] = record.attrib['dateHrLwt']



        else:
            print(record.tag, record.text)
            if record.tag == 'SurfaceTemperatureFahrenheit':
                if 'obs' in site_data[site_id]:
                    site_data[site_id]['obs'][valid_time]['SurfaceTemperatureFahrenheit'] = float(record.text)
                else:
                    site_data[site_id]['obs'] = {valid_time : {'SurfaceTemperatureFahrenheit':float(record.text)}}

            if record.tag == 'SurfaceDewpointTemperatureFahrenheit':
                if 'obs' in site_data[site_id]:
                    site_data[site_id]['obs'][valid_time]['SurfaceDewpointTemperatureFahrenheit'] = float(record.text)
                else:
                    site_data[site_id]['obs'] = {valid_time : {'SurfaceDewpointTemperatureFahrenheit':float(record.text)}}

            if record.tag == 'RelativeHumidityPercent':
                if 'obs' in site_data[site_id]:
                    site_data[site_id]['obs'][valid_time]['RelativeHumidityPercent'] = float(record.text)
                else:
                    site_data[site_id]['obs'] = {valid_time:{'RelativeHumidityPercent':float(record.text)}}

            if record.tag == 'ApparentTemperatureFahrenheit':
                if 'obs' in site_data[site_id]:
                    site_data[site_id]['obs'][valid_time]['ApparentTemperatureFahrenheit'] = float(record.text)
                else:
                    site_data[site_id]['obs'] = {valid_time:{'ApparentTemperatureFahrenheit':float(record.text)}}

            if record.tag == 'WindChillTemperatureFahrenheit':
                if 'obs' in site_data[site_id]:
                    site_data[site_id]['obs'][valid_time]['WindChillTemperatureFahrenheit'] = float(record.text)
                else:
                    site_data[site_id]['obs'] = {valid_time:{'WindChillTemperatureFahrenheit':float(record.text)}}

            if record.tag == 'CloudCoveragePercent':
                if 'obs' in site_data[site_id]:
                    site_data[site_id]['obs'][valid_time]['CloudCoveragePercent'] = float(record.text)
                else:
                    site_data[site_id]['obs'] = {valid_time:{'CloudCoveragePercent':float(record.text)}}

            if record.tag == 'SurfaceWetBulbTemperatureFahrenheit':
                if 'obs' in site_data[site_id]:
                    site_data[site_id]['obs'][valid_time]['SurfaceWetBulbTemperatureFahrenheit'] = float(record.text)
                else:
                    site_data[site_id]['obs'] = {valid_time:{'SurfaceWetBulbTemperatureFahrenheit':float(record.text)}}

            if record.tag == 'PrecipitationPreviousHourInches':
                if 'obs' in site_data[site_id]:
                    site_data[site_id]['obs'][valid_time]['PrecipitationPreviousHourInches'] = float(record.text)
                else:
                    site_data[site_id]['obs'] = {valid_time:{'PrecipitationPreviousHourInches':float(record.text)}}

            if record.tag == 'WindSpeedMph':
                if 'obs' in site_data[site_id]:
                    site_data[site_id]['obs'][valid_time]['WindSpeedMph'] = float(record.text)
                else:
                    site_data[site_id]['obs'] = {valid_time:{'WindSpeedMph':float(record.text)}}

            if record.tag == 'WindDirectionDegrees':
                if 'obs' in site_data[site_id]:
                    site_data[site_id]['obs'][valid_time]['WindDirectionDegrees'] = float(record.text)
                else:
                    site_data[site_id]['obs'] = {valid_time:{'WindDirectionDegrees':float(record.text)}}

            if record.tag == 'DirectNormalIrradianceWsqm':
                if 'obs' in site_data[site_id]:
                    site_data[site_id]['obs'][valid_time]['DirectNormalIrradianceWsqm'] = float(record.text)
                else:
                    site_data[site_id]['obs'] = {valid_time:{'DirectNormalIrradianceWsqm':float(record.text)}}

            if record.tag == 'MslPressureMillibars':
                if 'obs' in site_data[site_id]:
                    site_data[site_id]['obs'][valid_time]['MslPressureMillibars'] = float(record.text)
                else:
                    site_data[site_id]['obs'] = {valid_time:{'MslPressureMillibars':float(record.text)}}

            if record.tag == 'DownwardSolarRadiationWsqm':
                if 'obs' in site_data[site_id]:
                    site_data[site_id]['obs'][valid_time]['DownwardSolarRadiationWsqm'] = float(record.text)
                else:
                    site_data[site_id]['obs'] = {valid_time:{'DownwardSolarRadiationWsqm':float(record.text)}}

            if record.tag == 'DiffuseHorizontalRadiationWsqm':
                if 'obs' in site_data[site_id]:
                    site_data[site_id]['obs'][valid_time]['DiffuseHorizontalRadiationWsqm'] = float(record.text)
                else:
                    site_data[site_id]['obs'] = {valid_time:{'DiffuseHorizontalRadiationWsqm':float(record.text)}}


for site in site_data:
    ParseWXA_XML(site, myxml)

print("======================")
print(site_data)
