import unittest
from format_price import format_price

class TestFormatPrice(unittest.TestCase):

    def test_format_price(self):
        self.assertEqual('3 245',str(format_price(3245.00000)))
        self.assertEqual('1 111', str(format_price('1111,0000')))
        self.assertEqual(0, format_price('asd'))
        self.assertEqual('1 325.01', str(format_price(1325.0112312)))
        