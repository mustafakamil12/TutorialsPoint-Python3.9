import re
text='values are 1,10,100,1000'

pattern=r'\d+'
regex=re.compile(pattern)

numbers=regex.findall(text)
print(numbers)