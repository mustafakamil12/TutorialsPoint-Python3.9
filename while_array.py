prod_count = 0
prod_name = []
row_ref = [('BOFADLYFCSTN', 'frmt_bofa_daily_fcst', 'bofa_stn', '', ''), ('SARACENOBS', 'obs_saracen', 'saracen_stn', None, ''), ('NGRID_LI', 'frmt_ngrid_li', 'single_FRG', None, ''), ('USEFCST', 'frmt_usenergy', 'usenergy_stn', None, ''), ('DTEHOURLYFCST', 'frmt_dtehourly', 'dte_new_stn', None, '')]
while row_ref:
    print("row_ref.pop(0): ", row_ref[0])
    print("prod_count: ", prod_count)
    row_ref_tup_to_list = [elem for elem in row_ref[0]]
    print("row_ref_tup: ", row_ref_tup_to_list)
    prod_name.insert(prod_count,row_ref_tup_to_list[0])
    print("prod_name: ", prod_name)
    prod_count += 1
    row_ref.pop(0)
