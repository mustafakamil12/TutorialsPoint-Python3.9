customer_data = {'NOEL': {'NOELTESTPROD': {'station_list': 'NOELTEST', 'post_proc': ''}, 'NOELTESTPROD2': {'station_list': 'NOELTEST2', 'post_proc': ''}}, 'GBE': {'GBESOLAROBS': {'station_list': 'gbe_solar_stn', 'post_proc': 'proc_gbe_solar'}}}

customerKey = 'NOEL'
productKey = 'NOELTESTPROD'
list_order = 1
wsi_code = 1979

key_to_lookup = 'stations'
if key_to_lookup in customer_data[customerKey][productKey]:
    customer_data[customerKey][productKey]['stations'][list_order] =  wsi_code
else:
    customer_data[customerKey][productKey]['stations'] = {list_order:wsi_code}

print(f"customer_data = {customer_data}")
#print(f"site_data = {site_data}")

customerKey = 'NOEL'
productKey = 'NOELTESTPROD'
list_order = 3
wsi_code = 2016

key_to_lookup = 'stations'
if key_to_lookup in customer_data[customerKey][productKey]:
    customer_data[customerKey][productKey]['stations'][list_order] =  wsi_code
else:
    customer_data[customerKey][productKey]['stations'] = {list_order:wsi_code}

print(f"customer_data = {customer_data}")


customerKey = 'GBE'
productKey = 'GBESOLAROBS'
list_order = 2
wsi_code = 1982


key_to_lookup = 'stations'
print("customer_data[customerKey][productKey] = ", customer_data[customerKey][productKey])
if key_to_lookup in customer_data[customerKey][productKey]:
    customer_data[customerKey][productKey]['stations'][list_order] =  wsi_code

else:
    customer_data[customerKey][productKey]['stations'] = {list_order:wsi_code}


print(f"customer_data = {customer_data}")
