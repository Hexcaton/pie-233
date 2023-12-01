list_int = [147, 241, 39, 5, 778, 18, 0, 10]

count_even = (lambda x: len(list(filter(lambda num: num % 2 == 0, x))))(list_int)
count_odd = (lambda x: len(list(filter(lambda num: num % 2 == 1, x))))(list_int)

print("Количество четных чисел:", count_even)
print("Количество нечетных чисел:", count_odd)