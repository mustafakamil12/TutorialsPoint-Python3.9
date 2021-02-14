#www.facebook.com/CSxFunda
#program to illustrate shorthand character class

import re
text='email ids are ab-c9@yahoo.com, pqr.9@gmail.com'
pattern=r'\S+@\S+'
regex=re.compile(pattern)
email=regex.findall(text)
print(email)
