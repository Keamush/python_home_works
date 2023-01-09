from string import ascii_lowercase
from typing import Any, Dict

def check_data_type(cell: Any, size: Any):
    """Check data type, raise Type error"""
    if not isinstance(cell, str):
        raise TypeError(f'Invalid data type for chessboard cell: {type(cell)}, expected str')
    if not isinstance(size, int):
        raise TypeError(f'Invalid data type for chessboard size: {type(cell)}, expected int')

def check_chessboard_size(size: int):
    """Check size of chessboard max value 26,
    if size more than 25 raise Value error"""
    if size >= len(ascii_lowercase):
        raise ValueError(f'Max size ,ust be less than {ken(ascii_lowercase)}')

def make_chessboard(size: int):
    """Make chessboard structure data"""
    letters = ascii_lowercase[:size]
    digits = range(1, size + 1)
    chessboard = {}
    color = 0
    line_start_color = 0


    for letter in letters:
        for digit in digits:
            cell = letter + str(digit)
            color = 1 if line_start_color % 2 == 0 else 0
            chessboard[cell] = color
            line_start_color += 1
        line_start_color = 0 if color else 1
    return chessboard

def check_cell(chessboard: Dict[str, int], cell: str):
    """Check cell of chessboard, if cell not exist raise Value error"""
    if cell not in chessboard:
        raise ValueError(f'Cell not found in chessboard {cell}')

def find_cell_color(chessboard: Dict[str, int], cell:str):
    """Find cell color in chessboard"""
    return 'black' if chessboard[cell] else 'white'

def main(cell: str, size: int = 8):
    """Main controller of module chessboard"""
    check_data_type(cell, size)
    check_chessboard_size(size)

    chessboard = make_chessboard(size)
    check_cell(chessboard, cell)
    cell_color = find_cell_color(chessboard, cell)

    return cell_color


if __name__ == '__main__':
    user_cell = 'b2'
    size = 8
    print(main(user_cell, size))