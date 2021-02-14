import re

randstr = "123456"
print("Matches: ", len(re.findall("\d{5}",randstr)))