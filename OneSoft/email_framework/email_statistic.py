import os
import re
from collections import defaultdict
from pathlib import Path
from functools import lru_cache
from tabulate import tabulate

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
    domains = defaultdict(int)
    with open(path) as file:
        for line in file:
            line = line.strip()
            if line:
                email = get_emails_from_string(line)
                if email:
                    domain = email.split('@').pop()
                    domains[domain] += 1

    sorted_domains = sorted(domains.values(), reverse=True)
    new_sorted_domains = {}
    for i in sorted_domains:
        for k in domains.keys():
            if domains[k] == i:
                new_sorted_domains[k] = domains[k]
                break

    choose_by_value = {}
    for key, value in new_sorted_domains.items():
        if value >= 1000:
            choose_by_value[key] = value
    print(tabulate(choose_by_value.items(), headers=['Domain', 'Qty'], tablefmt="grid"))
    # print(tabulate(new_sorted_domains.items(), headers=['Domain', 'Qty'], tablefmt="grid"))
    return domains


def main(path: str):
    """Main controller"""
    check = check_type_exist_of_file(path)
    if check:
        print(check)
        exit()
    domains = get_domains_from_file(path)



if __name__ == '__main__':
    emails_file = 'mbox.txt'
    path_to_emails = get_path(emails_file)
    main(path_to_emails)


