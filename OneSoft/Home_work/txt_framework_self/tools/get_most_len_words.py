def find_most_len_words(words: list[str]):
    """Return the longest words in text"""
    words_len = {word: len(word) for word in set(words)}    #set -множество -вытаскивает только слова по уникальности
    max_len = max(words_len.values())    #максимальная длина = 16
    most_len_words = [word for word in words if len(word) == max_len]    #['unenforceability']
    qty_words = {word: max_len for word in most_len_words}
    return qty_words