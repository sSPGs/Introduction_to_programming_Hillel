


'''                                            Занятие 8.
Функции (аргументы, значения), assert и простейшие тесты, модули os, typing, sys.'''
##########################################################################################################################

def get_distance(point_1, point_2) -> float:
    distance = (point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1] ** 2) ** 0.5
    return distance

'''Формула Герона'''
def get_area_gerone(point_1, point_2, point_3) -> float:
    a = get_distance(point_1, point_2)
    b = get_distance(point_1, point_3)
    c = get_distance(point_2, point_3)
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    return area
"----------------------------------------"
point_A = (8, 1)
point_B = (5, 2)
point_C = (9, 1)
"----------------------------------------"
# dist_A_B = get_distance(point_A, point_B)
# print(dist_A_B)



# if area_a_b_c == 0.5:
#     print("OK")
# else:
#     print("BAD")
#
# if abs(area_a_b_c - 0.5) < 0.001:
#     print("OK")
# else:
#     print("NO OK")
area_a_b_c = get_area_gerone(point_A, point_B, point_C)

print(area_a_b_c)

if __name__ == "__main__":
    assert abs(get_area_gerone((0, 0), (0, 4), (3, 0)) - 6.0) < 0.01
    print(area_a_b_c)



##########################################################################################################################







