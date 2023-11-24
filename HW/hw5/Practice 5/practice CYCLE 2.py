print('Введите целые числа через Enter. Чтобы прекратить вводить числа, введите 0 и нажмите Enter.')

while 1:
    user_input = input()
    if user_input.isdigit():
        num = int(user_input)

        if num < 10:
            continue
        elif num > 100 or num == 0:
            break
        else:
            print(num)

    else:
        print("Некорректный ввод.")