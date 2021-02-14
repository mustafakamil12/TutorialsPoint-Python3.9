# find numbers from 10 to 99
import re
text='the values are 10,100,140,44,62,59,200'

pattern=r'\b[1-9][0-9]\b'
regex=re.compile(pattern)
numbers=regex.findall(text)
print('Integer Numbers are: ')
for i in numbers:
    print(i)
