import re

PRODUCTID = "DTEHOURLYFCST"
CLIENTID  = 'gfs' + PRODUCTID[0:3]
print(f"CLIENTID = {CLIENTID}")

ADDRESS = "ftpsrv.wsicorp.com /u/saracen saracen horse3empire obs09232021.csv"
ADDRESS = re.sub(r"\s","",ADDRESS)
print(f"ADDRESS = {ADDRESS}")

myStr = "Hello World!"

print(myStr)
print(myStr[0])
print(myStr[1])
print(myStr[2:4])
print(myStr[6:])
print(myStr *2)
print(myStr + "Test")

mylist = ['abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print(mylist)
print(mylist[0])
print(mylist[2:4])
print(mylist[2:])
print(mylist + tinylist)
print(mylist * 2)
print(len(mylist))

mytuple = ('abcd', 786 , 2.23, 'john', 70.2)
tinytuple = (123, 'john')

print(mytuple)
print(mytuple[0])
print(mytuple[2:4])
print(mytuple[2:])
print(mytuple + tinytuple)
print(mytuple * 2)

mydict = {}
mydict['one'] = "This is number one"
mydict[2] = "This is number two"

tinydict = {'name':'John','code':'6748','dept':'IT'}

print(mydict)
print(tinydict)
print(mydict['one'])
print(mydict[2])
print(tinydict.keys())
print(tinydict.values())

del tinydict['name']
print(tinydict.keys())
print(tinydict.values())

tinydict.clear()
print(tinydict.keys())
print(tinydict.values())

del tinydict
print(tinydict.keys())
print(tinydict.values())
