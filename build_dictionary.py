import json

cycle_arr = ['ET_12PM','ET_11AM']
newcyclecontArr1 = ['DTEHOURLYFCST','CRSTVIEWHRLYFCST', 'DOMENERGYFCST14']
newcyclecontArr2 = ['Mustafa','Mena', 'Yousif']

products_per_period = {}

for cycle_elem in cycle_arr:
    products_per_period[cycle_elem] = []
    for newcyclecontArrelem in newcyclecontArr1:
        products_per_period[cycle_elem].append(newcyclecontArrelem)

print(f"products_per_period = {products_per_period}")
print(products_per_period['ET_12PM'][1])
