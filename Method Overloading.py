class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(5))
print(calc.add(5, 10.22))
print(calc.add(5, 1.0, 1.5))
