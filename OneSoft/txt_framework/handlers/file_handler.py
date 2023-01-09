import re
from functools import lru_cache

@lru_cache(maxsize=2000)
def exclude_words(word: str):
    """Check if word not in ban list"""
    ban_list = {'the', 'and', 'this', 'were', 'not', 'https', 'www', 'org'}
    return word not in ban_list
    # return word not in ban_list

@lru_cache(maxsize=2000)
def normalize_line(line: str):
    """Normalize row from txt file"""
    words = re.findall(r'[a-zA-Z]{1,}', line)
    words_lower = map(str.lower, words)
    words_without_ban = filter(exclude_words, words_lower)
    words = list(words_without_ban)
    return words


def read_data_from_file(filename: str):
    """Read data from txt file"""
    result = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line:
                normalized_line = normalize_line(line)
                result.extend(normalized_line)
    return result

