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
    def __init__(self, center, radius, color, finish):
        self.center = center
        self.radius = radius
        self.color = color
        self.finish = finish

    def __eq__(self, other):
        return (self.center == other.center) and utility.epsilon_equal(self.radius, other.radius, 0.00001) and (self.color == other.color) and utility.epsilon_equal(self.finish, other.finish, 0.00001)


class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def __eq__(self, other):
        return utility.epsilon_equal(self.r, other.r, 0.00001) and utility.epsilon_equal(self.g, other.g, 0.00001) and utility.epsilon_equal(self.b, other.b, 0.00001)


class Finish:
    def __init__(self, ambient):
        self.ambient = ambient  # percentage of ambient light reflected by the finish

    def __eq__(self, other):
        return utility.epsilon_equal(self.ambient, other.ambient, 0.00001)
