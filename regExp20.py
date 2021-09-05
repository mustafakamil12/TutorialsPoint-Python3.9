import re

param = 'bydaytcprob_m3'
default_match = re.search('m3',param)
print(f"default_match = {default_match[0]}")
