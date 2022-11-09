import cast
import unittest
import data

class TestCases(unittest.TestCase):
    def test_cast_all_rays(self):
        eye_point = data.Point(0.0, 0.0, -14.0)
        min_x = -10
        max_x = 10
        min_y = -7.5
        max_y = 7.5
        width = 512
        height = 384
        sphere_list = [data.Sphere(data.Point(1.0, 1.0, 0.0), 2), data.Sphere(data.Point(0.5, 1.5, -3), 0.5)]
        cast.cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list)

if __name__ == "__main__":
    unittest.main()