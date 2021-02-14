#www.facebook.com/CSxFunda
#program to illustrate the non capturing groups

import re
text='My  personal number is 043-225431  and my office number is 043-225143'

pattern1=r'\d\d\d-\d\d\d\d\d'
regex=re.compile(pattern1)
numbers=regex.findall(text)
print(numbers)                        #list of strings

pattern2=r'(\d\d\d)-(\d\d\d\d\d)'
regex=re.compile(pattern2)
numbers=regex.findall(text)
print(numbers)                         #list of tuples

pattern3=r'(?:\d\d\d)-(?:\d\d\d\d\d)'
regex=re.compile(pattern3)
numbers=regex.findall(text)
print(numbers)                         #list of strings


