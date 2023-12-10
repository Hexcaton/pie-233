list_a = [1, 2, -3, 4, 5, -6, 7, 8, -9, 10]
result = [x ** 2 for x in list_a if x % 2 == 0]
print(result)