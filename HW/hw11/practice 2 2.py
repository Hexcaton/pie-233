from datetime import datetime
def days_in_month(year, month):
    first_day_of_month = datetime(year, month, 1)
    first_day_of_next_month = (first_day_of_month.replace(month=first_day_of_month.month % 12 + 1)
                               if first_day_of_month.month < 12
                               else first_day_of_month.replace(year=first_day_of_month.year + 1, month=1))

    days_in_month = (first_day_of_next_month - first_day_of_month).days
    return days_in_month

year = int(input("Введите год: "))
month = int(input("Введите месяц (числом): "))
days = days_in_month(year, month)
print(f"Количество дней в месяце: {days}")
