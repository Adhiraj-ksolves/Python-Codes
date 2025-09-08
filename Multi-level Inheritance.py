class GrandParent:
    Name = "Ravikant"
    surname = "Joshi"

    def show(self):
        print("I am GrandParent")


class Parent(GrandParent):
    Name = "Suryakant"

    def show(self):
        print(f"I am son of {self.Name} {self.surname}")


class Child(Parent):
    def show(self):
        print(f"I am Child of {self.Name}")



p = Parent()
c = Child()

p.show()
c.show()
