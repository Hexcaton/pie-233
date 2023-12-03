def min_taxi_cost(distance, tariff):
    distance.sort(reverse=True)
    tariff.sort()

    total_cost = 0

    for i in range(len(distance)):
        total_cost += distance[i] * tariff[i]

    return total_cost

distance = list(map(int, input("Введите расстояния от работы до домов: ").split()))
tariff = list(map(int, input('Введите тарифы за проезд одного километра в такси: ').split()))

result = min_taxi_cost(distance, tariff)
print(result)