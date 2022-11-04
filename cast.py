import collisions
import data
import vector_math as vm

def cast_ray(ray, sphere_list, amb_color):
    list_intersections = collisions.find_intersection_points(sphere_list, ray)
    if len(list_intersections) == 0:
        return data.Color(1, 1, 1)
    else:
        nearest_inter = list_intersections[0]
        distance = vm.length_vector(vm.vector_from_to(ray.pt, nearest_inter[1]))
        for intersec in list_intersections:
            new_distance = vm.length_vector(vm.vector_from_to(ray.pt, intersec[1]))
            if new_distance <= distance:
                nearest_inter = intersec
        modified_color = data.Color(nearest_inter[0].color.r, nearest_inter[0].color.g, nearest_inter[0].color.b)
        modified_color.r = modified_color.r * amb_color.r * nearest_inter[0].finish.ambient
        modified_color.g = modified_color.g * amb_color.g * nearest_inter[0].finish.ambient
        modified_color.b = modified_color.b * amb_color.b * nearest_inter[0].finish.ambient
        return modified_color


def cast_all_rays(min_x, max_x, min_y, max_y, width, height, eye_point, sphere_list, amb_color):
    x_step = (max_x - min_x)/width
    y_step = (max_y - min_y)/height
    print('P3')
    print(width, height)
    print('255')
    for y in range(height):
        for x in range(width):
            ray = data.Ray(eye_point, data.Vector(min_x + x_step*x, max_y - y_step*y, 14))
            #print(x, y, cast_ray(ray, sphere_list))
            color_shown = cast_ray(ray, sphere_list, amb_color)
            color_255r = min(int(color_shown.r * 255), 255)
            color_255g = min(int(color_shown.g * 255), 255)
            color_255b = min(int(color_shown.b * 255), 255)
            print(color_255r, color_255g, color_255b)