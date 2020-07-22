from random import choice

my_list = [choice(range(1000)) for x in range(100)]

max_value = 0
for item in my_list:
    if item > max_value:
        max_value = item

print(max_value)
print(max(my_list))
