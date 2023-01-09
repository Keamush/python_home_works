import argparse
from typing import Dict, List, Tuple
from prettytable import PrettyTable
from tabulate import tabulate

from report_framework.report import main as main_report, sort_race_logs, DriverCompany


def parse_args():
    """Parse arguments from command line"""
    parser = argparse.ArgumentParser(
        prog='Report F1 framework',
        usage='%(prog)s cli_interface.py --files "<path_to_folder>" [--asc | --desc] [--driver]',
        description='Show report about F1 race results')
    parser.add_argument(
        '--files',
        type=str,
        help='path to folder with race logs',
        required=True)
    parser.add_argument(
        '--asc',
        action='store_true',
        help='ordering by ascending',
        default=False,
        required=False)
    parser.add_argument(
        '--desc',
        action='store_true',
        help='ordering by descending',
        default=False,
        required=False)
    parser.add_argument(
        '--driver',
        type=str,
        help='Show information about driver',
        default='',
        required=False)
    args = parser.parse_args()
    return args


def prepare_race_table(race_results: Dict[str, str], abbrs: Dict[str, DriverCompany], current_driver: str):
    """Prepare race data to console print"""
    race_table = []
    for counter, code in enumerate(race_results, 1):
        driver = abbrs[code].driver
        company = abbrs[code].company
        race_time = race_results[code]
        if current_driver:
            if driver == current_driver:
                race_table.append((counter, driver, company, race_time))
                break
            continue
        race_table.append((counter, driver, company, race_time))

    if current_driver and not race_table:
        return False
    return race_table


def print_race_table_prettytable(race_table: List[Tuple[str, str, str, str]], place_limit: int = 15):
    """Print race table with PrettyTable"""
    table = PrettyTable()
    table.field_names = ['№', 'Driver', 'Company', 'Time']
    for counter, driver, company, race_time in race_table:
        table.add_row([counter, driver, company, race_time])
        if counter == place_limit:
            table.add_row(['*', '*', '*', '*'])
    print(table)


def print_race_table_tabulate(race_table: List[Tuple[str, str, str, str]], place_limit: int = 15):
    """Print race table with PrettyTable"""
    table = []
    for counter, driver, company, race_time in race_table:
        table.append([counter, driver, company, race_time])
        if counter == place_limit:
            table.append(['*', '*', '*', '*'])
    print(tabulate(table, headers=['№', 'Driver', 'Company', 'Time'], tablefmt='jira'))


def main(folder: str, order_asc: bool = True, order_desc: bool = False, driver: str = ''):
    """Main controller of cli_module"""
    if order_asc and order_desc:
        print('Cannot use two ordering options together: --asc --desc')
        return False
    try:
        race_results, abbrs = main_report(folder)
    except FileNotFoundError as error:
        print(error)
        return False
    order = 'desc' if order_desc else 'asc'
    race_results_sorted = sort_race_logs(race_results, order)
    race_table = prepare_race_table(race_results_sorted, abbrs, driver)
    if not race_table:
        print(f'Driver {driver} not found')
        return False
    print_race_table_tabulate(race_table)


if __name__ == '__main__':
    args = parse_args()
    folder = args.files
    order_asc = args.asc
    order_desc = args.desc
    driver = args.driver
    main(folder, order_asc, order_desc, driver)
