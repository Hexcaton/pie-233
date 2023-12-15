from datetime import datetime, timedelta
def last_day_of_month(year, month):
    first_day_of_next_month = datetime(year, month, 1) + timedelta(days=32)
    last_day = (first_day_of_next_month.replace(day=1) - timedelta(days=1)).day
    return last_day

year = int(input("Введите год: "))
month = int(input("Введите месяц (числом): "))
last_day = last_day_of_month(year, month)
print(f"Последний день месяца: {last_day}")