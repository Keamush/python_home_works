import random


def generate_random_numbers(size):
    numbers = [random.randint(1, 2**16) for _ in range(size)]
    return numbers

print(generate_random_numbers(1000 * 10))
# print(generate_random_numbers(10**10))

# for _ in range(size):
#     random_number = random.randint(1, 2**16)
#     numbers.append(random_number)


size = 100
numbers = []
for number_top in range(size):
    for number_bottom in range(size):
        numbers.append(number_top + number_bottom)
print(len(numbers))

numbers.pop()