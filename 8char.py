import re

myText = 'mustafa'

test = re.findall((r'.'),myText)
test2 = re.findall(r'^.',myText)
test1 = re.findall(r'\d+',myText)


if(len(test)<= 8 and len(test1) == 0 and len(test2) == 0):
    print("name meet the rules")
else:
    print("name doesn't meet the rules")

