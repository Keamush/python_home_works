def add(first: int, second: int):
    print(f'First value: {first}')
    print(f'Second value: {second}')
    return first + second


def say_hello(name: str):
    name += '!'
    name = name.title()
    return f'Hello, {name}!'

def first_func(x: int | float):
    def second_func(y: int | float):
        return x + y
    return second_func

def find_average(a,b,c=[1, 2, 3]):
    if isinstance(c, list):
        return sum([a, b, sum(c)]) / (len(c) + 2)
    return sum([a, b, c]) / 3


# args, kwargs
def make_something(*args, **kwargs):
    for number in args:
        print(number)
    for key, value in kwargs.items():
        print(f'{key}:{value}')

# make_something(1, 2, 3, 4, name='bob', last_name='smith')
#
# func = lambda x, y: x + y
# print(func(2, 2))



# print(find_average(1, 2))
# print(find_average(1, 2, [10, 20, 30]))
# print(find_average(1, 2, 3))


# при присвоении опред.значений аргумент становится именованным
# print(add(second=10, first=5))

# sum_numbers = first_func(10)(5)
# print(sum_numbers)
# print(sum_numbers(19))

# print(add(1, 2))
# print(add(4, 5))
# print(add('1', '2'))

# print(say_hello('john doe'))
#
# print(type(add))

names = ['Alf Zed', 'Jane Corner', 'Bob Smith']
print(sorted(names, key=lambda name: name.split(' ')[-1].lower()))