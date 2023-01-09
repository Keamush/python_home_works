from string import ascii_lowercase

full_name = 'John Doe'
full_name = full_name.lower()

# letters_count = {}

#подсчет количества букв в словах
# for char in full_name:
#     if char in ascii_lowercase:
#         letters_count[char] = full_name.count(char)
#
# print(letters_count)

find_value = 'john'

#найти в списках
# if full_name.startswith(find_value):
#     print(f'Full name contains {find_value.capitalize()}')

#разделение в список из строки
letters = list(find_value)
# print(letters)

#из списка в строку
#letters = list(find_value)
# print('|'.join(letters))
#
# print(find_value.find('o'))

print(find_value[2])

if find_value.find('r') == -1:
    print('Value not found')

