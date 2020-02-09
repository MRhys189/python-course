class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
print(isinstance(m, object)) #if m is an instance of object class
o = object()  # for creating an empty object
print(issubclass(Mammal, object)) #if mammal class is derived from object class

