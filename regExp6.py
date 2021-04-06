import re

food = "hat rat mat pat"

regex = re.compile("[r]at")

#food = regex.sub("food",food)
food = re.sub("[r]at","food",food)

print(food)
