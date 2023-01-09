import argparse
from argparse import Namespace
from typing import List


def parse_args() -> Namespace:
    """Parse arguments from console"""
    parser = argparse.ArgumentParser(
        prog='Delete comments App',
        usage='%(prog)s delete_comments.py --input "<filename>" '
              '[--output "<filename>" default value clean_code_out.py]',
        description='Delete comments from source code')
    parser.add_argument(
        '-i',
        '--input',
        type=str,
        help='path to source code file',
        required=True)
    parser.add_argument(
        '-o',
        '--output',
        type=str,
        help='path to clean output file, default clean_code_out.py',
        required=False,
        default='clean_code_out.py')
    args = parser.parse_args()
    return args


def check_file_exist(filename_input: str):
    """Check if file exist and has text bites"""
    try:
        open(filename_input).read()
    except FileNotFoundError as error:
        return error
    except UnicodeDecodeError:
        return 'File must be text format'
    return False


def normalize_code_line(line: str, comment_char: str):
    """Normalize code line exclude comment_char variable"""
    if line.strip().startswith(comment_char):
        return False

    if comment_char in line:
        char_index = line.index(comment_char)
        line = line[:char_index] + '\n'
    return line


def read_code_from_file(filename_input: str, comment_char: str):
    """Read code from file and delete comments"""
    normalized_code = []
    with open(filename_input) as code_file:
        for line in code_file:
            normalized_line = normalize_code_line(line, comment_char)
            if normalized_line:
                normalized_code.append(normalized_line)
    return normalized_code


def write_code_to_file(filename_output: str, code: List[str]):
    """Write code lines into file"""
    with open(filename_output, 'w') as code_file:
        for line in code:
            code_file.write(line)
    return True


def main(filename_input: str, filename_output: str, comment_char: str):
    """Main controller"""
    check = check_file_exist(filename_input)
    if check:
        print(check)
        return False
    code = read_code_from_file(filename_input, comment_char)
    if write_code_to_file(filename_output, code):
        print(f'Normalized code from file {filename_input} in {filename_output}')


CHAR_TO_DELETE = '#'

if __name__ == '__main__':
    cli_args = parse_args()
    input_code = cli_args.input
    output_code = cli_args.output
    main(input_code, output_code, CHAR_TO_DELETE)
