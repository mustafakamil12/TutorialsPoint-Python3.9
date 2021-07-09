import sys

print("The number of arguments:",len(sys.argv),"arguments.")
print("Arguments list",sys.argv)
wholeArgsArray = sys.argv
print("wholeArgsArray = ", wholeArgsArray)
wholeArgsArray.pop(0)
print("clean wholeArgsArray = ", wholeArgsArray)

#print(' '.join([str(singleArg) for singleArg in (wholeArgsArray)]))

while wholeArgsArray:
    arg = wholeArgsArray.pop(0)
    print("what in while loop: ", arg)
    
