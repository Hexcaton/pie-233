from datetime import datetime, timedelta
def count_first_day_mondays(start_year, end_year):
    count = 0
    current_date = datetime(start_year, 1, 1)
    while current_date.year <= end_year:
        if current_date.weekday() == 0:
            count += 1
        current_date += timedelta(days=365 if current_date.year % 4 != 0 or (
                    current_date.year % 100 == 0 and current_date.year % 400 != 0) else 366)
    return count

start_year = int(input("Введите начальный год: "))
end_year = int(input("Введите конечный год: "))
result = count_first_day_mondays(start_year, end_year)
print(f"Число понедельников 1-го числа месяца: {result}")
