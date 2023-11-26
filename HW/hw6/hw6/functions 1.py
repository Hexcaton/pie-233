def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def main():
    for i in range(1, 11):
        result = fibonacci(i)
        print(f"fibonacci number {i} = {result}")

if __name__ == "__main__":
    main()