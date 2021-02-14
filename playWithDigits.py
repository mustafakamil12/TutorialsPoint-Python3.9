import re
text='The phone number is 043405117'

pattern=r'(\d{3})(\d{3})'
regex=re.compile(pattern)
MyOut=regex.findall(text)

print(MyOut)