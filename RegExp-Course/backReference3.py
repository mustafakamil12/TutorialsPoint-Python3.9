#www.facebook.com/CSxFunda
#program to illustrate  named  backreferences 

import re

text='The numbers are 1414,1618,2020,4038'
pattern=r'(?P<first>\d{2})(?P=first)'

regex=re.compile(pattern)

numbers=regex.finditer(text)
#print(numbers)
for n in numbers:
    print(n.group())


    




