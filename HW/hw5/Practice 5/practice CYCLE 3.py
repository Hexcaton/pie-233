limit = 100
i = 2

while i <= limit:
    divisors = [1]

    for j in range(2, i // 2 + 1):
        if i % j == 0:
            divisors.append(j)

    if sum(divisors) == i:
        print(i)

    i += 1