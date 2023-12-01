import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Ошибка: Деление на 0"
    return x / y

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

def fibonacci(n):
    if n <= 0:
        return "Ошибка. Введите положительное число."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def power(x, n):
    return x ** n

def trig_functions(x, function):
    if function == 'sin':
        return math.sin(x)
    elif function == 'cos':
        return math.cos(x)
    elif function == 'tan':
        return math.tan(x)
    else:
        return "Ошибка. Тригонометрическая функция введена не верно."

def main():
    while 1:
        print("\nВыберите действие:")
        print("1. Сумма")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Факториал")
        print("6. Фибоначчи")
        print("7. Возведение в степень")
        print("8. Тригонометрические функции (sin, cos, tan)")
        print("0. Exit")

        choice = input("Выберите (0-8): ")

        if choice == '0':
            print("Выход.")
            break
        elif choice in ['1', '2', '3', '4', '7']:
            x = float(input("Введите первое число: "))
            y = float(input("Введите второе число: "))
        elif choice in ['5', '6']:
            n = int(input("Введите положительное число: "))
        elif choice == '8':
            x = float(input("Введите угол: "))

        if choice == '1':
            print("Результат:", add(x, y))
        elif choice == '2':
            print("Результат:", subtract(x, y))
        elif choice == '3':
            print("Результат:", multiply(x, y))
        elif choice == '4':
            print("Результат:", divide(x, y))
        elif choice == '5':
            print("Результат:", factorial(n))
        elif choice == '6':
            print("Результат:", fibonacci(n))
        elif choice == '7':
            print("Результат:", power(x, y))
        elif choice == '8':
            trig_func = input("Введите тригонометрическую функцию (sin, cos, tan): ")
            print("Результат:", trig_functions(x, trig_func))
        else:
            print("Некорректный ввод. Пожалуйста, выберите между 0 и 8.")

if __name__ == "__main__":
    main()
