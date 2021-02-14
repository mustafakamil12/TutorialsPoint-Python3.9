import re
text='the values are 8,109,1400,44,1001,59,2064'

pattern=r'\b([0-9]|[1-9][0-9]|[1-9][0-9][0-9])\b'
regex=re.compile(pattern)
numbers=regex.findall(text)

print('numbers in the giving range: ')
for i in numbers:
    print(i)