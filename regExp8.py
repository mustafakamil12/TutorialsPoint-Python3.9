import re

randstr = '''
Keep the blue flag
flying high
chelsea
'''

print(randstr)

regex = re.compile("\n")
randstr = regex.sub(" ",randstr)
print(randstr)

testStr = "Mustafa"

print(f"this is {testStr}...")

newStr = re.sub('chelsea',f"\'\"\'\"\'\"{testStr}\"\'\"\'\"\'",randstr)
print(newStr)

#Another white spaces u can work with
#\b: backspace
#\f: formfeed
#\r: carriage return
#\t: tab
#\v: vertical tab
