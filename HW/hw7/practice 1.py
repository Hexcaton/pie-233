#1
num = int(input('Введите целое число: '))
add = lambda x: x + 15
result = add(num)
print(result)

#2
x = int(input('Введите целое число x: '))
y = int(input('Введите целое число y: '))
multiply = lambda x, y: x * y
result = multiply(x, y)
print(result)

#3
list_int = [78, 2, 13, 46, 5, 61, 74, 81, 94, 10]
list_even = list(filter(lambda x: x % 2 == 0, list_int))
list_odd = list(filter(lambda x: x % 2 == 1, list_int))
print("Список четных чисел:", list_even)
print("Список нечетных чисел:", list_odd)

#4
from datetime import datetime
date_info = lambda dt: \
    (
    dt.strftime("\n%Y-%m-%d %H:%M:%S.%f")[:-3],
    dt.year,
    dt.month,
    dt.day,
    dt.strftime("%H:%M:%S.%f")[:-3]
    )

current_datetime = datetime.now()
result = date_info(current_datetime)

for item in result:
    print(item)