n = 4
filename = 'code.txt'
"""
myfile = open(filename,'r')
print(myfile)
for line in myfile:
    print(line)
"""

with open(filename) as my_file:
    head = [next(my_file) for x in range(n)]

for line in head:
    print(line)
