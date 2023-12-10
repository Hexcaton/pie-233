list_a = [1, 2, 3, 4, 5, 6, 7]
list_b = {x: x ** 3 for x in list_a if x % 2 != 0}
print(list_b)