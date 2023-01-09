strings = ['roses', 'are', 'red']
print(id(strings))

#чтобы посмотреть айди каждого слова нужно сделать запрос каждого слова начиная индекс с нуля

print(strings[0], strings[1], strings[2])
print(id(strings[0]), id(strings[1]), id(strings[2]))

#определение, что список имеет неизменяемый тип данных  и в результате идентификатор не меняется
#append - добавляет в конце списка значение

# strings.append('new')
# print(id(strings))

# new_strings = strings
# print(new_strings)
# new_strings.append('new')
# print(new_strings)

# new_strings=strings.copy()
# print(new_strings)
# new_strings.append('new')
# print(new_strings)
# print(strings)

# strings = ['roses', ['are', 'red']]
# print(strings[1][0])
# new_strings=strings.copy()
# new_strings [1][0] = 'new'
# print(new_strings, strings)

