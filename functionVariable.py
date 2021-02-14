from modules import support

def printinfo(var1, *vartuple):
    print("This is printinfo function")
    print(var1)

    for var in vartuple:
        print(var)
    return

def printinfoDef(var2=30):
    print("This is printinfoDef function")
    print(var2)
    return

printinfo(10)
printinfo(10,20,30)
print()
printinfoDef(2.5)
printinfoDef()

sum = lambda arg1 , arg2 : arg1 + arg2
print(sum(3,5))

support.print_func("test")

print("global variable: " , __name__)

