print("Введите 2 целых числа через Enter:")
a_int = int(input())
b_int = int(input())

print("Все числа в указанном диапазоне:")
for i in range(a_int, b_int + 1):
    print(i)

print("\nНечетные числа в указанном диапазоне:")
for i in range(a_int, b_int + 1):
    if i % 2 != 0:
        print(i)

print("\nЧетные числа в указанном диапазоне:")
for i in range(a_int, b_int + 1):
    if i % 2 == 0:
        print(i)
print("\nЧисла в указанном диапазоне в порядке убывания:")
for i in range(b_int, a_int - 1, -1):
    print(i,)