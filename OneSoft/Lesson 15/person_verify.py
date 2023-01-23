import re
from typing import NamedTuple, Type


class PersonData(NamedTuple):
    full_name: str
    age: int
    id_card: str
    weight: float


class Person:
    def __init__(self, obj: PersonData, verification: Type['PersonVerifyRus']):
        self.__verification = verification
        self.__verification.verify_all(obj)

        self.__full_name = obj.full_name
        self.__age = obj.age
        self.__id_card = obj.id_card
        self.__weight = obj.weight
        self._protected = 'protect'

    @property
    def full_name(self):
        return self.__full_name

    @full_name.setter
    def full_name(self, full_name: str):
        self.__verification.verify_full_name(full_name)
        self.__full_name = full_name

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self, age: int):
        self.__verification.verify_age(age)
        self.__age = age

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight: float):
        self.__verification.verify_weight(weight)
        self.__weight = weight

    @property
    def id_card(self):
        return self.__id_card

    @id_card.setter
    def id_card(self, id_card: str):
        self.__verification.verify_id_card(id_card)
        self.__id_card = id_card


class PersonVerifyRus:
    _RUS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    _LETTERS = _RUS + _RUS.lower()
    _AGE_RANGE = range(16, 66)
    _WEIGHT_RANGE = range(50, 110)
    _CARD_FORMAT = re.compile(r'\w{2}-\d{6}$')

    @classmethod
    def verify_all(cls, obj: PersonData):
        cls.verify_full_name(obj.full_name)
        cls.verify_age(obj.age)
        cls.verify_weight(obj.weight)
        cls.verify_id_card(obj.id_card)

    @classmethod
    def verify_full_name(cls, full_name: str):
        if not isinstance(full_name, str):
            raise TypeError('Full name must be a sting')

        full_name = full_name.split(' ')

        if not [value for value in full_name if value.strip()]:
            raise ValueError('Full name must contains at least one character')

        if len(full_name) != 3:
            raise ValueError('Invalid full name format')

        for name in full_name:
            if len(name.strip(cls._LETTERS)):
                raise ValueError(f'Full name must contains only {cls._LETTERS}')

    @classmethod
    def verify_age(cls, age: int):
        if not isinstance(age, int):
            raise TypeError('Age must be an integer')

        if age not in cls._AGE_RANGE:
            raise ValueError(f'Age must be between {cls._AGE_RANGE[0]} and {cls._AGE_RANGE[-1]}')

    @classmethod
    def verify_weight(cls, weight: float):
        if not isinstance(weight, float):
            raise TypeError('Weight must be a float')

        if int(weight) not in cls._WEIGHT_RANGE:
            raise ValueError(f'Weight must be between {cls._WEIGHT_RANGE[0]} and {cls._WEIGHT_RANGE[-1]}')

    @classmethod
    def verify_id_card(cls, id_card: str):
        if not isinstance(id_card, str):
            raise TypeError('Id card must be a str')

        if cls._CARD_FORMAT.match(id_card) is None:
            raise ValueError('Invalid id card format XX-XXXXXX')


# class PersonVerifyRusExtended(PersonVerifyRus):
#     @classmethod
#     def verify_manager(cls, manager):
#         cls._verify_all()

if __name__ == '__main__':
    person_data = PersonData('Иванов Иван Иванович', 36, 'ВР-515423', 101.3)
    person_rus = Person(person_data, PersonVerifyRus)
    # print(dir(person_rus))
    print(person_rus.full_name)
    person_rus.full_name = 'Петров Иван Иванович'
    print(person_rus.full_name)
