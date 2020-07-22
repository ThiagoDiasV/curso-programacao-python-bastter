from random import choice

my_list = [choice(range(1000)) for x in range(100)]

min_value = max(my_list)
for item in my_list:
    if item < min_value:
        min_value = item

print(min_value)
print(min(my_list))