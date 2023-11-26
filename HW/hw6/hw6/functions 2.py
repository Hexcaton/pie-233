def is_power_of_two(num):
    return num > 0 and (num & (num - 1)) == 0

number = int(input("Enter a number: "))
print(is_power_of_two(number))