myStr = 'python'
for i in myStr:
    if i == 't':
        break
    print("Letter: ",i)
print('-----')
myStr = 'python'
for i in myStr:
    if i == 't':
        pass
        print("we are in the pass block")
    print("Letter: ",i)
print('-----')
myStr = 'python'
for i in myStr:
    if i == 't':
        continue
    print("Letter: ",i)