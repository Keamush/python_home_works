season_month_num_and_name = {
    '12': 'Winter', '1': 'Winter', '2': 'Winter',
    '3': 'Spring', '4': 'Spring', '5': 'Spring',
    '6': 'Summer', '7': 'Summer', '8': 'Summer',
    '9': 'Autumn', '10': 'Autumn', '11': 'Autumn',
    'january': 'Winter', 'february': 'Winter', 'december': 'Winter',
    'march': 'Spring', 'april': 'Spring', 'may': 'Spring',
    'june': 'Summer', 'july': 'Summer', 'august': 'Summer',
    'september': 'Autumn', 'october': 'Autumn', 'november': 'Autumn'
}

season_of_year = input('Please, enter number or name of month with lowercase: ')

if season_of_year.lower() in season_month_num_and_name.keys():
    print('Your input is', season_of_year + '.', 'Your season is', season_month_num_and_name[season_of_year.lower()] + '.')
else:
    print('something is wrong with input')
