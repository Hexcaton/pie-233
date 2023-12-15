from datetime import datetime

# Введите две даты от пользователя
date_str1 = input("Введите первую дату в формате YYYY MM DD HH:MM:SS: ")
date_str2 = input("Введите вторую дату в формате YYYY MM DD HH:MM:SS: ")
date_format = '%Y %m %d %H:%M:%S'
date1 = datetime.strptime(date_str1, date_format)
date2 = datetime.strptime(date_str2, date_format)

delta = date2 - date1
days = delta.days
hours, remainder = divmod(delta.seconds, 3600)
minutes, seconds = divmod(remainder, 60)

print(f'Разница между датами:')
print(f'Дни: {days} дней')
print(f'Часы: {hours} часов')
print(f'Минуты: {minutes} минут')
print(f'Секунды: {seconds} секунд')
