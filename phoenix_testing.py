prod_phoenix_not_in_periods_list_raw = ['CAITHNESSFCST,CAITHNESSOBS', 'ENRGYVALFRCST,ENRGYVALOBS', 'FPLEXCEL', 'DAILYTRADERFC,HOURLYTRADERFC', 'NATGASCSSRAW', 'NATGRIDLIFCST', 'NATGRIDLIOBS5AM', 'NATGRIDLIOBS12PM', 'PHOENIXDAILYFCST,PHOENIXHOURLYFCST', 'PHOENIXDAILYOBS', 'PHOENIXDAILYFCSTEARLY,PHOENIXHOURLYFCSTEARLY', 'PHOENIXDAILYOBSEUR,PHOENIXDAILYFCSTEUR,PHOENIXHOURLYFCSTEUR', 'PHOENIXHOURLYOBSEUR', 'PHOENIXDAILYFCSTEURUPDATE,PHOENIXHOURLYFCSTEURUPDATE', 'PHOENIXHOURLYOBS,PHOENIXHOURLYOBSAUS,PHOENIXHOURLYOBSASIA', 'PHOENIXDAILYOBSAUS,PHOENIXDAILYFCSTAUS,PHOENIXHOURLYFCSTAUS', 'PHOENIXDAILYOBSASIA,PHOENIXDAILYFCSTASIA,PHOENIXHOURLYFCSTASIA', 'PHOENIXDAILYFCSTOFFHOUR,PHOENIXHOURLYFCSTOFFHOUR', 'PHOENIXDAILYFCSTUPDATE,PHOENIXHOURLYFCSTUPDATE']

prod_phoenix_not_in_periods_list = []
for phoenixElem in prod_phoenix_not_in_periods_list_raw:
    temp_array = phoenixElem.split(",")
    for phoenixSubElem in temp_array:
        prod_phoenix_not_in_periods_list.append(phoenixSubElem)

print(f"prod_phoenix_not_in_periods_list = {prod_phoenix_not_in_periods_list}")
