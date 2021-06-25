site_data = {}
customer_data = {'NOEL': {'NOELTESTPROD': {'station_list': 'NOELTEST', 'post_proc': ''}, 'NOELTESTPROD2': {'station_list': 'NOELTEST2', 'post_proc': ''}}, 'GBE': {'GBESOLAROBS': {'station_list': 'gbe_solar_stn', 'post_proc': 'proc_gbe_solar'}}}

wsi_code =  17045
icao_code =  "KCVG"
name =  "COVINGTON"
lat =  39.05
lon =  -84.6667
list_order =  0
start_date = "06/23/2021"
past_date = "06/21/2021"
customerKey =  'GBE'
productKey = 'GBESOLAROBS'

ref = (17912, 'KCLE', 'CLEVELAND       ', 41.4167, -81.8667, 1)

if len(site_data) == 0:
    site_data = {wsi_code : {'metadata' : list(ref)}}
else:
    if wsi_code in site_data:
        site_data[wsi_code]['metadata'] = {list(ref)}
    else:
        site_data[wsi_code]= {'metadata' : list(ref)}

site_data[wsi_code]['APICall'] = {f"http://api.weatheranalytics.com/v2/wsi/metar/[{lat},{lon}]?startDate=${past_date}&endDate=${start_date}&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25"}

#Testing:
if 'stations' in customer_data[customerKey][productKey]:
    customer_data[customerKey][productKey] = {'stations' : {list_order :wsi_code}}
else:
    customer_data[customerKey][productKey]['stations'] = {list_order :wsi_code}

print(f"1. Checkpoint for customer_data = {customer_data}")

wsi_code =  17046
icao_code =  "KCVG"
name =  "COVINGTON"
lat =  39.05
lon =  -84.6667
list_order =  1
start_date = "06/23/2021"
past_date = "06/21/2021"
customerKey =  'GBE'
productKey = 'GBESOLAROBS'

ref = (17447, 'KSTL', 'ST LOUIS/LAMBERT', 38.75, -90.3667, 2)

if len(site_data) == 0:
    site_data = {wsi_code : {'metadata' : list(ref)}}
else:
    if wsi_code in site_data:
        site_data[wsi_code]['metadata'] = list(ref)
    else:
        site_data[wsi_code]= {'metadata' : list(ref)}

site_data[wsi_code]['APICall'] = {f"http://api.weatheranalytics.com/v2/wsi/metar/[{lat},{lon}]?startDate=${past_date}&endDate=${start_date}&interval=hourly&units=imperial&format=xml&userKey=4449f2f578c59aa4eb638a9c5d39ec52&time=lwt&limit=25"}

#Testing:
if 'stations' in customer_data[customerKey][productKey]:
    customer_data[customerKey][productKey]['stations'][list_order] =  wsi_code
else:
    customer_data[customerKey][productKey] = {'stations' : {list_order :wsi_code}}


print(f"2. Checkpoint for customer_data = {customer_data}")

print(f"site_data = {site_data}")
print("\n")
print(f"customer_data = {customer_data}")
