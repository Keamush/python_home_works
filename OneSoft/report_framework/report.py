import os
import re
from typing import List, NamedTuple, Dict
from datetime import datetime

from report_framework.file_handler import read_data_from_file


class DriverCompany(NamedTuple):
    driver: str
    company: str


def get_data_from_race_files(folder: str):
    """Get race data from files"""
    path_to_start = os.path.join(folder, 'start.log')
    path_to_end = os.path.join(folder, 'end.log')
    path_to_abbr = os.path.join(folder, 'abbreviations.txt')

    start_log = sorted(read_data_from_file(path_to_start))
    end_log = sorted(read_data_from_file(path_to_end))
    abbr_txt = sorted(read_data_from_file(path_to_abbr))

    return start_log, end_log, abbr_txt


def parse_data_from_log(data: List[str]):
    """Parse data from log files SVF2018-05-24_12:02:58.917"""
    racers = {}
    datetime_format = '%Y-%m-%d %H:%M:%S.%f'
    for race in data:
        racer_abbr = re.findall(r'^[A-Z]{3}', race).pop()
        race_date = re.findall(r'[0-9]{4}-[0-9]{2}-[0-9]{2}', race).pop()
        race_time = re.findall(r'[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{3}', race).pop()
        if not all([racer_abbr, race_date, race_time]):
            raise ValueError('Wrong data in race files')
        race_datetime = datetime.strptime(f'{race_date} {race_time}', datetime_format)
        racers[racer_abbr] = race_datetime
    return racers


def parse_data_from_abbr(abbrs: List[str]):
    """Parse data from abbreviations SVF_Sebastian Vettel_FERRARI"""
    abbrs_map = {}
    for line in abbrs:
        abbr, driver, company = line.split('_')
        abbrs_map[abbr] = DriverCompany(driver, company)
    return abbrs_map


def calc_results(start_data: Dict[str, datetime], end_data: Dict[str, datetime]):
    """Calc race results"""
    race_results = {}
    for racer, race_datetime in end_data.items():
        start_time = start_data[racer]
        end_time = race_datetime
        race_result = end_time - start_time if end_time >= start_time else start_time - end_time
        race_results[racer] = str(race_result)
    return race_results


def sort_race_logs(race_results: Dict[str, str], order: str):
    """Sort race log dict by values(asc, desc)"""
    reverse = False if order == 'asc' else True
    return dict(sorted(race_results.items(), key=lambda item: item[1], reverse=reverse))


def main(folder: str):
    """Main controller with business logic"""
    start_log, end_log, abbr_txt = get_data_from_race_files(folder)
    start_data = parse_data_from_log(start_log)
    end_data = parse_data_from_log(end_log)
    abbr_data = parse_data_from_abbr(abbr_txt)
    race_results = calc_results(start_data, end_data)
    return race_results, abbr_data

