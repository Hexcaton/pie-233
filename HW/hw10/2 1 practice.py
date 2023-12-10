def i_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<i>{result}</i>"
    return wrapper

def text():
    return "Hello, World!"

result = text()
print(result)