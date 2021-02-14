import re

str = "sat,hat,mat,pat"
allstr = re.findall("[shmp]at",str)

for i in allstr:
    print(i)