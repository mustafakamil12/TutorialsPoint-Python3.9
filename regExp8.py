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

final_address = "#TZ=godric#"
#final_address = "godric.phoenix@gmail.com"
final_address = re.sub(' (\S*[\$#]\S*) ',f"\'\"\'\"\'\"{final_address}\"\'\"\'\"\'" ,final_address)

print(f"final_address = {final_address}")
#Another white spaces u can work with
#\b: backspace
#\f: formfeed
#\r: carriage return
#\t: tab
#\v: vertical tab
