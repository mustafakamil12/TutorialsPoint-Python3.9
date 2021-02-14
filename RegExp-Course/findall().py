#www.facebook.com/CSxFunda
#program to illustrate the working of findall 

import re
text='Kalyan roll number is 1001. Meghana roll number is 1002'
pattern=r'\d\d\d\d'

regex=re.compile(pattern)
rollNumbers=regex.findall(text)

if rollNumbers:
    print(rollNumbers)
else:
    print('Roll Numbers are not found')
