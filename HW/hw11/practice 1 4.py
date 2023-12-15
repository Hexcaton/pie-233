import datetime

current_date_time = datetime.datetime.now()
current_time = current_date_time.time()
formatted_time = current_time.strftime("%H: %M: %S. %f")
print('Format:: ', formatted_time)