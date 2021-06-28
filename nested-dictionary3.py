import requests
import xml


site_data = {17045: {'metadata': [17045, 'KCVG', 'COVINGTON       ', 39.05, -84.6667, 0], 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[39.05,-84.6667]?startDate=$06/22/2021&endDate=$06/24/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 17912: {'metadata': [17912, 'KCLE', 'CLEVELAND       ', 41.4167, -81.8667, 1], 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[41.4167,-81.8667]?startDate=$06/22/2021&endDate=$06/24/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 17447: {'metadata': [17447, 'KSTL', 'ST LOUIS/LAMBERT', 38.75, -90.3667, 2], 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[38.75,-90.3667]?startDate=$06/22/2021&endDate=$06/24/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 16986: {'metadata': [16986, 'KIND', 'INDIANAPOLIS    ', 39.7333, -86.2667, 3], 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[39.7333,-86.2667]?startDate=$06/22/2021&endDate=$06/24/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 17246: {'metadata': [17246, 'KDTW', 'DETROIT/WAYNE   ', 42.2333, -83.3333, 4], 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[42.2333,-83.3333]?startDate=$06/22/2021&endDate=$06/24/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 17370: {'metadata': [17370, 'KMSP', 'MINNEAPOLIS     ', 44.8833, -93.2167, 5], 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[44.8833,-93.2167]?startDate=$06/22/2021&endDate=$06/24/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 17857: {'metadata': [17857, 'KNYC', 'NYC/CENTRAL PARK', 40.7833, -73.9667, 6], 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[40.7833,-73.9667]?startDate=$06/22/2021&endDate=$06/24/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 17161: {'metadata': [17161, 'KBWI', 'BALTIMORE/INTL  ', 39.1833, -76.6667, 7], 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[39.1833,-76.6667]?startDate=$06/22/2021&endDate=$06/24/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 18414: {'metadata': [18414, 'KORF', 'NORFOLK         ', 36.9, -76.2, 8], 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[36.9,-76.2]?startDate=$06/22/2021&endDate=$06/24/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 18418: {'metadata': [18418, 'KRIC', 'RICHMOND        ', 37.5, -77.3333, 9], 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[37.5,-77.3333]?startDate=$06/22/2021&endDate=$06/24/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 16684: {'metadata': [16684, 'KDCA', 'WASHINGTON/NATL ', 38.85, -77.0333, 10], 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[38.85,-77.0333]?startDate=$06/22/2021&endDate=$06/24/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 18598: {'metadata': [18598, 'KCRW', 'CHARLESTON      ', 38.3667, -81.6, 11], 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[38.3667,-81.6]?startDate=$06/22/2021&endDate=$06/24/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 17684: {'metadata': [17684, 'KACY', 'ATLANTIC CITY   ', 39.45, -74.5667, 12], 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[39.45,-74.5667]?startDate=$06/22/2021&endDate=$06/24/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 18090: {'metadata': [18090, 'KPIT', 'PITTSBURGH      ', 40.5, -80.2167, 13], 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[40.5,-80.2167]?startDate=$06/22/2021&endDate=$06/24/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 18044: {'metadata': [18044, 'KABE', 'ALLENTOWN       ', 40.65, -75.4333, 14], 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[40.65,-75.4333]?startDate=$06/22/2021&endDate=$06/24/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 17697: {'metadata': [17697, 'KEWR', 'NEWARK          ', 40.7, -74.1667, 15], 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[40.7,-74.1667]?startDate=$06/22/2021&endDate=$06/24/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 17921: {'metadata': [17921, 'KDAY', 'DAYTON          ', 39.9, -84.2, 16], 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[39.9,-84.2]?startDate=$06/22/2021&endDate=$06/24/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 17917: {'metadata': [17917, 'KCMH', 'COLUMBUS        ', 40.0, -82.8833, 17], 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[40.0,-82.8833]?startDate=$06/22/2021&endDate=$06/24/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 18085: {'metadata': [18085, 'KPHL', 'PHILADELPHIA    ', 39.8833, -75.25, 18], 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[39.8833,-75.25]?startDate=$06/22/2021&endDate=$06/24/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}, 18420: {'metadata': [18420, 'KROA', 'ROANOKE         ', 37.3167, -79.9667, 19], 'APICall': 'http://api.weatheranalytics.com/v2/wsi/metar/[37.3167,-79.9667]?startDate=$06/22/2021&endDate=$06/24/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'}}

agent = {'env_proxy':1, 'keep_alive':1, 'timeout':30}

call = 'http://api.weatheranalytics.com/v2/wsi/metar/[39.45,-74.5667]?startDate=06/22/2021&endDate=06/24/2021&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25'

#response = requests.get(call,timeout=30)
response = requests.get(call,params=agent)
print(response.content)
print(response.headers)
print(response.status_code)
print(response.connection)

print("use another way to get content....")
print(response.content.decode("utf-8"))


call = 'http://api.weatheranalytics.com/test'
try:
    response = requests.get(call)
    response.raise_for_status()
    # Additional code will only run if the request is successful
except requests.exceptions.HTTPError as error:
    print(error)
    # This code will run if there is a 404 error.

"""
my $agent = LWP::UserAgent->new(env_proxy => 1, keep_alive => 1, timeout => 30);
my $header = HTTP::Request->new(GET => $call );
my $request = HTTP::Request->new('GET',$call, $header);

my $site_pulled_succesfully = 0;
my $num_attempts = 0;
"""
"""
for site in site_data:
    #print(f"The dic. Key is {site} and the value is {site_data[site]}")
    call = site_data[site]['APICall']
    print("call = ", call)
"""
