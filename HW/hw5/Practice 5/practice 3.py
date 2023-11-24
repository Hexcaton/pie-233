total_sum = 0

print("Введите целые числа через Enter для расчёта их суммы. Чтобы прекратить вводить числа, введите 0 и нажмите Enter. ")

while 1:
    num = int(input())

    if num == 0:
        break
    else:
        total_sum += num

print(total_sum)