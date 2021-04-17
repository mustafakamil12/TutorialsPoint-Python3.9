import re

address = '#TZ=whatever#'

default_match = re.match('#TZZ=(\w*)#',address)
print(default_match)
print(default_match.group(0))
print(default_match.group(1))

"""
if (default_match:=re.match('#TZ=(\w*)#',address)):
    print(default_match)
else:
    print("Fail")
"""
