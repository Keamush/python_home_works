class Car:
    car_count = 0

    @classmethod
    def get_car_count(cls):
        return cls.car_count

    def __init__(self, name, make, model, price):
        self.name = name
        self.make = make
        self.model = model
        self.price = price
        Car.car_count += 1

    def start_engine(self):
        return f'Start engine {self.name}'

    def stop_engine(self):
        return f'Stop engine {self.name}'


car_mercedes = Car('c200', 'mercedes', 2012, 10000)
car_audi = Car('a4', 'audi', 2015, 12000)

# print(car_mercedes.make)
# print(car_audi.make)
# print(Car.get_car_count())
print(car_mercedes.start_engine())
print(car_audi.start_engine())
print(car_audi.get_car_count())
print(car_audi.__class__)
