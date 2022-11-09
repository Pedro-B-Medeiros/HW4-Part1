import utility


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x, 0.00001) and utility.epsilon_equal(self.y, other.y, 0.00001) and utility.epsilon_equal(self.z, other.z, 0.00001)


class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        return utility.epsilon_equal(self.x, other.x, 0.00001) and utility.epsilon_equal(self.y, other.y, 0.00001) and utility.epsilon_equal(self.z, other.z, 0.00001)


class Ray:
    def __init__(self, pt, dir):
        self.pt = pt
        self.dir = dir

    def __eq__(self, other):
        return (self.pt == other.pt) and utility.epsilon_equal(self.dir, other.dir, 0.00001)


class Sphere:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def __eq__(self, other):
        return (self.center == other.center) and utility.epsilon_equal(self.radius, other.radius, 0.00001)
