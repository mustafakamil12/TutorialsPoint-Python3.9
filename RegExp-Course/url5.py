#www.facebook.com/CSxFunda
#URL Question 5 Solution


import re
#read the text file having urls
fp=open('url.txt','r')
text=fp.read()

#write the regex expression
pattern=r'(?:https://)?www\.[a-z0-9]+(?:\.in|\.com)'

#create the regex object
regex=re.compile(pattern)

#extract the urls
urls=regex.findall(text)

for u in urls:
    print(u)
