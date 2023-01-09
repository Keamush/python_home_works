import calendar

month_dict = dict()
for month_number in range(1, 13):
    month_dict[str(month_number)] = calendar.month_name[month_number].lower()

final_dict = {}

month_and_season = [
    [['12', '2', '1'], 'Winter'],
    [['3', '4', '5'], 'Spring'],
    [['6', '7', '8'], 'Summer'],
    [['9', '10', '11'], 'Autumn']
]

for i in month_and_season:
    month_numbers = i[0]
    season_name = i[1]
    for j in month_numbers:
        final_dict[j] = season_name

for mont_num in month_dict.keys():
    final_dict[month_dict[mont_num]] = final_dict[mont_num]

season_of_year = input('Please, enter number or name of month with lowercase: ')

if season_of_year.lower() in final_dict.keys():
    print('your input is', season_of_year + '.', 'Your season is', final_dict[season_of_year.lower()])
else:
    print('something is wrong with input')
