#www.facebook.com/CSxFunda
#program to illustrate the astersik meta character

import re

text='words are abbbc  abbc abc  ac'
pattern=r'ab*c'

regex=re.compile(pattern)

print(regex.findall(text))
