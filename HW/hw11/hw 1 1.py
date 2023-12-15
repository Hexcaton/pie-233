import datetime

date_input = input('Введите дату в формате YYYY, MM, DD: ')
try:
    input_format = datetime.datetime.strptime(date_input, '%Y, %m, %d')
except ValueError:
    print('Некорректный формат ввода.')

week_num = input_format.strftime('%U')
print(week_num)