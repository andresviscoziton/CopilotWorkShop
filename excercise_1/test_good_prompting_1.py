import unittest
from good_prompting_1 import calculate_rectangle_area

class TestCalculateRectangleArea(unittest.TestCase):
    
    def test_valid_area(self):
        self.assertAlmostEqual(calculate_rectangle_area(5.0, 10.0), 50.0)
        self.assertAlmostEqual(calculate_rectangle_area(3.5, 2.0), 7.0)
    
    def test_zero_base(self):
        with self.assertRaises(ValueError):
            calculate_rectangle_area(0.0, 5.0)
    
    def test_zero_height(self):
        with self.assertRaises(ValueError):
            calculate_rectangle_area(5.0, 0.0)
    
    def test_negative_base(self):
        with self.assertRaises(ValueError):
            calculate_rectangle_area(-5.0, 10.0)
    
    def test_negative_height(self):
        with self.assertRaises(ValueError):
            calculate_rectangle_area(5.0, -10.0)
    
    def test_non_float_base(self):

        with self.assertRaises(TypeError):
            calculate_rectangle_area("5", 10.0)
    
    def test_non_float_height(self):
        with self.assertRaises(TypeError):
            calculate_rectangle_area(5.0, "10")
    
    def test_non_float_base_and_height(self):
        with self.assertRaises(TypeError):
            calculate_rectangle_area("5", "10")

if __name__ == '__main__':
    unittest.main()