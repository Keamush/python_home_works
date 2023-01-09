from typing import List

def read_data_from_file(filename: str):
    result = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line:
                result.append(line)
    return result


def write_data_to_file(filename: str, data: List[str]):
    with open(filename, 'w') as file:
        for count, line in enumerate(data, 1):
            line = f'{count}. {line}\n'
            file.write(line)


def main(filename: str):
    read_data = read_data_from_file(filename)
    write_data_to_file(filename, read_data)
    return f'Write {filename}'


if __name__ == '__main__':
    print(main('example.txt'))