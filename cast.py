import collisions
import data
import vector_math as vm

def cast_ray(ray, sphere_list):
    list_intersections = collisions.find_intersection_points(sphere_list, ray)
    if len(list_intersections) == 0:
        return False
    else:
        return True


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list):
    x_step = (max_x - min_x)/width
    y_step = (max_y - min_y)/height
    print('P3')
    print(width, height)
    print('255')
    for y in range(height):
        for x in range(width):
            ray = data.Ray(eye_point, data.Vector(min_x + x_step*x, max_y - y_step*y, 14))
            if cast_ray(ray, sphere_list) is True:
                print('0 0 0')
            else:
                print('255 255 255')
