#www.facebook.com/CSxFunda
#program to illustrate positive character class

import re
text='rolls are ab101,bc102,cd103,ef104'
pattern=r'[a-z]{2}\d{3}'
regex=re.compile(pattern)
rolls=regex.findall(text)
print(rolls)
