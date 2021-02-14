# find numbers between 100 and 150
import re
text='the valuse are 2,8,18,109,140,44,63,59,206,4003'

pattern=r'\b1[0-4][0-9]|150\b'
regex=re.compile(pattern)
numbers=regex.findall(text)
print('Numbers in the range 100 - 150 : ')
for i in numbers:
    print(i)