# find the even number of digits in the giving string
import re
text='the valuse are 2,8,18,109,140,44,63,59,206,4003'

pattern=r'\b(?:\d{2})+\b'
regex=re.compile(pattern)
numbers=regex.findall(text)
print('Even numbers digits are: ')
for i in numbers:
    print(i)