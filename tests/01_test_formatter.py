import unittest
from src.util.formatter import InputFormatter
from src.util.exceptions import InputError


class TestInputFormatter(unittest.TestCase):

    def test1_extract_values_with_valid_pair(self):
        input = 'Year 2007 ID 6735'
        result = InputFormatter._extract_values_from_pair(input)
        self.assertEqual(result, {'id': '6735', 'year': '2007'})

    def test2_extract_values_with_in_valid_pair(self):
        input = 'Year 2007  6735'

        with self.assertRaises(InputError):
            InputFormatter._extract_values_from_pair(input)

    def test3_extract_values_with_in_valid_pair(self):
        input = ''

        with self.assertRaises(InputError):
            InputFormatter._extract_values_from_pair(input)

    def test4_extract_values_with_in_valid_pair(self):
        input = 'ID 6735 Year 2007'

        with self.assertRaises(InputError):
            InputFormatter._extract_values_from_pair(input)

    def test5_extract_values_with_valid_input(self):
        input = 'Year 2007 ID 67352, Year 2011 ID 87964'
        result = InputFormatter.extract_values(input)
        self.assertEqual(result, [{'id': '67352', 'year': '2007'}, {
                         'id': '87964', 'year': '2011'}])

    def test6_extract_values_with_invalid_input(self):
        input = 'Year 2007 ID 67352 Year 2011 ID 87964'
        
        with self.assertRaises(InputError):
            InputFormatter._extract_values_from_pair(input)

    def test7_extract_values_with_invalid_input(self):
        input = 'Year 2007, ID 67352, Year 2011, ID 87964'
        
        with self.assertRaises(InputError):
            InputFormatter._extract_values_from_pair(input)

    def test8_extract_values_with_invalid_input(self):
        input = ' '
        
        with self.assertRaises(InputError):
            InputFormatter._extract_values_from_pair(input)
