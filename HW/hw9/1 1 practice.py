import re
sentence = input('Введите ваше предложение чтобы вывести первое слово: ')
result = re.split(r' ', sentence)
print(result[0])