import math

class Figure:
    def dimention(self):
        raise NotImplementedError

    def perimetr(self):
        return None

    def square(self):
        return None

    def squareSurface(self):
        return None

    def squareBase(self):
        return None

    def height(self):
        return None

    def volume(self):
        return self.square() if self.dimention() == 2 else None


# 2D Figures
class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def dimention(self): return 2

    def perimetr(self): return self.a + self.b + self.c

    def square(self):
        s = self.perimetr() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))


class Rectangle(Figure):
    def __init__(self, a, b):
        self.a, self.b = a, b

    def dimention(self): return 2

    def perimetr(self): return 2 * (self.a + self.b)

    def square(self): return self.a * self.b


class Trapeze(Figure):
    def __init__(self, a, b, c, d):
        self.a, self.b, self.c, self.d = a, b, c, d

    def dimention(self): return 2

    def perimetr(self): return self.a + self.b + self.c + self.d

    def square(self):
        h = math.sqrt(self.c**2 - ((self.b - self.a)**2 + self.c**2 - self.d**2) / (2 * (self.b - self.a))**2)
        return 0.5 * (self.a + self.b) * h


class Parallelogram(Figure):
    def __init__(self, a, b, h):
        self.a, self.b, self.h = a, b, h

    def dimention(self): return 2

    def perimetr(self): return 2 * (self.a + self.b)

    def square(self): return self.a * self.h


class Circle(Figure):
    def __init__(self, r):
        self.r = r

    def dimention(self): return 2

    def perimetr(self): return 2 * math.pi * self.r

    def square(self): return math.pi * self.r ** 2


# 3D Figures
class Ball(Figure):
    def __init__(self, r):
        self.r = r

    def dimention(self): return 3

    def squareSurface(self): return 4 * math.pi * self.r**2

    def volume(self): return (4/3) * math.pi * self.r**3


class TriangularPyramid(Triangle):
    def __init__(self, a, h):
        super().__init__(a, a, a)
        self.h = h

    def dimention(self): return 3

    def squareBase(self): return super().square()

    def height(self): return self.h

    def volume(self): return (1/3) * self.squareBase() * self.h


class QuadrangularPyramid(Rectangle):
    def __init__(self, a, b, h):
        super().__init__(a, b)
        self.h = h

    def dimention(self): return 3

    def squareBase(self): return super().square()

    def height(self): return self.h

    def volume(self): return (1/3) * self.squareBase() * self.h


class RectangularParallelepiped(Rectangle):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def dimention(self): return 3

    def squareSurface(self): return 2 * (self.a*self.b + self.a*self.c + self.b*self.c)

    def volume(self): return self.a * self.b * self.c


class Cone(Circle):
    def __init__(self, r, h):
        super().__init__(r)
        self.h = h

    def dimention(self): return 3

    def squareBase(self): return super().square()

    def height(self): return self.h

    def squareSurface(self):
        l = math.sqrt(self.r**2 + self.h**2)
        return math.pi * self.r * (self.r + l)

    def volume(self): return (1/3) * super().square() * self.h


class TriangularPrism(Triangle):
    def __init__(self, a, b, c, h):
        super().__init__(a, b, c)
        self.h = h

    def dimention(self): return 3

    def squareBase(self): return super().square()

    def height(self): return self.h

    def volume(self): return super().square() * self.h
