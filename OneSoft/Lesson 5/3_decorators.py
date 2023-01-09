def verbose(func):
    def wrapper(*args, **kwargs):
        print(f'Call function: {func.__name__}')
        return func(*args, **kwargs)
    return wrapper

@verbose
def lower(variable: str):
    return variable.lower()

@verbose
def upper(variable: str):
    return variable.upper()

@verbose
def capitalize(variable: str):
    return variable.capitalize()

name = 'John'
print(lower(name))
print(upper(name))
print(capitalize(name))

