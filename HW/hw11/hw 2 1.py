import datetime

utc_now = datetime.datetime.utcnow()
local_timezone = datetime.datetime.now().astimezone().tzinfo
local_now = datetime.datetime.now()

print(f'Текущее время по Гринвичу (UTC): {utc_now}')
print(f'Текущее местное время: {local_now}')