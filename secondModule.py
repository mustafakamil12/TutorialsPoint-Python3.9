myVar = None

def loader():
    global myVar
    print("calling loader in the secondModule")
    myVar = "This is myVar within loader()"
    resVar = myVar
    return resVar


if __name__ == '__main__':
    print(f"myVar = {loader()}")
