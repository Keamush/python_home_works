import os
from pathlib import Path
from typing import Callable

from Home_work.txt_framework_self import examples
from examples import ROMEO as romeo_example     #можно здесь изменить название файла romeo и дальше использовать romeo_example
from Home_work.txt_framework_self.handlers.error_handler import check_file
from Home_work.txt_framework_self.handlers.file_handler import read_data_from_file
from Home_work.txt_framework_self.tools.get_most_len_words import find_most_len_words
from Home_work.txt_framework_self.tools.get_frequently_used_words import find_frequently_used_words
from Home_work.txt_framework_self.tools.get_underused_words import find_underused_words
from Home_work.txt_framework_self.tools.get_number_of_letters import count_number_of_letters

#показываем путь к файлу C:\Users\user\Desktop\Python Homework\PC projects\txt_framework_self\examples\romeo.txt
PATH_TO_ROMEO_EXAMPLE = os.path.join(Path(examples.__file__).parent, romeo_example)


def main(filename: str, func: Callable):
    """Main controller"""
    check = check_file(filename)
    if check:
        return check
    data = read_data_from_file(filename)
    result = func(data)
    return result


funcs = {
    'most_len_words': find_most_len_words,
    'frequently_used_words': find_frequently_used_words,
    'underused_words': find_underused_words,
    'number_of_letters': count_number_of_letters
}

if __name__ == '__main__':
    user_func_1 = funcs['most_len_words']
    user_func_2 = funcs['frequently_used_words']
    user_func_3 = funcs['underused_words']
    user_func_4 = funcs['number_of_letters']
    print(main(PATH_TO_ROMEO_EXAMPLE, user_func_4))

