import functools
def log_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function '{func.__name__}' with arguments {args} and keyword arguments {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function '{func.__name__}' returned {result}")
        return result
    return wrapper

@log_function
def add(a, b):
    return a + b

@log_function
def multiply(x, y):
    return x * y

# Example usage
result_add = add(2, 3)
result_multiply = multiply(4, 5)

result = add(3, 5)
print(f"Result: {result}")

def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper

@my_decorator
def say_whee():
    print("Whee!")

