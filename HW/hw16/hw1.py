try:
    my_list = [1, 2, 3, 4, 5]
    index = 10
    value = my_list[index]
    print("Значение по индексу {}: {}".format(index, value))
except IndexError:
    print("Ошибка: Индекс за границами массива!")