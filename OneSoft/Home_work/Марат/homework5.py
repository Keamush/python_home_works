import time

range_begin = int(input('enter range begin number\n'))
range_end = int(input('enter range end number\n'))


# TODO понять рендж из какой длинны нам пришёл
# TODO сгенерировать дикт такой длинны для каждой цифры этой длинны
# TODO использовать обращение к этому словарю вместо возведения в степень

def get_dict_of_numbers(len_range_end):
    init_dict = {}
    for i in range(1, len_range_end + 1):
        sub_dict = {}
        for j in range(10):
            sub_dict[str(j)] = j ** i
        init_dict[i] = sub_dict

    return init_dict


paws_for_different_positions = get_dict_of_numbers(len(str(range_end)))

start = time.time()


def pow_sum_from_num(any_num: int):
    string_num = str(any_num)
    position_counter = 1
    number_sum = 0
    for i in string_num:
        number_sum += paws_for_different_positions[position_counter][i]
        position_counter += 1

    return number_sum


result = []
for num in range(range_begin, range_end + 1):
    if pow_sum_from_num(num) == num:
        result.append(num)

print(result)

end = time.time()
print(end - start)

#
# 6 36
# 7 49
# 8 64
# 9 81
# 16-19
# 26-29

# 1 to 10 000 000 = 13.30752182006836 seconds
#
