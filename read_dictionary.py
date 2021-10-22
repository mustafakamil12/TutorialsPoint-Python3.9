products_per_period = {
'ET_06AM':
['BOFAHRLYFCST6AM', 'CONOCOOBS', 'DTEDAILYOBS', 'DTEHOURLYOBS', 'VITOLMAXMINOBS'],

'ET_09AM':
['CMWHOURLYOBS', 'DIAMONDHRLYFCST', 'DIAMONDHRLYFCST2'],

'ET_01PM':
['BOFADLYFCSTN', 'DTEHOURLYFCST', 'NGRID_LI', 'SARACENOBS', 'USEFCST'],

'ET_07PM':
['DYNEGYFCST', 'ESCOHOURLY', 'STATARBFCST4']
}

print(f"products_per_period = {products_per_period}")

for cycle_product_elem in products_per_period:
    for product_elem in products_per_period[cycle_product_elem]:
        print(f"product = {product_elem}")
