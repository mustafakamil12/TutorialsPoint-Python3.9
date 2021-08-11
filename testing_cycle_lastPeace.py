import GFS_history
import GFS_date

send_cycle = 1
send_count = 0
error_count = 0
warning_count = 0

if send_cycle:
    official_tag = 'official'
    official_history_column = 'official_table'
    prod_send_update_column = 'product_send_time'

    cycle_time_Arr = []
    cycle_time_Arr.append(official_history_column)
    cycle_time_Arr.append(official_tag)
    print("cycle_time_Arr: ", cycle_time_Arr)

    cycle_time = GFS_history.get_cycle_time(cycle_time_Arr)

    time_string = GFS_date.format_date(GFS_date.current_date_time())
    print("time_string: ", time_string)

    print("------------------------")
    print("cycle_time: ", cycle_time)
    print("prod_send_update_column: ", prod_send_update_column)
    print("time_string: ", time_string)


    update_history_row_Arr = []
    update_history_row_Arr.append(cycle_time)
    update_history_row_Arr.append(prod_send_update_column)
    update_history_row_Arr.append(time_string)

    print("update_history_row_Arr: ", update_history_row_Arr)

    GFS_history.update_history_row(update_history_row_Arr)

    print(f"GFS Product send complete {send_count} products, {error_count} errors, {warning_count} warnings")
