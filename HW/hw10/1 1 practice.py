list_a = [1, 2, -3, 4, 5, -6, 7, 8, -9, 10]
list_b = [x ** 3 if x < 0 else x ** 2 for x in list_a if x % 2 == 0]
print(list_b)