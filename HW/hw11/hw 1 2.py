import datetime
def FindFirstMonday(year, week):
    firstDay = datetime.datetime(year, 1, 1)
    firstDayOfWeek = firstDay.weekday()
    daysAdd = (7 - firstDayOfWeek) % 7
    firstMonday = firstDay + datetime.timedelta(days=daysAdd + (week - 1) * 7)
    return firstMonday

date_input = input('Введите в формате YYYY, W: ')
year, week = map(int, date_input.split(','))
result = FindFirstMonday(year, week)
print(f'пн {result}')