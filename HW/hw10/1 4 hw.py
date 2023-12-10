def div7(n):
    for i in range(n + 1):
        if i % 7 == 0:
            yield i

n = int(input('Введите число N'))
result = list(div7(n))
print(result)