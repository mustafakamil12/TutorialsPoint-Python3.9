# find the even number in the giving string
import re
text='the valuse are 2,8,18,109,140,44,63,59,206'

pattern=r'\b[02468]\b|\d+[02468]\b'
regex=re.compile(pattern)
numbers=regex.findall(text)
print('Even numbers are: ')
for i in numbers:
    print(i)