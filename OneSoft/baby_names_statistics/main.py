import os
import configparser
from typing import List, Callable

from baby_names_statistics.handlers.error_handlers import check_folder_exist
from baby_names_statistics.handlers.file_handlers import get_list_of_files, read_data_from_file
from baby_names_statistics.handlers.normalize_handlers import filter_file_names, parse_year_gender
from baby_names_statistics.tools.most_least import find_most_least_names
from baby_names_statistics.tools.print_baby_names_statistics import print_statistics


def make_names_table(folder: str, filtered_files: List[str], ban_names: List[str]):
    """Make dict format [gender][year][name][number_of_names]"""
    names_table = {
        'girls': {},
        'boys': {}
    }
    for file in filtered_files:
        path = os.path.join(folder, file)
        names = read_data_from_file(path, ban_names)
        year, gender = parse_year_gender(file)
        names_table[gender][year] = names
    print(names_table)
    return names_table


def get_ban_names(config_file: str = 'config.ini'):
    """Get ban names from config file"""
    config = configparser.ConfigParser()
    config.read(config_file)
    ban_names = config['ban-names']['names'].split(', ')
    return ban_names


def main(folder: str, func: Callable):
    """Main controller of Baby names statistics"""
    if not check_folder_exist(folder):
        return f'Directory {folder} not exist'

    ban_names = get_ban_names()
    files = get_list_of_files(folder)
    filtered_files = filter_file_names(files)
    names_table = make_names_table(folder, filtered_files, ban_names)
    girls, boys = func(names_table)
    print_statistics(boys, girls)


funcs = {
    'most_least': find_most_least_names
}


if __name__ == '__main__':
    # current_dir = os.getcwd()
    # folder_path = os.path.join(current_dir, 'baby_names')
    # main(folder_path, funcs['most_least'])
    statistic = {
        1900: {
            'girl': 'Mary',
            'boy': 'Richard'
        },
        1901: {
            'girl': 'Rachel',
            'boy': 'Martinez'
        }
    }

    # for year, object in statistic.items():
    #     print(f'Year {year}. Girl: {object["girl"]}, Boy: {object["boy"]}')

    print(statistic.items())
