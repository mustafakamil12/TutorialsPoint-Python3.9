# find the odd number in the giving string
import re
text='the valuse are 2,8,18,109,140,44,63,59,206'

pattern=r'\b[13579]\b|\d+[13579]\b'
regex=re.compile(pattern)
numbers=regex.findall(text)
print('Odd numbers are: ')
for i in numbers:
    print(i)