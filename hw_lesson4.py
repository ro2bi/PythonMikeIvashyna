import math


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'


class Line:
    def __init__(self, point1: Point, point2: Point):
        self.length = math.sqrt(math.pow(point2.x - point1.x, 2) + math.pow(point2.y - point1.y, 2))


class Circle:
    def __init__(self, center: Point, R: float) -> None:
        self.center = center
        self.R = R

    def getS(self):
        return math.pi * self.R ** 2

    def getL(self):
        return 2 * math.pi * self.R


# Пример использования:
point1 = Point(0, 0)
point2 = Point(0, 5)

Rline = Line(point1, point2)

circle = Circle(point1, Rline.length)

print(f"Центр кола: {circle.center}")
print(f"Радіус кола: {circle.R}")
print(f"Площа кола: {circle.getS()}")
print(f"Довжина кола: {circle.getL()}")
