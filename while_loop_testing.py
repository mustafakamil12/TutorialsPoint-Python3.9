import time

flag = 0
my_counter = 0
while my_counter < 50:
    print(my_counter)
    my_counter += 1

    if my_counter == 50:
        time.sleep(1)
        my_counter = 0
        flag += 1
    if flag == 3:
        break
