import unittest
from good_prompting_3 import DateHelper

class TestDateHelper(unittest.TestCase):
    def setUp(self):
        self.date_helper = DateHelper()

    def test_valid_date(self):
        self.assertEqual(self.date_helper.get_weekday_name("15/10/2023"), "Sunday")

    def test_invalid_date_format(self):
        self.assertEqual(self.date_helper.get_weekday_name("2023/10/15"), "Invalid date format. Please use DD/MM/YYYY.")
        self.assertEqual(self.date_helper.get_weekday_name("15-10-2023"), "Invalid date format. Please use DD/MM/YYYY.")

    def test_invalid_date_string(self):
        self.assertEqual(self.date_helper.get_weekday_name("invalid_date"), "Invalid date format. Please use DD/MM/YYYY.")

    def test_non_string_input(self):
        self.assertEqual(self.date_helper.get_weekday_name(15102023), "Invalid input type. Please provide a date string in DD/MM/YYYY format.")
        self.assertEqual(self.date_helper.get_weekday_name(None), "Invalid input type. Please provide a date string in DD/MM/YYYY format.")
        self.assertEqual(self.date_helper.get_weekday_name([]), "Invalid input type. Please provide a date string in DD/MM/YYYY format.")

if __name__ == "__main__":
    unittest.main()