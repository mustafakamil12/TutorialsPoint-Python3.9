import inspect

class dog:
    def __init__(self,name):
        self.name = name

        if isinstance(self.name,dog):
            print("This is object to the same class...", name)
            dog.get_another_name(self.name)

        else:
            print("Dog name = ", self.name)

    def get_another_name(self):
        print(self.name)

myDog = dog("bobi")
hisDog = dog(myDog)
