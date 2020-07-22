my_list = [x for x in range(101)]

product = 1
for item in my_list:
    if item != 0:
        product *= item

print(product)