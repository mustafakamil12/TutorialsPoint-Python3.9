#www.facebook.com/CSxFunda
#meta character example program

import re
text='values are +10,20,+30,40'
pattern=r'\+?\d{2}'
regex=re.compile(pattern)
numbers=regex.findall(text)
print(numbers)
