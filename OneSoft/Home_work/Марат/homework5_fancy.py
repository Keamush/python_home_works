import time

range_begin = int(input('enter range begin number\n'))
range_end = int(input('enter range end number\n'))


def get_dict_of_numbers(len_range_end):
    init_dict = {}
    for i in range(1, len_range_end + 1):
        sub_dict = {}
        for j in range(10):
            sub_dict[str(j)] = j ** i
        init_dict[i] = sub_dict

    return init_dict


def calculate_paw_sum(string_num: str, current_dict):
    begining_of_string_num = string_num[0:len(string_num)-1]
    ending_of_string_num = string_num[-1]
    sum_of_this_string_num = current_dict[begining_of_string_num] + (int(ending_of_string_num) ** len(string_num))
    current_dict[string_num] = sum_of_this_string_num
    return sum_of_this_string_num, current_dict


def pow_sum_from_num(any_num: int):
    string_num = str(any_num)
    position_counter = 1
    number_sum = 0
    for i in string_num:
        number_sum += paws_for_different_positions[position_counter][i]
        position_counter += 1

    return number_sum

if __name__ == '__main__':
    paws_for_different_positions = get_dict_of_numbers(len(str(range_end)))

    start = time.time()
    result = []
    for num in range(range_begin, range_end + 1):
        str_num =
        if pow_sum_from_num(num) == num:
            result.append(num)

    a = find_cell_color()

print(result)

end = time.time()
print(end - start)
