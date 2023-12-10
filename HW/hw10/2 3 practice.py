def i_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<i>{result}</i>"
    return wrapper

def s_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<strong>{result}</strong>"
    return wrapper

@i_decorator
@s_decorator
def get_text():
    return "Hello, World!"

result = get_text()
print(result)