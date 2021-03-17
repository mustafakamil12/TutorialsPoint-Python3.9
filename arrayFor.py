for letter in 'python':
    print(letter)
print()

fruits = ['apple','banana','orange','mango']
for fruit in fruits:
    print(fruit)

print("-----")

for myInd in range(len(fruits)):
    print(fruits[myInd])

myNum = [1,2,3,4,5,6,7,8,9,1,2,2,3,4,5,6,6,6,6]
print(max(myNum))
print(min(myNum))

print(myNum)
myNum.append(10)
print(myNum)
print(myNum.count(6))
myNum1 = [11,12,13]
myNum.extend(myNum1)
print(myNum)
print("index: ",myNum.index(6))
myNum.insert(3,99)
print(myNum)
myNum.pop()
print(myNum)
myNum.pop(3)
print(myNum)
myNum.remove(6)
print(myNum)
myNum.reverse()
print(myNum)
myNum.sort()
print(myNum)

myNum2 = (99,100,101)
myNum3 = (99,100,6)
print(myNum2)
print(myNum2[0])
#myNum2[0] = 102
