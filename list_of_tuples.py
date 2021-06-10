import datetime
import psycopg2

row_ref = [('AmDaweek', datetime.datetime(1980, 1, 1, 0, 0, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), datetime.datetime(2038, 1, 19, 3, 14, 7, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), 'MST   ', False, -25200), ('AfAcccra', datetime.datetime(1901, 12, 13, 20, 45, 52, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), datetime.datetime(1936, 8, 31, 23, 59, 59, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), 'GMT   ', False, 0), ('AfAcccra', datetime.datetime(1936, 9, 1, 0, 0, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), datetime.datetime(1936, 12, 30, 23, 39, 59, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), 'GHST  ', True, 1200), ('AfAcccra', datetime.datetime(1936, 12, 30, 23, 40, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), datetime.datetime(1937, 8, 31, 23, 59, 59, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), 'GMT   ', False, 0), ('AfAcccra', datetime.datetime(1937, 9, 1, 0, 0, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), datetime.datetime(1937, 12, 30, 23, 39, 59, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), 'GHST  ', True, 1200), ('AfAcccra', datetime.datetime(1937, 12, 30, 23, 40, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), datetime.datetime(1938, 8, 31, 23, 59, 59, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), 'GMT   ', False, 0), ('AfAcccra', datetime.datetime(1938, 9, 1, 0, 0, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), datetime.datetime(1938, 12, 30, 23, 39, 59, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), 'GHST  ', True, 1200), ('AfAcccra', datetime.datetime(1938, 12, 30, 23, 40, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), datetime.datetime(1939, 8, 31, 23, 59, 59, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), 'GMT   ', False, 0), ('AfAcccra', datetime.datetime(1939, 9, 1, 0, 0, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), datetime.datetime(1939, 12, 30, 23, 39, 59, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), 'GHST  ', True, 1200), ('AfAcccra', datetime.datetime(1939, 12, 30, 23, 40, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), datetime.datetime(1940, 8, 31, 23, 59, 59, tzinfo=psycopg2.tz.FixedOffsetTimezone(offset=0, name=None)), 'GMT   ', False, 0)]


#print("myArr: ", row_ref)
row_ref_tup_to_list = []
while row_ref:
  #print("row_ref.pop(0): ", row_ref[0])
  #print("prod_count: ", prod_count)

  for elem in row_ref[0]:
      if isinstance(elem, datetime.date):
          selem = elem.strftime("%Y-%m-%d %H:%M:%S.%f")
          row_ref_tup_to_list.append(selem)
      else:
          row_ref_tup_to_list.append(elem)

  #row_ref_tup_to_list = [elem for elem in row_ref[0]]
  #prod_name.append(prod_count)
  #prod_name.append(row_ref_tup_to_list[0])


  print("row_ref_tup_to_list: ", row_ref_tup_to_list)
  #build_product_from_info(row_ref_tup_to_list)
  #print("row_ref_tup after pass it to build_product_from_info: ", row_ref_tup_to_list)

  #print("prod_name: ", prod_name)
  #prod_count += 1
  row_ref.pop(0)
  row_ref_tup_to_list = []
