list_a = [1, 2, -3, 4, 5, -6, 7, 8, -9, 10]
result = [x if x > 0 and x % 5 else 0 for x in list_a]
print(result)