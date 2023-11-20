print('Введите сколько часов рекомендуется спать: ')
A = int(input())
print('Введите сколько часов пересыпать вредно: ')
B = int(input())
print('Введите сколько часов Аня спит: ')
H = int(input())

if (A < B) or (A == B):
    if H == A or (H < B and H > A):
        print('Это нормально')
    elif H < A:
        print('Недосып')
    elif H > B:
        print('Пересып')
else:
    print('Часы введены не верно.')