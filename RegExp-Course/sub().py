#www.facebook.com/CSxFunda
#program to illustrate the working of sub

import re

text='Kalyan roll number is 1001. Meghana roll number is 1002'
pattern=r'\d\d\d\d'

regex=re.compile(pattern)
mtext=regex.sub(r'****',text)

print(mtext)
