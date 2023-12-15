from datetime import datetime as dt

str_input = input('Введите дату в следующем формате: день месяц год часы:минуты \n')
months_dict = {'января': 1, 'февраля': 2, 'марта': 3, 'апреля': 4, 'мая': 5, 'июня': 6,
               'июля': 7, 'августа': 8, 'сентября': 9, 'октября': 10, 'ноября': 11, 'декабря': 12}

format_string = "%d %m %Y %H:%M"

for month, month_number in months_dict.items():
    str_input = str_input.replace(month, str(month_number))

parsed_dt = dt.strptime(str_input, format_string)
format_output = "%Y-%m-%d %H:%M:%S"
str_output = parsed_dt.strftime(format_output)

print("Input:", str_input)
print("Output:", str_output)