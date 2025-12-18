import math


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)
        self.x3 = int(x3)
        self.y3 = int(y3)

    def area(self):
        len1 = ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5
        len2 = ((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2) ** 0.5
        len3 = ((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2) ** 0.5
        p = (len1 + len2 + len3) / 2
        s = (p * (p - len1) * (p - len2) * (p - len3)) ** 0.5
        print('Площадь треугольника:', round(s, 2))
        return round(s, 2)

    def perimeter(self):
        len1 = ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5
        len2 = ((self.x3 - self.x1) ** 2 + (self.y3 - self.y1) ** 2) ** 0.5
        len3 = ((self.x2 - self.x3) ** 2 + (self.y2 - self.y3) ** 2) ** 0.5
        print('Периметр треугольника:', round(len1 + len2 + len3, 2))
        return round(len1 + len2 + len3, 2)

    def vertices(self):
        print('Количество углов треугольника: 3')


class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.x2 = int(x2)
        self.y2 = int(y2)

    def area(self):
        lenx = abs(self.x2 - self.x1)
        leny = abs(self.y2 - self.y1)
        print('Площадь прямоугольника:', round(lenx * leny, 2))
        return round(lenx * leny, 2)

    def perimeter(self):
        lenx = abs(self.x2 - self.x1)
        leny = abs(self.y2 - self.y1)
        print('Периметр прямоугольника:', round((lenx + leny) * 2, 2))
        return round((lenx + leny) * 2, 2)

    def vertices(self):
        print('Количество углов прямоугольника: 4')


class Circle:
    def __init__(self, x1, y1, r):
        self.x1 = int(x1)
        self.y1 = int(y1)
        self.r = int(r)

    def area(self):
        print('Площадь круга:', round(math.pi * self.r ** 2, 2))
        return round(math.pi * self.r ** 2, 2)

    def perimeter(self):
        print('Периметр круга:', round(2 * math.pi * self.r, 2))
        return round(2 * math.pi * self.r, 2)

    def vertices(self):
        print('У круга нет углов')


a = int(input('Введите количество фигур: \n'))
mas, area, per, vert = [], 0, 0, 0
for i in range(a):
    m = input()
    mas.append(m)
haract = input()
if haract not in 'area, perimeter, vertices':
    print('Введите area, perimeter или vertices')

for elem in mas:
    c = (elem + ' ' + haract).split()
    if c[0] == 'triangle':
        if len(c) == 8:
            k = Triangle(c[1], c[2], c[3], c[4], c[5], c[6])
            if c[-1] == 'area':
                area += k.area()
            if c[-1] == 'perimeter':
                per += k.perimeter()
            if c[-1] == 'vertices':
                vert += 3

    if c[0] == 'rectangle':
        if len(c) == 6:
            k = Rectangle(c[1], c[2], c[3], c[4])
            if c[-1] == 'area':
                area += k.area()
            if c[-1] == 'perimeter':
                per += k.perimeter()
            if c[-1] == 'vertices':
                vert += 4

    if c[0] == 'circle':
        if len(c) == 5:
            k = Circle(c[1], c[2], c[3])
            if c[-1] == 'area':
                area += k.area()
            if c[-1] == 'perimeter':
                per += k.perimeter()
            if c[-1] == 'vertices':
                vert += 0

if haract == 'area':
    print('Общая площадь:', area)
if haract == 'perimeter':
    print('Общий периметр:', per)
if haract == 'vertices':
    print('Общее количество углов:', vert)
