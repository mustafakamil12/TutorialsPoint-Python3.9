#www.facebook.com/CSxFunda
#program to illustrate reptition {m,}

import re

text='numbers are 101,1203,14005'

pattern=r'\d{3,}'
regex=re.compile(pattern)

numbers=regex.findall(text)

print(numbers)
