#www.facebook.com/CSxFunda
#program to illustrate negative character class

import re

text='Roll numbers are b1001 , c1002, d1003, f1004 ,h1005 '
pattern=r'[^aeiou]\d{4}'   
regex=re.compile(pattern)

roll=regex.findall(text)
print(roll)
  
