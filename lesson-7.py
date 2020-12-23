from time import sleep


class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):                                         # вывод информации для пользователя в строковом виде
        return f"Координата Х:{self.x}, координата Y:{self.y}"

    def __repr__(self):                                         # вывод информации для диагностики в строковом виде
        return f"Координата Х:{self.x}, координата Y:{self.y}"

    def __add__(self, other):    # point1 - self, point2 - other   вычисление сложения
        x = self.x + other.x
        y = self.y + other.y
        return Point2D(x, y)

    def __eq__(self, other):            # сравнение по равенству
        return self.x == other.x and self.y == other.y

class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):                                         # вывод информации для пользователя в строковом виде
        return f"{super().__str__()}, координата Z:{self.z}"

    def __repr__(self):                                         # вывод информации для диагностики в строковом виде
        return f"{super().__str__()}, координата Z:{self.z}"

    def __add__(self, other: 'Point3D') -> 'Point3D':    # point1 - self, point2 - other   вычисление сложения
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        return Point3D(x, y, z)

    def __eq__(self, other):            # сравнение по равенству
        return super().__eq__(other) and self.z == other.z

    def __iter__(self):
        return MyShinnyIterator(self)

    @property
    def summ_coord(self):
        return self.x + self.y + self.z


class MyShinnyIterator:                 # Custom Iterator
    def __init__(self, point_3d):
        self.start = min(point_3d.x, point_3d.y,point_3d.z)
        self.finish = max(point_3d.x, point_3d.y, point_3d.z)
        self.buf = self.start

    def __next__(self):
        if self.start == self.finish:
            raise StopIteration("Ошибка предельного значния итерации!")
        self.start += 1
        return self.start

    def to_start(self):
        self.start = self.buf

    def __iter__(self):
        return self



point1 = Point2D(x=1, y=2)
point2 = Point2D(x=3, y=4)
point3 = point1 + point2 + point2 + point1
print(point3)
point1 = Point2D(x=1, y=2)
point2 = Point2D(x=1, y=2)
print(point1 == point2)

point2 = point2 + point1
point3 += point2            # вызывается метод __iadd__ если его нет, то __add__

print(point2)
print(point3)

point3d1 = Point3D(1,2,3)
print(point3d1)
point3d2 = Point3D(4,5,6)
print(point3d1 == point3d2)

#----ИТЕРАТОРЫ----------
l = [1, 2, 3]
o = iter(l)
c = 1
for el in l:
    print(el)

point3d3 = Point3D(1, 2, 30)
for coord in point3d3:
    sleep(0.5)
    print(coord)
c = iter(point3d3)
for i in range(5):
    print(next(c))
c.to_start()                # управление интератором, сброс в начало
print("--------------")
for el in c:
    print(el)
#----------Декоратор Property-----------
print("--------------")
print(point3d3.summ_coord)




