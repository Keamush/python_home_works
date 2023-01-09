name = 'bob'

counter = 0

# while counter < len(name):
#     name[0]
#     name.__getitem__(0)
#     print(name.__getitem__(counter))
#     counter += 1
#
#
# for letter in name:
#     print(letter)

# print(name + '!')
# print(name.__add__('!'))

# for letter in name.__iter__():
#     print(letter)

name_iter = iter(name)
# print(name_iter.__next__())
# print(name_iter.__next__())
# print(name_iter.__next__())
# print(name_iter.__next__())

while True:
    try:
        print(next(name_iter))
    except StopIteration:
        break
