def plus_two(number):
    try:
        result = number + 2
        print(result)
    except TypeError:
        print("Ожидаемый тип данных — число!")

plus_two(3)
plus_two("hello")
plus_two(10.5)