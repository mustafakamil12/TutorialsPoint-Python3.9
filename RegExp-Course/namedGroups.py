#www.facebook.com/CSxFunda
#program to illustrate the working of named groups
import re

text='Kalyan roll number is CS1004'
pattern=r'(?P<branch>CS)(?P<roll>\d\d\d\d)'

regex=re.compile(pattern)

mo=regex.search(text)
print(mo.group())            #prints CS1004
print(mo.group(0))           #prints CS1004
print(mo.group('branch'))    #prints CS
print(mo.group('roll'))      #prints 1004
print(mo.groups())           #prints (CS,1004)



