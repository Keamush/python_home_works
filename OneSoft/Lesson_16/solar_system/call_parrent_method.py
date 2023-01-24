from abc import ABCMeta, abstractmethod


class Vehicle(metaclass=ABCMeta):
    wheels = 4

    def move(self):
        print('Move vehicle')

    @abstractmethod
    def fill_tank(self):
        pass


class Car(Vehicle):
    def move(self):
        super().move()
        print('Move car')

    def fill_tank(self):
        print('Fill car tank')


car = Car()
car.move()
print(Car.__mro__)
