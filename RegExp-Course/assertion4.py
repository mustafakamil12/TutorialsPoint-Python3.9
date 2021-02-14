#www.facebook.com/CSxFunda
#program to illustrate  negative look behind assertion
 
import re

text='Values are CS1001,CS1002,CS1003,1989'
pattern='(?<!CS)\d{4}'

regex=re.compile(pattern)
values=regex.findall(text)

print(values)




