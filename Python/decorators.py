def decorator(func):
    def wrapper(*args, **kwargs):
        func_val = func(*args, **kwargs)
        print("I am decorating your function!!!!")
        return func_val

    return wrapper


@decorator
def hello_world(person):
    return f"Hello {person}"

print(hello_world("Amit"))

def calc(func):
    def wrapper(*args, **kwargs):
        value = func(*args)
        print(f"Performing {func.__name__} on {args[0]} and {args[1]}")
        return value

    return wrapper


@calc
def add(x, y):
    return x + y


@calc
def sub(X, Y):
    return X - Y


@calc
def mul(X, Y):
    return X * Y


@calc
def div(X, Y):
    return X // Y


a = 46
b = 23
print("=>", add(a, b))
print("=>", sub(a, b))
print("=>", mul(a, b))
print("=>", div(a, b))
