import inspect

class dog:
    def __init__(self,secs):
        self.secs = secs

        if isinstance(self.secs,dog):
            print("This is object to the same class...", secs)
            self.other = 1260
            print("other obj value = ", self.other)
            print("original obj value = ", self.secs.secs)

        else:
            print("Dog secs = ", self.secs)


    def get_another_secs(self):
        print(self.secs)

    def seconds_after(self):
        print(f"{self.secs} - {self.other}")
        res = self.secs.secs - self.other
        print("Res = ", res)

myDog = dog(1250)
hisDog = dog(myDog)

dog.seconds_after(hisDog)
