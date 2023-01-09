from types import MappingProxyType
from collections import namedtuple
from typing import Tuple

from prettytable import Prettytable


Month = namedtuple('Month', 'number name')
a = Month(1, 'January')

SEASONS = MappingProxyType(
    {
        'winter':(
            Month(12, 'December'),
            Month(1, 'January'),
            Month(2, 'February')
        ),
        'spring':(
            Month(3, 'March'),
            Month(4, 'April'),
            Month(5, 'May')
        ),
        'summer':(
            Month(6, 'June'),
            Month(7, 'July'),
            Month(8, 'August')
        ),
        'autumn':(
            Month(9, 'September'),
            Month(10, 'October'),
            Month(11, 'November')
        )
    }
)

# print(SEASONS['winter'])
# print(SEASONS.items())

# del SEASONS ['fall']

if __name__ == '__main__':
    user_month = '1'

    if user_month.isdigit():
        user_month = int(user_month)
    else:
        user_month = user_month.capitalize()

    for season in SEASONS:
        for month in SEASONS[season]:
            if user_month in month:
                print(f'Your choice "{month.name}" refers to the season "{season}"')
                exit()

    print(f'Your choice "{user_month}" is not correct')
    print(f'Use next values')
    #
    # cli_table = Prettytable()
    # cli_table.field_names = ['Season', 'Number', 'Name']
    #
    # months: tuple[Month, Month, Month]
    # for season, months in SEASONS.items()
    #     for month in months:
    #         cli_table.add_row([season, month.number, month.name])
    # print(cli_table)
    #

