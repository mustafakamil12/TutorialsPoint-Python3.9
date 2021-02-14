import re
text='values are +10.01,20.02,30.03'

pattern=r'\+?\d{2}\.\d{2}'
regex=re.compile(pattern)

numbers=regex.findall(text)
print(numbers)