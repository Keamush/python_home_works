
# глобальная область видимости
def say_hello():
    print(f'Hello, {name}')

# локальная область видимости
def say_hello_custom():
    global name
    name = 'Bob'
    print(f'Hello, {name}')

def outer():
    number = 5
    def inner():
        nonlocal number
        number = 25
        print(number)

    inner()
    print(number)

def get_input():
    user_choice = input('Enter some data: ')
    return user_choice

# функциональный стиль
def increment_state(data):
    return data + 1

state = 0

print(increment_state(state))
print(state)


# процедурный стиль
# def increment_state():
#     global state
#     state +=1
#
# state = 0
#
# increment_state()
# increment_state()
# increment_state()
# print(state)

# print(get_input())

# outer()

name = 'James'

# say_hello_custom()
# print(name)
# say_hello()
# say_hello_custom()
