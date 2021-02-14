#www.facebook.com/CSxFunda
#program to illustrate the dot   meta character

import re
text='kalyan1234\n145'
pattern=r'.'   

regex=re.compile(pattern)
characters=regex.findall(text)

print(characters)
