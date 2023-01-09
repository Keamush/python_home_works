def find_underused_words(words: list[str]):
    """Return ten underused (used a little) words in text"""
    _dict = dict()
    for word in words:
        words = word.split()
        _dict[word] = _dict.get(word, 0) + 1
    list = []
    for key, value in _dict.items():
        list.append((value, key))
        list.sort(reverse=False)
    print('Ten underused words:')
    for underused, word in list[0:10]:
        print(f'{word:>10} -> {underused:>3} time')
