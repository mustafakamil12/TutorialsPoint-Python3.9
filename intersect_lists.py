def fetch_product_list_names_from_cycle_list(cycle_arr):
    products_per_period = {}
    for cycle_elem in cycle_arr:
        print(f"cycle_elem = {cycle_elem}")
        products = subprocess.run('crontab -l | grep cycle',stdin=True, input=None, stdout=PIPE, stderr=PIPE, shell=True)
        subprocess_rc = products.returncode
        productsop = products.stdout
        productsop = productsop.decode("utf-8")
        productsop = productsop.strip()
        for productsop_elem in productsop:
            print(f"productsop_elem = {productsop_elem}")


cycle_payload = ['Afternoon', 'Evening', 'ET_11PM', 'ET_00AM', 'ET_01AM', 'ET_02AM', 'ET_03AM', 'ET_04AM', 'ET_05AM', 'ET_06AM', 'ET_07AM', 'ET_08AM', 'ET_09AM', 'ET_10AM', 'ET_11AM', 'ET_12PM', 'ET_01PM', 'ET_02PM', 'ET_03PM', 'ET_04PM', 'ET_05PM', 'ET_06PM', 'ET_07PM', 'ET_08PM']
psqlcontArr = ['ET_12PM', 'Mid Morning', 'ET_06PM', 'Afternoon', 'ET_06AM', 'Trader 6AM', 'Priority 6AM', 'Early Morning', 'ET_07AM', 'NRGSTREAMDLYOBS', 'ET_8PM', 'Intermediate', 'Energy Trader', 'ET_08PM', 'ET_01PM', 'ET_11PM', 'ET_11AM', 'ET_07PM', 'ET_04AM', 'ET_05PM', 'ET_08AM', 'ET_00AM', 'Evening', 'ET_09AM', 'ET_05AM', 'ET_03PM', 'Trader Long-Range', 'ET_03AM', 'Early', 'ET_02PM', 'ET_5PM', 'Trader Priority', 'ET_10AM', 'ET_04PM', '(34 rows)']

print(f"lenght of cycle_payload = {len(cycle_payload)}")
print(f"length of psqlcontArr = {len(psqlcontArr)}")

cycle_payload_as_set = set(cycle_payload)
intersection = cycle_payload_as_set.intersection(psqlcontArr)
intersection_as_list = list(intersection)
print(f"length of intersection_as_list = {len(intersection_as_list)}")
print(intersection_as_list)
