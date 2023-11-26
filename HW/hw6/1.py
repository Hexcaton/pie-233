def IsAscending(A):
    for i in range(1, len(A)):
        if A[i] <= A[i - 1]:
            return "No"

    return "Yes"

input_list = [1, 7, 9]
result = IsAscending(input_list)
print(result)