import re

text='Kalyan is a good boy and he is 24 years old and he is going to marry Meghana'
pattern=r'\d{2}'

regex=re.compile(pattern)
newList=regex.split(text)
print(newList)

