#www.facebook.com/CSxFunda
#program to illustrate  numbered backreferences 

import re

text='The numbers are 1116,1414,4035,2020'
pattern=r'(\d{2})\1'

regex=re.compile(pattern)

mo=regex.finditer(text)
for i in mo:
    print(i.group())



