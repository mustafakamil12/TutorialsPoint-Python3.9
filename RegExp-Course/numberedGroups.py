#www.facebook.com/CSxFunda
#program to illustrate the numbered groups

import re 
text='Kalyan roll number is CS1004'
     
pattern=r'(CS)(\d\d\d\d)'
regex=re.compile(pattern)

mo=regex.search(text)
print(mo)           #prints Object
print(mo.group())   #prints CS1004
print(mo.group(0))  #prints CS1004
print(mo.group(1))  #prints CS
print(mo.group(2))  #prints 1004
print(mo.groups())  #prints (CS,1004)



