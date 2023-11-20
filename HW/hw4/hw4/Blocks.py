s = int(input('Стоимость подписки на онлайн-кинотеатр: '))
p = int(input('Стоимость пиццы: '))
m = int(input('Зарплата Пети: '))

if (s + p) < m:
    print('Да')
else: #(s + p) > m
    print('Нет')