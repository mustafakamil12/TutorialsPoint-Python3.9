import time

epoch_time = 1625768714

def gmttime(epoch_time):
    print("gmttime inpurt arg: ", epoch_time)
    struct_tm_py_way = time.gmtime(epoch_time)
    print("struct_tm_py_way: ", struct_tm_py_way)
    struct_tm = []

    for elem in struct_tm_py_way:
        struct_tm.append(elem)

    print("struct_tm = ", struct_tm)
    struct_tm[8] = -1

    print("struct_tm before return = ", struct_tm)
    return struct_tm

print(gmttime(epoch_time))
