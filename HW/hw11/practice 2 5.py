from datetime import datetime, timedelta
def get_dates_30_days_around_current():
    current_date = datetime.now()
    date_30_days_before = current_date - timedelta(days=30)
    date_30_days_after = current_date + timedelta(days=30)
    return date_30_days_before, current_date, date_30_days_after

dates = get_dates_30_days_around_current()
print(f"Дата 30 дней назад: {dates[0].strftime('%Y-%m-%d')}")
print(f"Текущая дата: {dates[1].strftime('%Y-%m-%d')}")
print(f"Дата 30 дней вперед: {dates[2].strftime('%Y-%m-%d')}")