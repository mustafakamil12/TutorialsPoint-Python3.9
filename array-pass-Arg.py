def myArrFun(funArr = [], *args):
    if len(funArr) != 0:
        firstElem = funArr.pop(0)
        print(firstElem)
        print(funArr)


myList = 1
myArrFun(myList)
