import re

with open('../romeo.txt', 'r', encoding='utf-8') as file:
    text = file.read()

text = text.replace('\n', ' ')
text = re.sub(r'[^\w\s]', ' ', text)
text = re.sub(' +', ' ', text)

text = text.split(' ')


def restrict_words(word):
    if 'http' in word:
        return False
    elif '*' in word:
        return False
    elif '#' in word:
        return False
    elif '@' in word:
        return False
    elif '(' in word:
        return False
    elif '/' in word:
        return False
    elif '-' in word:
        return False
    else:
        return True


words_len = {}


def remove_punctuation(word):
    word_wo_punctuation = re.sub(r',.?!', " ", word)
    return word_wo_punctuation


for word in text:
    if restrict_words(word):
        word = remove_punctuation(word)
        len_of_word = len(word)
        if len_of_word in words_len.keys():
            words_len[len_of_word].append(word)
        else:
            words_len[len_of_word] = [word]

print(words_len[max(list(words_len.keys()))])