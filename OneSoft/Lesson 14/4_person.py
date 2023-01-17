import re
from typing import NamedTuple


class PersonData(NamedTuple):
    full_name: str
    age: int
    id_card: str
    weight: float


class Person:
    RUS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    LETTERS = RUS + RUS.lower()
    AGE_RANGE = range(16, 66)
    WEIGHT_RANGE = range(50, 110)
    CARD_FORMAT = re.compile(r'\w{2}-\d{6}')

    def __init__(self, obj: PersonData):
        self.full_name = obj.full_name
        self.age = obj.age
        self.id_card = obj.id_card
        self.weight = obj.weight


if __name__ == '__main__':
    person_data = PersonData('Иванов Иван Иванович', 36, 'ВР-515423', 101.3)
    person = Person(person_data)
