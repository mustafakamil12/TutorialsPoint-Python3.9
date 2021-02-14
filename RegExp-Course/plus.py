#www.facebook.com/CSxFunda
#program to illustrate the plus  meta character

import re
text='abbbc abbc  abc  ac'

pattern=r'ab+c'
regex=re.compile(pattern)
words=regex.findall(text)
print(words)

pattern1=r'ab*c'
regex1=re.compile(pattern1)
words1=regex1.findall(text)
print(words1)
