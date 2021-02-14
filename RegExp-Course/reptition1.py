#www.facebook.com/CSxFunda
#program to illustrate the repitition {m}

import re

text='numbers are 100,200,300,400'
pattern=r'\d{3}'

regex=re.compile(pattern)
numbers=regex.findall(text)

print(numbers)
