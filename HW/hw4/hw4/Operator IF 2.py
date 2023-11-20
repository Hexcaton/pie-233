amount = int(input('Insert amount in KZT: '))
currency = int(input('Choose currency: [1] USD [2] EUR [3] RUB '))

rates = {'USD': 420, 'EUR': 510, 'RUB': 5.8}

if currency == 1:
    converted_amount = amount / 420
    print(converted_amount, 'USD')
elif currency == 2:
    converted_amount = amount / 510
    print(converted_amount, 'EUR')
else: #currency == 3:
    converted_amount = amount / 5.8
    print(converted_amount, 'RUB')