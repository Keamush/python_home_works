import os
import re
from collections import Counter
from typing import List, Tuple
from pathlib import Path
from functools import lru_cache

from prettytable import PrettyTable

import email_data


def get_path(filename: str):
    """Get path to file with emails"""
    folder = Path(email_data.__file__).parent
    path = os.path.join(folder, filename)
    return path


def check_type_exist_of_file(path: str):
    """Check if file exist and has text format"""
    try:
        open(path).read()
    except FileNotFoundError as error:
        return error
    except UnicodeDecodeError:
        return f'File {path} must be text format'
    return False


@lru_cache
def get_emails_from_string(line: str):
    """Find emails in string with re"""
    email_pattern = re.compile(r'([a-zA-Z0-9+._-]+@[a-zA-Z0-9._-]+\.[a-zA-Z0-9_-]+)')
    email = email_pattern.search(line)
    if email:
        email = email.group()
        return email
    return False


def get_domains_from_file(path: str):
    """Get domains from emails log file"""
    domains = []
    with open(path) as file:
        for line in file:
            line = line.strip()
            if line:
                email = get_emails_from_string(line)
                if email:
                    domain = email.split('@').pop()
                    domains.append(domain)
    return domains


def calc_domains(domains: List[str], qty: int = 5):
    """Calculate domains"""
    return Counter(domains).most_common(qty)


def print_domains_statistics(domains: List[Tuple[str, int]]):
    """print domains statistics"""
    table = PrettyTable()
    table.field_names = ['Domain', 'QTY']
    for domain, qty in domains:
        table.add_row([domain, qty])
    print(table)


def main(path: str):
    """Main controller"""
    check = check_type_exist_of_file(path)
    if check:
        print(check)
        exit()
    domains = get_domains_from_file(path)
    top_domains = calc_domains(domains)
    print_domains_statistics(top_domains)


if __name__ == '__main__':
    emails_file = 'mbox.txt'
    path_to_emails = get_path(emails_file)
    main(path_to_emails)

