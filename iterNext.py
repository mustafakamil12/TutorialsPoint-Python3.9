myList = [1,2,3,4,5]
myiter = iter(myList)
print(next(myiter))

print('-----')

for i in myiter:
    print(i,end=" ")

print()