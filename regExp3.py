import re

str = "we need to inform him with the latest information"

for i in re.finditer("inform",str):
    loctup = i.span()
    print(loctup)