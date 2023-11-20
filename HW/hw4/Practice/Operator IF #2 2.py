print("Введите год через Enter:")
int_1 = int(input())
if 1900 <= int_1 <= 3000:
    if (int_1 % 400 == 0) or (int_1 % 4 == 0) and not (int_1 % 100 == 0):
        print('Високосный')
    else:
        print('Обычный')

else:
    print('Введите год от 1900 до 3000.')