import re
text='names are Kalyan, Meghana'

pattern=r'[A-Z][a-z]+'
regex=re.compile(pattern)

names=regex.findall(text)
print(names)