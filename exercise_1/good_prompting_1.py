import unittest

# Create a Python function called `calculate_rectangle_area` that calculates the area of a rectangle.
def calculate_rectangle_area(base: float, height: float) -> float:
    """
    Calculate the area of a rectangle.

    This function takes two parameters, `base` and `height`, both of type float, and returns the area as a float.excercise_1/good_prompting_2.py
    It also considers ValueError and TypeError exceptions.

    Parameters:
    base (float): The base of the rectangle.
    height (float): The height of the rectangle.

    Returns:
    float: The area of the rectangle.

    Raises:
    ValueError: If either `base` or `height` is less than or equal to zero.
    TypeError: If either `base` or `height` is not a float.
    """
    if base <= 0 or height <= 0:
        raise ValueError("The base and height of a rectangle must be greater than zero.")
    elif not isinstance(base, float) or not isinstance(height, float):
        raise TypeError("The base and height of a rectangle must be of type float.")
    return base * height


