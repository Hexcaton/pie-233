year = int(input('Введите год чтобы определить, является ли данный год високосным: '))
if year % 4 == 0:
    print("Этот год является високосным.")
else:
    print("Этот год не является високосным.")