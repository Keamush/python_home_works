class Car(object):
    name = 'c200'
    make = 'mercedes'
    model = 2012
    price = 10000

    def start_engine(self):
        print(f'Start engine {self.name}')

    def stop_engine(self):
        print(f'Stop engine {self.name}')

    def __add__(self, other):
        return self.price + other.price

    def __eq__(self, other):
        return self.price == other.price

    def __str__(self):
        return f'Make by {self.make}, name {self.name}'

    def __len__(self):
        return 2023 - self.model


car_a = Car()
car_b = Car()
car_b.price = 15000


# print(dir(Car))

# print(car_a + car_b)
# print(car_a.__add__(car_b))
#
# print(car_a == car_b)
# print(car_a.__eq__(car_b))
# print(car_b.__eq__(car_a))
#
# print(Car.__eq__(car_a, car_b))

# print(id(car_a), id(car_b))
# print(car.name)
# print(Car.name)

# car_a.start_engine()
# car_b.stop_engine()
# Car.start_engine(car)
print(car_a)
print(len(car_b))
if __name__ == '__main__':
    pass
