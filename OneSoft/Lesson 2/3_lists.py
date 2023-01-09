numbers = [1, -16, 7, 0 ,100, 25]

# numbers.append(4)
# print(numbers)
#
# numbers.insert(1, 1000)
# print(numbers)
#
# numbers.extend([0.1, 0.2, 0.4])
# print(numbers)
#
# search_number = 1000
#
# print(numbers.index(search_number))
#
# if search_number in numbers:
#     numbers.remove(search_number)
#
# print(numbers)

#сортировка
# numbers.sort()
# print(numbers)
#
# #обратная сортировка
# numbers.sort(reverse=True)
# print(numbers)
#
# print(list(reversed(numbers)))
# print(numbers)
#
# print(sorted(numbers, reverse=True))

search_value = -16
new_value = -10

for index, number in enumerate(numbers):
    if number == search_value:
        numbers[index] *= new_value

print(numbers)