#www.facebook.com/CSxFunda
#program to illustrate the pipe meta character
import re
text='words are cat,mat,bat'
pattern=r'cat|mat|bat'
regex=re.compile(pattern)
words=regex.findall(text)
print(words)

print('---------------------')
# Or u can use the below:

newPattern=r'(?:c|m|b)at'
newRegex=re.compile(newPattern)
newWords=newRegex.findall(text)
print(newWords)
