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

#Another white spaces u can work with
#\b: backspace
#\f: formfeed
#\r: carriage return
#\t: tab
#\v: vertical tab
