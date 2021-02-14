numbers = [3,5,7,9,11,13,15,17,19,21,22,23]

for i in numbers:
    if i%2 == 0:
        print("There's even number in the list = ",i)
        break
else:
    print("The list doesn't have even number")