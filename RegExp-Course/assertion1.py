#www.facebook.com/CSxFunda
#program to illustrate  positive look ahead assertion

import re

text='Kalyan_cs,Meghana_cs,John,Jack'
pattern='(?i)[a-z]+(?=_cs)'
#pattern=r'[A-Za-z]+'
regex=re.compile(pattern)

names=regex.findall(text)

print(names)
