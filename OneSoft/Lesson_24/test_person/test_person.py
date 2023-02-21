import unittest
from person.person_verify import PersonData, Person, PersonVerifyRus


class TestPersonClass(unittest.TestCase):
    def setUp(self) -> None:
        self.person_dto = PersonData('Иванов Иван Иванович', 36, 'ВР-515423', 101.3)
        self.verifier_rus = PersonVerifyRus
        self.person_rus = Person(self.person_dto, self.verifier_rus)

    def tearDown(self) -> None:
        del self.person_rus

    def test_normal_data(self):
        self.assertEqual(self.person_dto.full_name, self.person_rus.full_name)
        self.assertEqual(self.person_dto.age, self.person_rus.age)
        self.assertEqual(self.person_dto.id_card, self.person_rus.id_card)
        self.assertEqual(self.person_dto.weight, self.person_rus.weight)

    def test_set_data(self):
        full_name = 'Петров Петр Петрович'
        age = 41
        id_card = 'ФР-215423'
        weight = 91.3

        self.person_rus.full_name = full_name
        self.person_rus.age = age
        self.person_rus.id_card = id_card
        self.person_rus.weight = weight

        self.assertEqual(full_name, self.person_rus.full_name)
        self.assertEqual(age, self.person_rus.age)
        self.assertEqual(id_card, self.person_rus.id_card)
        self.assertEqual(weight, self.person_rus.weight)

    def test_full_name_with_wrong_data(self):
        with self.assertRaises(TypeError) as context:
            self.person_rus.full_name = None
        self.assertTrue('Full name must be a sting' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.person_rus.full_name = '    '
        self.assertTrue('Full name must contains at least one character' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.person_rus.full_name = 'Иван Иванов'
        self.assertTrue('Invalid full name format' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.person_rus.full_name = 'Иван Иванович Ивановqwe'
        self.assertTrue('Full name must contains only' in str(context.exception))

    def test_age_with_wrong_data(self):
        with self.assertRaises(TypeError) as context:
            self.person_rus.age = 77.3
        self.assertTrue('Age must be an integer' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.person_rus.age = 10
        self.assertTrue('Age must be between' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.person_rus.age = 200
        self.assertTrue('Age must be between' in str(context.exception))

    def test_weight_with_wrong_data(self):
        with self.assertRaises(TypeError) as context:
            self.person_rus.weight = 77
        self.assertTrue('Weight must be a float' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.person_rus.weight = 10.0
        self.assertTrue('Weight must be between' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.person_rus.weight = 200.0
        self.assertTrue('Weight must be between' in str(context.exception))

    def test_id_card_with_wrong_data(self):
        with self.assertRaises(TypeError) as context:
            self.person_rus.id_card = None
        self.assertTrue('Id card must be a str' in str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.person_rus.id_card = 'id123456'
        self.assertTrue('Invalid id card format XX-XXXXXX' in str(context.exception))