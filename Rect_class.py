class Rectangle:
    def set_params(self, a, par_b):
        self.a = a
        self.b = par_b

    def calc_surface(self):
        return self.a*self.b

    def __repr__(self):
        return "Rectangle[" + str(self.a) + " by " + str(self.b) + "] at " + str(hex(id(self)))

r = Rectangle()
r.set_params(4, 5)
area = r.calc_surface()
print(r)
print('area of r is: ' + str(area))
