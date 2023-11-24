print('Введите два натуральных числа через Enter, чтобы вывести фрагмент таблицы умножения для всех чисел между ними: ')
a_int = int(input())
b_int = int(input())

print('Введите два натуральных числа через Enter, на которые нужно произвести умножение.:')
c_int = int(input())
d_int = int(input())

if a_int < 11 and b_int < 11 and c_int < 11 and d_int < 11:
    print('\t', end='')

    for i1 in range(c_int, d_int + 1):
        print(i1, end='\t')
    print()

    for i2 in range(a_int, b_int + 1):
        print(i2, end='\t')
        for i1 in range(c_int, d_int + 1):
            print(i2 * i1, end='\t')
        print()

else:
    print("Некорректный ввод.")