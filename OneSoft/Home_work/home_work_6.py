from string import punctuation

def find_longest_word(filename):
    longest_word = ''
    with open(filename, 'r') as file:
       for word in file.read().split():
           word = word.strip(punctuation)
           if len(word) >= len(longest_word):
                longest_word = word
    file.close()
    return longest_word


print(find_longest_word('romeo.txt'))

