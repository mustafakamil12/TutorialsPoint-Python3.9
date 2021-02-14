import re 
#text='CS1005 Kalyan roll number is CS1004 and Mustafa roll number is CS1006'
text='Kalyan roll number is CS1004 and Mustafa roll number is CS1006'

pattern=r'CS\d{4}'
regex=re.compile(pattern)

myOut=regex.match(text)
print(myOut)