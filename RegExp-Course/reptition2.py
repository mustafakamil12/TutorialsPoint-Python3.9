#www.facebook.com/CSxFunda
#program to illustrate repitition {m,n}

import re

text='numbers are 10,100,1000,10000'
pattern=r'\d{2,5}'

regex=re.compile(pattern)
numbers=regex.findall(text)

print(numbers)
