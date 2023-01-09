def pow_digit(number: int):
    pow_digits = []
    for pow, digit in enumerate(str(number), 1):
        temp = int(digit) ** pow
        pow_digits.append(temp)
    return  sum(pow_digits)

def sum_digit_pow(start: int, stop: int):
    special_numbers = []
    for number in range(start, stop + 1):
        if number == pow_digit(number):
            special_numbers.append(number)
    return special_numbers

if __name__ == '__main__':
    print(sum_digit_pow(1, 200))