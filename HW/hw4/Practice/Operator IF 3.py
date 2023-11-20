print("Введите два целых числа через Enter:")
A = int(input())
B = int(input())

if A == B:
    print(0, 0)
else:
    A = A + B
    B = A
    print(A, B)