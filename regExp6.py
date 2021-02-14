import re

food = "hat rat mat pat"

regex = re.compile("[r]at")

food = regex.sub("food",food)

print(food)
