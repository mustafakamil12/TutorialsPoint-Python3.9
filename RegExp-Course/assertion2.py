#www.facebook.com/CSxFunda
#program to illustrate  negative look ahead assertion

import re

text='values are 12,13,14a,15b'
pattern=r'\d{2}(?![a-z])'

regex=re.compile(pattern)

values=regex.findall(text)
print(values)


