def find_frequently_used_words(words: list[str]):
    """Return ten frequently used words in text"""
    _dict = dict()      #my_dict
    for word in words:
        words = word.split()
        _dict[word] = _dict.get(word, 0) + 1
    list = []
    for key, value in _dict.items():
        list.append((value, key))
        list.sort(reverse=True)
    print('Ten frequently used words:')
    for freq, word in list[0:10]:
        print(f'{word:>10} -> {freq:>3} times')










###cамое часто встречающее слово (одно):
    # list = []
    # for key, value in _dict.items():
    #     list.append((value, key))
    #     list.sort(reverse=True)
    # # print(f'The most frequently used word in text is `{list[0][1]}`, used `{list[0][0]}` times.')
    # return (f'The most frequently used word in text is `{list[0][1]}`, used `{list[0][0]}` times.')