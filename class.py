class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self,age):
        self.age = age

d = dog("Time",34)
print(d.get_name(),d.get_age())
d.set_age(12)
print(d.get_age())
    
