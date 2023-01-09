import os
from pathlib import Path


from txt_framework import examples
from examples import ROMEO as romeo_example
from txt_framework.handlers.error_handler import check_file
from txt_framework.handlers.file_handler import read_data_from_file
from txt_framework.tools.get_most_len_words import find_most_len_words


PATH_TO_ROMEO_EXAMPLE = os.path.join(Path(examples.__file__).parent, romeo_example)


def main(filename: str):
    """Main controller"""
    check = check_file(filename)
    if check:
        return check
    data = read_data_from_file(filename)
    most_len_words = find_most_len_words(data)
    return most_len_words


if __name__ =='__main__':
    print(main(PATH_TO_ROMEO_EXAMPLE))
