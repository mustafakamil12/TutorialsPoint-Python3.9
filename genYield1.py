def infinit_seq():
    num = 0
    while True:
        yield num
        num += 1   
"""
for i in infinit_seq():
    print(i,end=' ')
"""
mygen = infinit_seq()
next(mygen)
       
