#www.facebook.com/CSxFunda
#program to illustrate the question mark meta character

import re
text='My lucky number is 06 and her lucky number is 121'
pattern=r'\d\d\d?'

regex=re.compile(pattern)

numbers=regex.findall(text)
print(numbers)

  
