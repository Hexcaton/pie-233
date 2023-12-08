def BringMoney(quantity, price_list):
    price_list.sort(reverse=True)
    to_bring = sum(sum(price_list[i:i+2]) for i in range(0, len(price_list), 3))
    return to_bring

quantity = int(input("Введите количество предметов, которые хотите купить: "))
print('Введите цены на товары:')
price_list = list(map(int, input().split()))
result = BringMoney(quantity, price_list)
print(result, price_list)