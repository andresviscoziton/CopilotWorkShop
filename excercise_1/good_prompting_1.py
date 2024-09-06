# Create a Python function called `calculate_rectangle_area` that calculates the area of a rectangle.
# Conser ValueError and TypeError exceptions.
# The function should take two parameters, `base` and `height`, both of type float, and should return the area as a float.

# Copilot as "Tester" should provide test cases for this function.
def calculate_rectangle_area(base: float, height: float) -> float:
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("Both base and height must be numbers.")
    if base <= 0 or height <= 0:
        raise ValueError("Both base and height must be positive numbers.")
    return base * height

# Test cases
def test_calculate_rectangle_area():
    try:
        assert calculate_rectangle_area(5.0, 10.0) == 50.0
        assert calculate_rectangle_area(3.5, 2.0) == 7.0
        assert calculate_rectangle_area(0, 10.0) == 0.0  # This should raise a ValueError
    except ValueError:
        print("ValueError caught as expected for zero input.")
    except TypeError:
        print("TypeError caught as expected for non-numeric input.")
    else:
        print("All test cases passed.")

test_calculate_rectangle_area()