import sys

print("The number of arguments:",len(sys.argv),"arguments.")
print("Arguments list",sys.argv)
wholeArgsArray = sys.argv
wholeArgsArray.pop(0)

print(' '.join([str(singleArg) for singleArg in (wholeArgsArray)]))

while arg:=(sys.argv).pop(0):
    print("what in while loop: ", arg)
    sys.exit()
