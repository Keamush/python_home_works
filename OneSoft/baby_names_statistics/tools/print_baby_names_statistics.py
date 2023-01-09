from prettytable import PrettyTable


def print_statistics(boys, girls):
    table = PrettyTable()
    table.field_names = ['Year', 'Boy top name', 'Qty boy top', 'Boy bottom name', 'Qty boy bottom',
                         'Girl top name', 'Qty girl top', 'Girl bottom name', 'Qty girl bottom']
    for year_boy, year_girl in zip(boys, girls):
        if year_boy == year_girl:
            year = year_boy
            boy_top_name = boys[year]['top'].name
            boy_top_qty = boys[year]['top'].qty
            boy_bottom_name = boys[year]['bottom'].name
            boy_bottom_qty = boys[year]['bottom'].qty

            girl_top_name = girls[year]['top'].name
            girl_top_qty = girls[year]['top'].qty
            girl_bottom_name = girls[year]['bottom'].name
            girl_bottom_qty = girls[year]['bottom'].qty

            table.add_row([year, boy_top_name, boy_top_qty, boy_bottom_name, boy_bottom_qty,
                           girl_top_name, girl_top_qty, girl_bottom_name, girl_bottom_qty])
    print(table)
