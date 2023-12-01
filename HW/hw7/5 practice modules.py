import calendar
year = 2022
month = 8

cal = calendar.monthcalendar(year, month)
dates = [day for week in cal for day in week if day != 0]

print(dates)
