import re
sentence = input('Введите дату в формате ДД.ММ.ГГГГ: ')
result = re.findall(r'\d+\.\d+\.\d+', sentence)

if result:
    print(result[0])
else:
    print("Дата не найдена.")