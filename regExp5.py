import re

str = "sat,hat,mat,pat"
allstr = re.findall("[h-m]at",str)

for i in allstr:
    print(i)

print('-----------')
newallstr = re.findall("[^h-m]at",str)

for j in newallstr:
    print(j)