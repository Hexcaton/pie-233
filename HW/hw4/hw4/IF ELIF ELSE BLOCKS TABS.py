ticket_num = str(input('Введите номер билета из 6 цифр: '))
if ticket_num.isdigit() and ticket_num[0].isdigit() and ticket_num[1].isdigit() and ticket_num[2].isdigit() and ticket_num[3].isdigit() and ticket_num[4].isdigit() and ticket_num[5].isdigit():
    sum_first_half = int(ticket_num[0]) + int(ticket_num[1]) + int(ticket_num[2])
    sum_second_half = int(ticket_num[3]) + int(ticket_num[4]) + int(ticket_num[5])

    if sum_first_half == sum_second_half:
        print("Счастливый")
    else:
        print("Обычный")
else:
    print("Некорректный ввод. Введите шестизначное число.")

