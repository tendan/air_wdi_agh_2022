from unittest import TestCase
from src.python.cyfry_slownie import main, slownie


class TestCyfrySlownie(TestCase):

    def test_main(self):
        pass

    params = [
        ("1410", "jeden cztery jeden zero"),
        ("54321", "pięć cztery trzy dwa jeden"),
        ("83", "osiem trzy"),
        ("476", "cztery siedem sześć")
    ]

    def test_slownie(self):
        for number, result in self.params:
            with self.subTest(f"number = {number}"):
                actual = slownie(number).rstrip()
                self.assertEqual(result, actual, f"Should return {result} as a string")
