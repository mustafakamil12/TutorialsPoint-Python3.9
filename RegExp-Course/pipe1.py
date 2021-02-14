import re
text='''
A weight is 42kg
B weight is 100kg
C weight is 30kg
D weight is 111kg
'''

pattern=r'\d\d\d?'
regex=re.compile(pattern)

myOut=regex.findall(text)
print(myOut)