def IsAscending(A):
    B = []
    for i in range(1, len(A)):
        if A[i - 1] < A[i]:
            B.append(A[i - 1])
        else:
            return "No"
        return "Yes"

A = []
num = float(input('Введите число или 0 для завершения: '))
while num != 0:
    A.append(num)
    num = float(input('Введите число или 0 для завершения: '))
result = IsAscending(A)
print(result)

