#www.facebook.com/CSxFunda
#program to illustrate positive character class

import re
text='words are cat, mat, bat, rat'
pattern=r'[cmbr]at'
regex=re.compile(pattern)
words=regex.findall(text)
print(words)
