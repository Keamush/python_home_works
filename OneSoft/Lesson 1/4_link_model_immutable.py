numbers_one = 10
numbers_second = 3

# print(id(numbers_one)== id(numbers_second))
#
# numbers_one = numbers_second
# print(id(numbers_one)== id(numbers_second))

#определение изменяемая ли структура данных или нет
print(id(numbers_one))
numbers_one += 1
print(id(numbers_one))
#если при изменении типа данных (добавление 1) возвращается другой идентификатор значит это неизменяемый тип данных

name = 'bob'
print(id(name))
name += '!'
print(id(name))