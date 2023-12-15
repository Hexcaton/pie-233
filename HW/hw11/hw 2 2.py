import datetime

date_str1 = input("Введите первую дату в формате YYYY MM DD: ")
date_str2 = input("Введите вторую дату в формате YYYY MM DD: ")
date_format = '%Y %m %d'
date1 = datetime.datetime.strptime(date_str1, date_format)
date2 = datetime.datetime.strptime(date_str2, date_format)
delta = date2 - date1
print(f'Разница между датами: {delta.days} дней.')
