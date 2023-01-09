import re
from functools import lru_cache  #last resent usage -декоратор -не проверяет после первой прокерки слова это слова если еще раз встретиться, т.к. уже проверял и сохранил себе в кэш(справочник) что оно соответствует и прошло проверку по функциям уже

@lru_cache(maxsize=2000)
def exclude_words(word: str):
    """Check of word not in ban list"""
    ban_list = {'the', 'this', 'and', 'were', 'not', 'https', 'www', 'org'}
    return word not in ban_list


@lru_cache(maxsize=2000)
def normalize_line(line: str):
    """Normalize row from txt file"""
    url = re.search('https?://[^\s]+', line)
    if url:
        start = url.start()
        end = url.end()
        line = line[:start] + line[end: -1]

    words = re.findall(r'[a-zA-Z]{3,}', line)
    words_lower = map(str.lower, words)
    words_whithout_ban = filter(exclude_words, words_lower)
    words = list(words_whithout_ban)
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

#########