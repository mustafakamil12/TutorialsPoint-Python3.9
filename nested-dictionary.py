customer_data = {}

customer = 'NOEL'
product_name = 'NOELTESTPROD'
station_list = 'NOELTEST'
frequency = 'daily'
post_proc = ''

print(f"length of customer_data = {len(customer_data)}")

if len(customer_data) != 0:
	if customer in customer_data:
		print(f"1. {customer} exist in {customer_data}")
		if product_name in customer_data[customer]:
			print(f"2. product_name: {product_name} exist")
			customer_data[customer][product_name]['station_list'] = station_list
		else:
			print(f"3. product_name: {product_name} not exist")
			customer_data[customer][product_name] = {'station_list' : station_list}

	else:
		print(f"4. {customer} not exist in customer_data = {customer_data}")
		customer_data[customer] = {product_name : {'station_list' : station_list}}


else:
	print(f"5. {customer} not exist in customer_data = {customer_data}")
	customer_data = {customer : {product_name : {'station_list' : station_list}}}

print(customer_data)
customer_data[customer][product_name]['post_proc'] = post_proc
print(customer_data)


print(f"length of customer_data = {len(customer_data)}")

customer = 'NOEL'
product_name = 'NOELTESTPROD2'
station_list = 'NOELTEST2'
frequency = 'daily'
post_proc = ''


if len(customer_data) != 0:
	if customer in customer_data:
		print(f"1. {customer} exist in {customer_data}")
		if product_name in customer_data[customer]:
			print(f"2. product_name: {product_name} exist")
			customer_data[customer][product_name]['station_list'] = station_list
		else:
			print(f"3. product_name: {product_name} not exist")
			customer_data[customer][product_name] = {'station_list' : station_list}

	else:
		print(f"4. {customer} not exist in customer_data = {customer_data}")
		customer_data[customer] = {product_name : {'station_list' : station_list}}


else:
	print(f"5. {customer} not exist in customer_data = {customer_data}")
	customer_data = {customer : {product_name : {'station_list' : station_list}}}

print(customer_data)
customer_data[customer][product_name]['post_proc'] = post_proc
print(customer_data)


print(f"length of customer_data = {len(customer_data)}")


customer = 'GBE'
product_name = 'GBESOLAROBS'
station_list = 'gbe_solar_stn'
frequency = 'daily'
post_proc = ''

if len(customer_data) != 0:
	if customer in customer_data:
		print(f"1. {customer} exist in {customer_data}")
		if product_name in customer_data[customer]:
			print(f"2. product_name: {product_name} exist")
			customer_data[customer][product_name]['station_list'] = station_list
		else:
			print(f"3. product_name: {product_name} not exist")
			customer_data[customer][product_name] = {'station_list' : station_list}

	else:
		print(f"4. {customer} not exist in customer_data = {customer_data}")
		customer_data[customer] = {product_name : {'station_list' : station_list}}


else:
	print(f"5. {customer} not exist in customer_data = {customer_data}")
	customer_data = {customer : {product_name : {'station_list' : station_list}}}

print(customer_data)
customer_data[customer][product_name]['post_proc'] = post_proc
print(customer_data)
