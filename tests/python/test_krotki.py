from unittest import TestCase

from src.python.krotki import suma_krotek


class TestKrotki(TestCase):

    number_params = [
        ([(1, 2), (3, 4), (5, 6), (7, 8)], [3, 7, 11, 15]),
        ([(1, 1), (2, 3), (5, 8)], [2, 5, 13])
    ]

    char_params = [
        ([('a', 'b'), ('c', 'd'), ('d', 'e')], ["ab", "cd", "de"]),
        ([('a', 'b'), ('a', 'c'), ('b', 'c')], ["ab", "ac", "bc"]),
    ]

    string_params = [
        ([("ab", "cd"), ("de", "fg"), ("gh", "ij")], ["abcd", "defg", "ghij"]),
    ]

    def sub_test_for_params(self, params):
        for candidate, expected in params:
            actual = suma_krotek(candidate)
            self.assertListEqual(actual, expected, f"Should be {expected}")

    def test_suma_krotek_numbers(self):
        self.sub_test_for_params(self.number_params)

    def test_suma_krotek_chars(self):
        self.sub_test_for_params(self.char_params)

    def test_suma_krotek_strings(self):
        self.sub_test_for_params(self.string_params)
