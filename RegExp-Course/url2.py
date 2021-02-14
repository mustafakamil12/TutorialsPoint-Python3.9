#www.facebook.com/CSxFunda
#URL Program1

import re
#read the text file
fp=open('url.txt','r')
text=fp.read()

#write the regex expression
pattern=r'https://www\.[a-z0-9]+\.[a-z]+'


#create the regex object
regex=re.compile(pattern)

#extract the urls
urls=regex.findall(text)
for u in urls:
    print(u)
