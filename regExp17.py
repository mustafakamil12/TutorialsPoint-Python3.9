import re,time
from datetime import datetime

build_count = 0


def gmttime(epoch_time):
      global build_count
      print("gmttime inpurt arg: ", epoch_time)
      struct_tm_py_way = time.gmtime(epoch_time)
      print("struct_tm_py_way: ", struct_tm_py_way)

      struct_tm_py_way_arr = []

      for elem in struct_tm_py_way:
         struct_tm_py_way_arr.append(elem)

      print(struct_tm_py_way_arr)
      struct_tm = []
      y = 5
      for x in range(len(struct_tm_py_way_arr)-1):
         print("index= ", x)
         if x <= 5:
            print("y= ", y)
            struct_tm.append(struct_tm_py_way_arr[y])
            print(struct_tm[x])
            y -= 1
         elif x > 5 or x < 8:
            struct_tm.append(struct_tm_py_way_arr[x])


      struct_tm.append(-1)
      print(struct_tm)
      build_count += 1
      return(struct_tm)


fmt = '%Y-%m-%d %H:%M:%S%z'

default_match = re.findall('\%z',fmt)
print("default_match = ", default_match)

if default_match:
    print("default_match", default_match)
else:
    print("Nothing had been matched!!!")

tmnow = int(time.time())

print(gmttime(tmnow))

date_time = datetime.fromtimestamp(tmnow)

d = date_time.strftime(fmt)
print("d:", d)
