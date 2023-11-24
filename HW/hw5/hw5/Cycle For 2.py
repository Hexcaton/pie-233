n = int(input('Введите натуральное число ≤ 9\n'))
numbers = []

if 1 <= n <= 9:
    for i in range (1, n + 1):
        numbers.append(str(i))
        print(''.join(numbers))
else:
    print("Некорректный ввод.")