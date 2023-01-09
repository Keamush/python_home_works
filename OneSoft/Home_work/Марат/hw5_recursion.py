import time

range_begin = int(input('enter range begin number\n'))
range_end = int(input('enter range end number\n'))

dict_of_paw_values = {
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}

def enrich_dict(string_num: str, current_dict):
    begining_of_string_num = string_num[0:len(string_num) - 1]
    ending_of_string_num = string_num[-1]
    if begining_of_string_num in current_dict.keys():
        sum_of_this_string_num = current_dict[begining_of_string_num] + (int(ending_of_string_num) ** len(string_num))
        current_dict[string_num] = sum_of_this_string_num
        return current_dict
    else:
        return enrich_dict(begining_of_string_num, current_dict)


def calculate_number_recursion(string_num: str, current_dict):
    if len(string_num) > 1:
        beginning_of_string_num = string_num[0:len(string_num) - 1]
        ending_of_string_num = string_num[-1]
        if beginning_of_string_num in current_dict.keys():
            sum_of_this_string_num = current_dict[beginning_of_string_num] + (int(ending_of_string_num) ** len(string_num))
            current_dict[string_num] = sum_of_this_string_num
            return sum_of_this_string_num, current_dict
        else:
            current_dict = enrich_dict(beginning_of_string_num, current_dict)
            return calculate_number_recursion(string_num, current_dict)
            # return calculate_number_recursion(beginning_of_string_num, current_dict)
    else:
        return dict_of_paw_values[string_num], current_dict


start = time.time()
result_answer_list = []
for i in range(range_begin, range_end+1):
    result, dict_of_paw_values = calculate_number_recursion(str(i), dict_of_paw_values)
    if result == i:
        result_answer_list.append(result)

print(result_answer_list)
end = time.time()
print(end - start)