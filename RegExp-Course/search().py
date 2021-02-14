import re 
text='Kalyan roll number is CS1004 and Mustafa roll number is CS1006'

pattern=r'\d{4}'
regex=re.compile(pattern)

myOut=regex.search(text)
print(myOut)

print(myOut.group())   
print(myOut.group(0))  
#print(myOut.group(1))  
#print(myOut.group(2))  
print(myOut.groups())  