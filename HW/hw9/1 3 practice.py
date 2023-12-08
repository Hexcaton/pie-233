import re
sentence = input('Введите номер телефона в формате Х.ХХХ.ХХХ.ХХХХ: ')
result = re.findall(r'\d\.\d{3}\.\d{3}\.\d{4}', sentence)

if result:
    print(result[0])
else:
    print("Некорректный ввод.")