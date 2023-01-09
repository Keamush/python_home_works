import re

row = 'VB,4 Analitics 5 company 203 AV17'
match_av = re.compile(r'[a-zA-Z][a-bA-B][,.][0-3]')
find_match_av = match_av.match(row)

numbers = re.findall(r'[0-9]+', row)
print(numbers)

phones = 'Jane phone number: 099-111-22-33\nJames phone number: 036-444-55-66\n095-111-22-33'
find_phone_numbers = re.findall(r'09[0-9]-[0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]', phones)
print(find_phone_numbers)


# if find_match_av:
#     print(find_match_av.group())

text = 'Im in the right place now круто тут'
words_grater_three_letters = re.findall(r'[a-zA-Z]{3,}|[а-яА-Я]{5,}', text)
print(words_grater_three_letters)
