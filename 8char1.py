import re

myName=input('Please Enter your name: ')

pattern=r'^[A-Za-z]{2,8}$'

if re.search(pattern,myName):
    print('Valid Name')
else:
    print('Not valid name')