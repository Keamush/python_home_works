import os
import json
from json import JSONDecodeError
from typing import List, Dict


def init_db(filename: str):
    if os.path.exists(filename):
        return True
    with open(filename, 'w') as file:
        pass


def read_user_credential(filename: str):
    with open(filename, 'r') as file:
        try:
            credentials = json.load(file)
        except JSONDecodeError:
            return []
    return credentials


def write_user_credential(filename: str, credentials: List[Dict[str, str]]):
    with open(filename, 'w') as file:
        json.dump(credentials, file, indent=4)


def main(username: str, pass_hash: str, filename: str):
    init_db(filename)
    credentials = read_user_credential(filename)
    new_user = {
        'username': username,
        'pass_hash': pass_hash
    }
    credentials.append(new_user)
    write_user_credential(filename, credentials)


DB_NAME = 'user.json'

if __name__ == '__main__':
    nick_name = 'pocker'
    user_pass_hash = '260000$LEKlPHCXsoS67dsU$e01f6a7d737fde785aba8a6a8a5a94117a689cb3c217c56b1b424a0478adbf60'
    main(nick_name, user_pass_hash, DB_NAME)
