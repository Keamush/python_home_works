import re
from typing import List


def filter_file_names(files: List[str]):
    """Filter file names use template year_BoysNames.txt or year_GirlsNames.txt"""
    filtered_files = []
    match_file_name = re.compile(r'^[1-2][0-9][0-9][0-9]_(BoysNames|GirlsNames)\.txt$')
    for file in files:
        file_name = match_file_name.match(file)
        if file_name:
            filtered_files.append(file)
    return filtered_files


def parse_names_qty_from_lines(line: str):
    """Parse name and number of names"""
    line = line.strip()
    match_line = re.match(r'[A-Z][a-z]+\s[0-9]+$', line)
    if match_line:
        name, qty = re.split(r'\s', match_line.group())
        return name, int(qty)
    return False


def parse_year_gender(filename: str):
    """Parse year and gender"""
    year = int(re.match(r'^[1-2][0-9][0-9][0-9]', filename).group())
    gender = re.search(r'Boys|Girls', filename).group().lower()
    return year, gender
