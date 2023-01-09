#преобразование данных

user_number = input('Enter a qty:')

if user_number.isdigit():
    user_number = int(user_number)

else:
    print('Data must be a number')
    exit()

price = 100

print(user_number * price)
print(type(user_number))

int_number = 20
float_number = 1.12
# print(int_number +float_number)

# number = 'some string'
#
# if isinstance(number, int):
#     print('Integer')
# elif isinstance(number, float):
#     print('Float')
# else:
#     print(f'{type(number)}Not a number')

#перевод в двоичную систему
# print(bin(int_number))
# Перевод в восьмеричную систему
# print(oct(int_number))
# Перевод в шестнадцатиричную систему
# print(hex(int_number))

# user_number = 0
# if user_number > 0:
#     print('Positive')
# elif user_number < 0:
#     print('Negative')
# else:
#     print('Zero')

wet = 95
max_wet = 75
#
# if wet > max_wet:
#     print('Danger situation')

# print(wet == max_wet)
# print(type(wet == max_wet))

print(wet != max_wet)
print(-wet)
print(wet * -1)



