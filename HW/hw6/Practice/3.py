def power(a, n):
    result = 1.0
    if n > 0:
        for i in range(n):
            result *= a
    elif n < 0:
        for i in range(-n):
            result /= a
    return result

a = float(input("Введите действительное положительное число a: "))
n = int(input("Введите целое число n: "))

result = power(a, n)
print(result)