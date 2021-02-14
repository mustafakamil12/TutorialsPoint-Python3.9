#www.facebook.com/CSxFunda
#program to illustrate  named  backreferences 

import re

text='Office Land Line number is 043405117 '
pattern=r'(?P<area>\d{3})(?P<number>\d{6})'

regex=re.compile(pattern)

text=regex.sub(r'\g<area>-\g<number>',text)

print(text)



