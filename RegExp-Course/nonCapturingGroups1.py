import re

text='My roll number is CS1004'
pattern=r'(?:CS)(?:\d{4})'

regex=re.compile(pattern)
myOut=regex.findall(text)

print(myOut)