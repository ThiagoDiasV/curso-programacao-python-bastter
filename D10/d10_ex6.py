my_list = [(5, 4, 1), (3, 2, 10), (10, 5, 2), (4, 6, 4), (8, 3, 3), (2, 7, 8)]

ordered_list = sorted(my_list, key=lambda x: x[2])

print(ordered_list)