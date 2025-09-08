class Animal:
    def sound(self):
        print("Animals make sound")

class Dog(Animal):
    def sound(self):   # overriding Animal ka method
        print("Dog barks")


a = Animal()
d = Dog()

a.sound()
d.sound()
