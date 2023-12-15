from datetime import datetime
import time
def print_with_delay(message, repetitions, delay):
    for _ in range(repetitions):
        print(message)
        time.sleep(delay)

message = input("Введите строку для печати: ")
repetitions = 5
delay = 3
print_with_delay(message, repetitions, delay)
