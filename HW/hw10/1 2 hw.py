list_a = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
list_b = {x for x in list_a if x % 2 == 0}
print(list_b)