# as long as your app will growing up, u need more functions and more organize of what u built

class MyMath:
    @staticmethod
    def add5(x):
        return x + 5
    @staticmethod
    def add10(x):
        return x + 10
    @staticmethod
    def pr():
        print("Run")

print(MyMath.add5(5))
print(MyMath.add10(10))
MyMath.pr()
