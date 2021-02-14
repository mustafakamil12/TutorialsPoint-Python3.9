#www.facebook.com/CSxFunda
#program to illustrate the working of finditer
import re
text='Kalyan roll number is 1001. Meghana roll number is 1002'
pattern=r'\d\d\d\d'

regex=re.compile(pattern)
rollNumbers=regex.finditer(text)

if rollNumbers:
    for r in rollNumbers:
        print(r.group())
        print(r.start())
        print(r.end())
        print(r.span())
        print(r.re.pattern)
        print(r.string)
else:
    print('No roll numbers found')
