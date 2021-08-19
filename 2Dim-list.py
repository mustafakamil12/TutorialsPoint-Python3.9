#newArr[s][i]
baseFile = [1,2]
baseArr = [11,22,33,44,55,66,77,88,99,100]

dualArr = []


for s,val in enumerate (baseFile):
    dualArr.insert(s,baseArr)

"""
for idx,val in enumerate(baseArr):
    print(idx)
"""

print(f"dualArr = {dualArr}")
