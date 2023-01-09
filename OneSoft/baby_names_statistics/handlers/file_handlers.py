import os
from typing import List

from baby_names_statistics.handlers.error_handlers import check_file_exist, check_file_type
from baby_names_statistics.handlers.normalize_handlers import parse_names_qty_from_lines


def get_list_of_files(folder: str):
    """Get list of files in folder"""
    files = os.listdir(folder)
    return files


def read_data_from_file(path: str, ban_names: List[str]):
    """Read statistics from file"""
    if not check_file_exist(path):
        return False
    if not check_file_type(path):
        return False

    names = {}
    with open(path) as file_names:
        for line in file_names:
            line = parse_names_qty_from_lines(line)
            if line:
                name, qty = line
                if name in ban_names:
                    name = name[0] + '*' * len(name[1:])
                names[name] = qty
    return names
