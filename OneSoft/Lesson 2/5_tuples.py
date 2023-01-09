numbers_immutable = (0, 1, 2, 3, 4, 5, 6)

new = numbers_immutable + (1, 2)
# print(new)
# del new [0]

# print(id(numbers_immutable))
# print(id(numbers_immutable+ (1, 2)))

numbers_immutable = (0, 1, 2, 3, 4, [1, 2])
print(numbers_immutable)
numbers_immutable[-1].append('new')
print(numbers_immutable)

del numbers_immutable[-1][-1]
print(numbers_immutable)