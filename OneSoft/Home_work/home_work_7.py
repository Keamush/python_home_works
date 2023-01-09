from collections import Counter
import numpy as np

def key_on_value(value):
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
top_3_often_words_cnt = list(np.sort(list(counter_word.values())))[-3:]
less_3_often_words_cnt = np.sort(list(counter_word.values()))[:3]

letters_count = 0
for word in counter_word.keys():
    letters_count += len(word) * counter_word[word]

# print(counter_word)
print('Amount of letters: ', letters_count)
print('\nMost often use 3 words are: ')
for word_value in top_3_often_words_cnt:
    print('word', '"' + str(key_on_value(word_value)) + '"', 'in text', word_value, 'times')

min_word_counter = 0
print('\nRarely use 3 words are: ')
for word in counter_word.keys():
    if counter_word[word] == 1:
        print('word', '"' + word + '"', 'in text', str(1), 'times')
        min_word_counter += 1
    if min_word_counter >= 3:
        break


