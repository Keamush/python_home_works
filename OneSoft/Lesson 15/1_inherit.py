import turtle


class Vehicle(object):
    def vehicle_method(self):
        print('vehicle_method')


class Car(Vehicle):
    def method(self):
        print('car_method')


class Bicycle(Vehicle):
    def method(self):
        print('bicycle_method')


class HybridCarBicycle(Bicycle, Car):
    def __init__(self, car, bicycle):
        self.car = car()
        self.bicycle = bicycle()

    def hybrid_car_bicycle_method(self):
        print('hybrid_car_bicycle_method')


vehicle = Vehicle()
car = Car()
bicycle = Bicycle()
hybrid = HybridCarBicycle(Car, Bicycle)

hybrid.method()

# vehicle.vehicle_method()

# car.vehicle_method()
# car.car_method()
#
# bicycle.vehicle_method()
# bicycle.bicycle_method()

print(HybridCarBicycle.__mro__)
