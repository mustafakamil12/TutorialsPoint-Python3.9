import re

randstr = "12345"

print("Match: ", len(re.findall("\d",randstr)))
print("Match: ", len(re.findall("\d{5}",randstr)))