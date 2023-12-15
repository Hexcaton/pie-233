import datetime
def FindSundays(year):
    firstDay = datetime.datetime(year, 1, 1)
    firstDayOfWeek = firstDay.weekday()
    days_add = (6 - firstDayOfWeek) % 7
    first_sunday = firstDay + datetime.timedelta(days=days_add)
    sundays = [first_sunday]
    current_sunday = first_sunday
    while current_sunday.year == year:
        current_sunday += datetime.timedelta(days=7)
        sundays.append(current_sunday)
    return sundays

year = int(input('Введите год: '))
all_sundays = FindSundays(year)
for sunday in all_sundays:
    print(f'Воскресенье: {sunday}')