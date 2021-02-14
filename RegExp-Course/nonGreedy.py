#www.facebook.com/CSxFunda
#program to illustrate  non-greedy matching

import re

text='The pattern is abcabcabcabc'
pattern=r'a[a-z]+?c'

regex=re.compile(pattern)
mo=regex.search(text)

print(mo.group()) 