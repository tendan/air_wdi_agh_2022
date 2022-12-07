from unittest import TestCase

import mock

from src.python.najmniejsza import main


class TestNajmniejsza(TestCase):
    def test_main(self):
        with mock.patch('builtins.input', side_effect=''):
            pass
        main()
