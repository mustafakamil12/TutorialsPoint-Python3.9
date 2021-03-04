class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old!")
    def speak(self):
        print("I don't know what to say!!!")


#Cat will inherent from Pet
class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color

    def speak(self):
        print("Meao")
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}!")


class Dog(Pet):
    def speak(self):
        print("Bark")

p = Pet("Tim",19)
p.show()
p.speak()
c = Cat("Bill",25,"white")
c.show()
c.speak()
d = Dog("Jill",34)
d.show()
d.speak()