import re
text='words are practice,practise'
pattern1=r'practice|practise'
regex1=re.compile(pattern1)
words1=regex1.findall(text)
print(words1)

print('---------------------')

pattern2=r'practi(?:c|s)e'
regex2=re.compile(pattern2)
words2=regex2.findall(text)
print(words2)