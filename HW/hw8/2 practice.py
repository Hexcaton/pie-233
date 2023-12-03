def KthAppearance(A, a, k):
    count = 0
    for i in range(len(A)):
        if A[i] == a:
            count += 1
            if count == k:
                return i + 1
    return -1

A = []
num = float(input('Введите число или 0 для завершения: '))
while num != 0:
    A.append(num)
    num = float(input('Введите число или 0 для завершения: '))

a = float(input('Введите число a: '))
k = int(input('Введите число k: '))
result = KthAppearance(A, a, k)
print(result)