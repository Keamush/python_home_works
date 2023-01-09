# def multiplay(number1):
#     def inner(number2):
#         return number1 * number2
#     return inner
#
# multiplay_number_ten = multiplay(10)
# print(multiplay_number_ten(2))
# print(multiplay_number_ten(5))
#
# multiplay_number_eleven = multiplay(11)
# print(multiplay_number_eleven(2))
# print(multiplay_number_eleven(5))

def func_as_object(number_one, number_two):
    def add():
        return number_one + number_two
    def sub():
        return number_one - number_two
    def mult():
        return number_one * number_two
    def div():
        return number_one / number_two

    func_as_object.add = add
    func_as_object.sub = sub
    func_as_object.mult = mult
    func_as_object.div = div
    return func_as_object

numbers_five_seven = func_as_object(5, 7)
print(numbers_five_seven.add())
print(numbers_five_seven.sub())
print(numbers_five_seven.mult())
print(numbers_five_seven.div())