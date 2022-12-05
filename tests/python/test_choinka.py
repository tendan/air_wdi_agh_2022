import io
import sys
import mock
from src.python.choinka import main
from unittest import TestCase


class TestChoinka(TestCase):

    def test_main_for_3(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        candidate = "  *\n" + \
                    " ***\n" + \
                    "*****\n"

        with mock.patch('builtins.input', return_value=3):
            main()

        actual = captured_output.getvalue()
        # sys.stdout = sys.__stdout__
        self.assertEqual(candidate, actual, "Should print 3-row christmas tree")

    def test_main_for_4(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        candidate = "   *\n" + \
                    "  ***\n" + \
                    " *****\n" + \
                    "*******\n"

        with mock.patch('builtins.input', return_value=4):
            main()

        actual = captured_output.getvalue()
        # sys.stdout = sys.__stdout__
        self.assertEqual(candidate, actual, "Should print 4-row christmas tree")

    def test_main_for_5(self):
        captured_output = io.StringIO()
        sys.stdout = captured_output
        candidate = "    *\n" + \
                    "   ***\n" + \
                    "  *****\n" + \
                    " *******\n" + \
                    "*********\n"
        with mock.patch('builtins.input', return_value=5):
            main()

        actual = captured_output.getvalue()
        # sys.stdout = sys.__stdout__
        self.assertEqual(candidate, actual, "Should print 5-row christmas tree")
