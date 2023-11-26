def power(base, exponent):
    return 1 if exponent == 0 else base * power(base, exponent - 1)

input_str = input("Введите число и его степень через пробел и нажмите Enter: ")
base, exponent = map(int, input_str.split())

result = power(base, exponent)
print(f"{base} в степени {exponent}: {result}")