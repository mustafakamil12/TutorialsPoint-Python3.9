no = int(input("Enter any number please: "))
noArr = [1,2,3,4,5,6,7,8,9]
for i in noArr:
    if i == no:
        print("found the number: " , no)
        break
else:
    print("Not found the number...")