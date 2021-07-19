import datetime

row_ref = [('2021-07-19 19:33:00+00')]
row_ref_tup_to_list = []
while row_ref:
   for elem in row_ref[0]:
      if isinstance(elem, datetime.date):
         selem = elem.strftime("%Y-%m-%d %H:%M:%S.%f")
         print("selem = ", selem)
         row_ref_tup_to_list.append(selem)
      else:
         row_ref_tup_to_list.append(elem)

   print("row_ref_tup_to_list: ", row_ref_tup_to_list)
   row_ref.pop(0)
   #row_ref_tup_to_list = []

#print("row_ref: ", row_ref)
if row_ref_tup_to_list:
   print(row_ref_tup_to_list[0])
else:
   print("Nothing to retrieve")
