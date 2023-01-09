white_letter_1st = ['a', 'c', 'e', 'g']
white_number_1st = ['2', '4', '6', '8']
white_letter_2nd = ['b', 'd', 'f', 'h']
white_number_2nd = ['1', '3', '5', '7']

letters = white_letter_1st + white_letter_2nd
numbers = white_number_1st + white_number_2nd

chess_field_letter_init = input('Please, enter letter of field: ')
chess_field_letter_lower = chess_field_letter_init.lower()
chess_field_number = input('Please, enter number of field: ')


if (chess_field_letter_lower in letters) and (chess_field_number in numbers):
    if ((chess_field_letter_lower in white_letter_1st) and (chess_field_number in white_number_1st)) \
            or ((chess_field_letter_lower in white_letter_2nd) and (chess_field_number in white_number_2nd)):
        print('White!')

    else:
        print('Black!')
else:
    print('Wrong value!')
