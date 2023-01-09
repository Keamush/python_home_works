letters_mapping = {'a': 2, 'b': 1, 'c': 2, 'd': 1, 'e': 2, 'f': 1, 'g': 2, 'h': 1}
result_color = {0: 'white', 1: 'black'}

position = input('insert chess board position here ')
if len(position) != 2:
    print('position should be 2 symbols. Example: "a1"')
else:
    position_letter = position[0]
    position_number = position[1]
    if (position_letter.lower() in list(letters_mapping.keys())):
        if position_number.isnumeric():
            position_number = int(position[1])
            if position_number == 0 or position_number == 9:
                print("can't use this number. Only numbers 1-8")
            else:
                print(result_color[(position_number + letters_mapping[position_letter]) % 2])
        else:
            print("the second symbol should be a number 1-8")
    else:
        print("the first symbol should be a letter A-H or a-h")
        
