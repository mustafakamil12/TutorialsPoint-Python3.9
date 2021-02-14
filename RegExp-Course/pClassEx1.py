#www.facebook.com/CSxFunda
#program to illustrate positive character class


import re
text='words are weak,week'
pattern=r'we[ae]k'
regex=re.compile(pattern)
words=regex.findall(text)
print(words)
