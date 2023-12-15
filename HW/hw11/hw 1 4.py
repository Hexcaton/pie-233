import datetime
def addYears(originalDate, years):
    try:
        newDate = originalDate.replace(year=originalDate.year + years)
        return newDate
    except ValueError:
        return originalDate

originalDate = input('Введите дату в формате YYYY, MM, DD: ')
year, month, day = map(int, originalDate.split(','))
dateFormat = datetime.date(year, month, day)
yearsToAdd = int(input('Введите количество лет для изменения даты: '))

result_date = addYears(dateFormat, yearsToAdd)
print(f'Новая дата после изменения: {result_date}')
