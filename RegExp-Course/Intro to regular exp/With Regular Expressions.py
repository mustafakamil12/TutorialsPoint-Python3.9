#www.facebook.com/CSxFunda
#Extract weights using regular expressions
#import the module
import re

#read the text file having weights
fp=open('weights.txt','r')
text=fp.read()

#extract the weights using regular expressions
#simple and short code
pattern=r'\d\d'
regex=re.compile(pattern)
weights=regex.findall(text)

#display the weights
print(weights)

