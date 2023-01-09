from collections import Counter
import numpy as np


def get_dict_key_on_value(value):
    return list(counter_word.keys())[list(counter_word.values()).index(value)]


with open('romeo.txt', 'r') as file:
    word_list = []
    for word in file.read().split():
        clear_word = ""
        for letter in word:
            if letter.isalpha():
                clear_word += letter.lower()
        word_list.append(clear_word)

counter_word = Counter(word_list)
top_3_freq_words_cnt = list(np.sort(list(counter_word.values())))[-3:]
bot_3_freq_words_cnt = np.sort(list(counter_word.values()))[:3]


print(counter_word)


print()

letters_count = 0
for word in counter_word.keys():
    letters_count += len(word) * counter_word[word]
# то же самое, но через генератор
# [len(word) * counter_word[word] for word in counter_word.keys()].sum()

print('amt of letters: ', letters_count)
print('most frequent words are')
for word_value in top_3_freq_words_cnt:
    print('word', '"' + str(get_dict_key_on_value(word_value)) + '"', 'in text', word_value, 'times')

min_word_counter = 0
for word in counter_word.keys():
    if counter_word[word] == 1:
        print('word', '"' + word + '"', 'in text', str(1), 'times')
        min_word_counter += 1
    if min_word_counter >= 3:
        break

word_freq_dict = {}
for i in counter_word.values():
    if i in word_freq_dict.keys():
        word_freq_dict[i] += 1
    else:
        word_freq_dict[i] = 1


print('ok')

