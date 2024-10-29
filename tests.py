import unittest
import regular_expressions

# Датасет для тестов
test_cases = [
    ("ru 123456", True), ("ru 654321", True),
    ("ru 12345", False), ("ru123456", False),
    ("usa 12345", True), ("usa 54321", True),
    ("usa 1234", False), ("usa12345", False),
    ("uk W1A 1AA", True), ("uk EC1A 1BB", True),
    ("uk 1234", False), ("uk W1A1AA", False),
    ("french 75001", True), ("french 13001", True),
    ("french 7500", False), ("french75001", False),
    ("de 12345", False), ("es 08001", False),
    ("", False)
]

# Класс для тестирования функции
class TestIsValidPostcode(unittest.TestCase):

    def test_postcodes(self):
        for postcode, expected in test_cases:
            with self.subTest(postcode=postcode):
                self.assertEqual(regular_expressions.is_valid_postcode(postcode), expected)


if __name__ == '__main__':
    unittest.main()
