import math


class Point:
    count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Point.count += 1

    def norm(self):
        n = math.sqrt(self.x**2 + self.y**2)
        return n

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)
