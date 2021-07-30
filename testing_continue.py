higherlimit = 3
looplimit = 1

for j in range(0,higherlimit):
    for i in range(0,looplimit):
        print(f"i = {i}")
        if i == 1:
            print(f"we found i = {i} we will run continue")
            continue
        print("we are at the end of for loop")

    
    print("reach out to the bottom of higherlimit")
