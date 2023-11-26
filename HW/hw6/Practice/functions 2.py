def sum_range(a, b):
    if a > b:
        return 0
    else:
        return a + sum_range(a + 1, b)

input_str = input("Введите 2 числа через пробел и нажмите Enter: ")
a, b = map(int, input_str.split())

result = sum_range(a, b)
print(f"Сумма всех чисел от {a} до {b}: {result}")