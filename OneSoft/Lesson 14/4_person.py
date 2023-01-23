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

        self._check_all_data()

    def _check_full_name(self):
        full_name_list = self.full_name.split(' ')
        if len(full_name_list) == 3:
            for element in full_name_list:
                for letter in element:
                    if letter not in self.LETTERS:
                        raise ValueError('Use ONLY letters')
        else:
            raise ValueError('Check your name again.')

    def _check_weight(self):
        if self.weight <= min(self.WEIGHT_RANGE):
            raise ValueError('Too SKINNY!')
        elif self.weight > max(self.WEIGHT_RANGE):
            raise ValueError('Too FAT!')

    def _check_age(self):
        if self.age <= min(self.AGE_RANGE):
            raise ValueError('Too young!')
        elif self.age > max(self.AGE_RANGE):
            raise ValueError('Too old!')

    # def _check_id_card(self):
    #     id_card_list = self.id_card.split('-')
    #     if len(id_card_list) == 2:
    #         for element in id_card_list:
    #             for letter in element:
    #                 if letter != re.match():
    #                     raise ValueError('Invalid data')
    #     else:
    #         raise ValueError('Check your id card number again.')

    def _check_all_data(self):
        self._check_full_name()
        self._check_weight()
        self._check_age()
        # self._check_id_card()



if __name__ == '__main__':
    person_data = PersonData('Иванов Иван Иванович', 36, 'ВР-515423', 101.3)
    person = Person(person_data)

