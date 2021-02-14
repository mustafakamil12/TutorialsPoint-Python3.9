# print all match email in the email1.txt
import re

fp=open('email1.txt','r')
text=fp.read()

pattern=r'\b[A-Za-z0-9.-_]+@[a-z]+(?:.[a-z]+)+\b'

regex=re.compile(pattern)

emails=regex.findall(text)
for e in emails:
    print(e)