#www.facebook.com/CSxFunda
#program to illustrate  numbered backreferences 

import re

text='Office Land Line number is 043405117 '
pattern=r'(\d{3})(\d{5})'

regex=re.compile(pattern)

text=regex.sub(r'\1-\2',text)

print(text)