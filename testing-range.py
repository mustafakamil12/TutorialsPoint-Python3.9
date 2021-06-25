class listIncrease:
    def __init__(self):
        self.myArr = []

    def append(self,val):
        arrSize = len(self.myArr)
        print(f"arrSize = {arrSize}")
        self.myArr.insert(arrSize,val)
        print(self.myArr)

    def arrSize(self):
        print(f"the array size is = {len(self.myArr)}")

titusArr = listIncrease()
titusArr.append(1)
titusArr.append(2)
titusArr.append(3)
titusArr.append(4)

titusArr.arrSize()
