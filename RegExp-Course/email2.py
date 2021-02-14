# match all yahoo adrresses
import re

fp=open('email1.txt','r')
text=fp.read()

pattern=r'\b[A-Za-z0-9.-_]+@yahoo(?:.[a-z]+)+\b'

regex=re.compile(pattern)

emails=regex.findall(text)
for e in emails:
    print(e)