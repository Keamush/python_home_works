import random

random_numbers = [random.randint(1, 100) for _ in range(10)]
# print(random_numbers)

# print(random.random())

# print(random.choice(list(range(1,100))))

names = ['bob', 'sarah', 'james']
# random_name = [random.choice(names)]
# print(random_name)

numbers = list(range(1, 1000))
random.shuffle(numbers)
print(numbers)
