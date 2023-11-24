n = int(input('Введите натуральное число чтобы вычислить сумму 1!+2!+3!+...+число!\n'))
factorial = 1
sum = 0

for i in range(1, n + 1):
    factorial *= i
    sum += factorial

print(f'Сумма 1! + 2! + 3! + ... + ', n, '! равна', sum )