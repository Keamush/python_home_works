import io
import unittest
from unittest.mock import patch


def print_hello():
    print('Hello')


class TestHello(unittest.TestCase):
    def setUp(self) -> None:
        self.func = print_hello

    def test_hello(self):
        with patch('sys.stdout', new=io.StringIO()) as fake_out:
            self.func()
        self.assertEqual(fake_out.getvalue(), 'Hello\n')


if __name__ == '__main__':
    unittest.main()
