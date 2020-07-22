my_list = [x for x in range(100001)]

sum_values = 0
for item in my_list:
    sum_values += item

print(sum_values)
print(sum(my_list))