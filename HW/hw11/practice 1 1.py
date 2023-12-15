import datetime

current_time = datetime.datetime.now()
print(current_time)

current_year = current_time.year
print(current_year)

current_month = current_time.month
print(current_month)

current_week_num = current_time.strftime('%U')
print(current_week_num)

current_day_num = current_time.day
print(current_day_num)

current_week_day = current_time.weekday()
print(current_week_day)