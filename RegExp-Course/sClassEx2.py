#www.facebook.com/CSxFunda
#program to illustrate shorthand character class

import re

text='names are Kalyan K, Meghana K'
pattern=r'[A-Z][a-z]+\s[A-Z]'

regex=re.compile(pattern)
names=regex.findall(text)

print(names)
