from typing import List

def find_most_len_words(words: List[str]):
    """Returns the longest words in text"""
    words_len = {word: len(word) for word in words}
    max_len = max(words_len.values())
    most_len_words = [word for word in words if len(word) == max_len]
    qty_words = {word: max_len for word in most_len_words}
    return qty_words

