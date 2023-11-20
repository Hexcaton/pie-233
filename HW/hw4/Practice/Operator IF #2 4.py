print('Выберите тип фигуры комнаты: 1 для треугольной, 2 для прямоугольной, 3 для круглой:')
choice = int(input())
CONSTANT_pi = 3.14

if choice == 1:
    print('Введите 3 стороны треугольника через Enter: ')
    a = float(input())
    b = float(input())
    c = float(input())

    # Полупериметр треугольника
    p = (a + b + c) / 2
    # Площадь треугольника по формуле Герона
    S = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print("Площадь комнаты:", S)

elif choice == 2:
    print('Введите 2 длины прямоугольника через Enter: ')
    a = float(input())
    b = float(input())

    # Площадь прямоугольника
    S = a * b
    print("Площадь комнаты:", S)

elif choice == 3:
    print('Введите радиус круга через Enter: ')
    r = float(input())

    # Площадь круга
    S = CONSTANT_pi * r**2
    print("Площадь комнаты:", S)

else:
    print("Некорректный выбор. Пожалуйста, введите 1, 2 или 3.")