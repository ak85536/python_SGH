class Shape:
    def __init__(self, a=10, b=6):
        self.set_params(a, b)

    def set_params(self, a, par_b):
        self._a = a
        self.b = par_b

    def get_a(self):
        return self._a

    def __repr__(self):
        return self.__class__.__name__ + "[" + str(self._a) + " by " + str(self.b) + "] at " + str(hex(id(self)))


class Rectangle(Shape):
    def calc_surface(self):
        return self._a*self.b

    def swap_sides(self):
        a = self._a
        b = self.b
        self._a = b
        self.b = a

    def perimeter(self):
        return (self._a+self.b) * 2

    def __repr__(self):
        return self.__class__.__name__ + " with sides: " + str(self._a) + " by " + str(self.b) + " is at " + str(hex(id(self)))

rec = Rectangle(2,3)
print(rec)
print(rec.perimeter())


import math

class Circle(Shape):
    def __init__(self, a):
        # call constructor of superclass (parent)
        super().__init__(a, 0)
        #self._a = a

    def calc_surface(self):
        return math.pi * self._a**2

    def perimeter(self):
        return self._a * math.pi * 2

    def __repr__(self):
        return self.__class__.__name__ + " with radius: " + str(self._a) + " is at " + str(hex(id(self)))


cir = Circle(3)
print(cir)
print(cir.perimeter())


########################
class Triangle(Shape):
    def __init__(self, a, b, v):
       self.set_params(a, b, v)

    def set_params(self, a, b, v):
        self._a = a
        self.b = b
        self.v = v

    def calc_surface(self):
        s = (self._a + self.b + self.v) / 2
        return (s*(s-self._a)*(s-self.b)*(s-self.v)) ** 0.5

    def perimeter(self):
        return self._a + self.b + self.v

    def __repr__(self):
        return self.__class__.__name__ + " with sides: " + str(self._a) + ", " + str(self.b) + ", " + str(self.v) + " is at " + str(hex(id(self)))

    # def __repr__(self):
    #     return self.__class__.__name__ + "Surface area is  " + str((self.s*(self.s-self._a)*(self.s-self.b)*(self.s-self.d)) ** 0.5) + \
    #            "] at " + str(hex(id(self)))


t = Triangle(2,3,4)
print(t)
print(t.calc_surface())
print(t.perimeter())


class EquilateralTriangle(Triangle):
    def __init__(self, a):
        self.set_params(a)

    def set_params(self, a):
        self._a = a

    def calc_surface(self):
        s = (self._a + self._a + self._a) / 2
        return (s*(s-self._a)*(s-self._a)*(s-self._a)) ** 0.5

    def perimeter(self):
        return self._a * 3

    def __repr__(self):
        return self.__class__.__name__ + " with sides " + str(self._a) + ", " + str(self._a) + ", " + str(self._a) + " is at " + str(hex(id(self)))


et = EquilateralTriangle(5)
print(et)
print(et.calc_surface())
print(et.perimeter())


class Square(Rectangle):
    def __init__(self, a):
        self._a = a
        self.b = a


sq = Square(4)
print(sq)
print(sq.calc_surface())

