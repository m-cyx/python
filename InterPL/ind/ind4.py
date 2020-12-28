from hashlib import sha256
from datetime import datetime
from time import sleep


class Triangle(object):
    def __init__(self, x1y1, x2y2, x3y3):
        sleep(0.1)
        self.mark = sha256(str(datetime.now()).encode()).hexdigest()
        self.x1y1 = x1y1
        self.x2y2 = x2y2
        self.x3y3 = x3y3
        self.x1 = x1y1[0]
        self.x2 = x2y2[0]
        self.x3 = x3y3[0]
        self.y1 = x1y1[1]
        self.y2 = x2y2[1]
        self.y3 = x3y3[1]
        self._area = abs( 1 / 2 * ( (self.x1 - self.x3) * (self.y2 - self.y3) - (self.y1 - self.y3) * (self.x2 - self.x3) ) )

    def move(self, x=0, y=0):
        try:
            self.x1y1[0] += x
            self.x2y2[0] += x
            self.x3y3[0] += x
            self.x1y1[1] += y
            self.x2y2[1] += y
            self.x3y3[1] += y
        except TypeError:
            print("Ввод цифр!")

    def printer(self):
        print(f"x1y1 - {self.x1y1}")
        print(f"x2y2 - {self.x2y2}")
        print(f"x3y3 - {self.x3y3}")

    def __str__(self):
        return f"Площадь треугольника {self.mark} = {self._area}"


class Quad(object):
    def __init__(self, x1y1, x2y2, x3y3, x4y4):
        sleep(0.1)
        self.mark = sha256(str(datetime.now()).encode()).hexdigest()
        self.x1y1 = x1y1
        self.x2y2 = x2y2
        self.x3y3 = x3y3
        self.x4y4 = x4y4
        self.x1 = x1y1[0]
        self.x2 = x2y2[0]
        self.x3 = x3y3[0]
        self.x4 = x4y4[0]
        self.y1 = x1y1[1]
        self.y2 = x2y2[1]
        self.y3 = x3y3[1]
        self.y4 = x4y4[1]
        self._area = abs( 1 / 2 * 
            (
                self.x1 * self.y2
                + self.x2 * self.y3
                + self.x3 * self.y4
                + self.x4 * self.y1
                - self.x2 * self.y1
                - self.x3 * self.y2
                - self.x4 * self.y3
                - self.x1 * self.y4
            )
        )

    def move(self, x=0, y=0):
        try:
            self.x1y1[0] += x
            self.x2y2[0] += x
            self.x3y3[0] += x
            self.x4y4[0] += x
            self.x1y1[1] += y
            self.x2y2[1] += y
            self.x3y3[1] += y
            self.x4y4[1] += y
        except TypeError:
            print("Ввод цифр!")

    def printer(self):
        print(f"x1y1 - {self.x1y1}")
        print(f"x2y2 - {self.x2y2}")
        print(f"x3y3 - {self.x3y3}")
        print(f"x4y4 - {self.x4y4}")

    def __str__(self):
        return f"Площадь квадрата {self.mark} = {self._area}"


class Comparator(object):
    def compare(self, Quad: Quad, triangle: Triangle):
        if Quad._area > triangle._area:
            print( f"Площадь квадрата({Quad._area}) больше площади треугольника({triangle._area}) на {Quad._area - triangle._area}")
        elif Quad._area < triangle._area:
            print( f"Площадь квадрата({Quad._area}) меньше площади треугольника({triangle._area}) на {triangle._area - Quad._area}")
        else:
            print( f"Площадь квадрата({Quad._area}) равна площали треугольника({triangle._area})")


triangle = Triangle([3, 6], [6, 4], [0, 0])
triangle.printer()
triangle.move(2, 3)
print("\nПосле использования move:")
triangle.printer()
print(triangle)
print("\n")
Quad = Quad([1, 1], [1, 3], [6, 3], [6, 1])
Quad.printer()
Quad.move(4, 5)
print("\nПосле использования move:")
Quad.printer()
print(Quad)

comparator = Comparator()
comparator.compare(Quad=Quad, triangle=triangle)
