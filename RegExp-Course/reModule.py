#www.facebook.com/CSxFunda
#program to illustrate the basics of re module

#import the re module
import re


text='Roll Number is 7004'
#write the regular expression
pattern=r'\d\d\d\d'

#creat the regex object using compile function
regex=re.compile(pattern)

#call the findall function using regex object
number=regex.findall(text)

#display the extracted numbers
print(number)
