"""This is object oriented programming"""


class BareMinimumClass:
        pass


class Complex:
        def __init__(self, realpart, imagpart):
           """Constructor for Complex Numbers"""
            self.r = realpart
            self.i = imagpart

        def add(self, other_complex):
            """Adds complex numbers"""
            self.r += other_complex.r
            self.i += other_complex.i 
        def __repr__(self):
            return "({}, {}i)".format(self.r, self.i)






num1 = Complex(3,-5)
num2 = Complex(2,6)
num1.add(num2)
print(num1.r, num1.i)