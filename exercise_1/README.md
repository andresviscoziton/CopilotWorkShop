### **Example 1: Good Prompting Python function creation**

#### **Instruction for GitHub Copilot**
```python
# Create a Python function called `is_palindrome` that determines if a string is a palindrome.
# Input: a string `text`
# Output: True if `text` is a palindrome, False if it is not.
# The function should ignore spaces and case differences.

def is_palindrome(text):
    pass
```

### **Explanation**
- **Specific Prompt:** The prompt clearly specifies the function name (`is_palindrome`), the input (a string called `text`), and the expected output (a boolean). Additionally, it provides details on how to handle spaces and case differences, guiding Copilot to generate a more precise and correct function.

### **Example 2: Pair Programming using Copilot as "Tester" and "Navigator"**

#### **Instruction for Pair Programming**

In this scenario, the human acts as the "Driver" and GitHub Copilot as the "Tester" and "Navigator".

```python
# Create a Python function called `calculate_rectangle_area` that calculates the area of a rectangle.
# The function should take two parameters, `base` and `height`, both of type float, and should return the area as a float.
# Copilot as "Tester" should provide test cases for this function.

def calculate_rectangle_area(base, height):
    # Your code here
    pass

# Copilot as "Tester", provide test cases for this function:
# - Base: 5.0, Height: 3.0, Expected result: 15.0
# - Base: 0, Height: 10.0, Expected result: 0.0
# - Base: -1, Height: 4.0, Expected result: ValueError
# - Base: 2.5, Height: 4.2, Expected result: 10.5

# Test cases:
def test_calculate_rectangle_area():
    assert calculate_rectangle_area(5.0, 3.0) == 15.0
    assert calculate_rectangle_area(0, 10.0) == 0.0
    try:
        calculate_rectangle_area(-1, 4.0)
    except ValueError:
        pass  # Test passed, ValueError expected
    assert calculate_rectangle_area(2.5, 4.2) == 10.5

test_calculate_rectangle_area()
```

### **Explanation**
- **Copilot as "Tester":** The instruction includes specific test cases that Copilot should suggest. The human implements the function, while Copilot generates the test cases. Then, the human can adjust the function implementation based on the test results provided by Copilot.
- **Copilot as "Navigator":** Additionally, Copilot can suggest improvements or point out possible errors in the function logic, helping the human "Driver" refine their code.

### **Example 3: Copilot as "Navigator" Assisting with SQL Queries**

#### **Instruction for GitHub Copilot in the Role of "Navigator"**

In this example, the human acts as the "Driver", writing an SQL query, and GitHub Copilot suggests optimizations or validations.

```sql
-- As a human Driver, I am writing an SQL query to get the list of employees who earn more than 50,000 per year.
-- I need to ensure that the query is efficient and considers indexes and best practices.

SELECT * FROM employees WHERE annual_salary > 50000;

-- Copilot as "Navigator", provide recommendations to improve the efficiency of the query:
-- 1. Select only the necessary columns instead of using '*'.
-- 2. Ensure there is an index on the 'annual_salary' column to improve performance.
-- 3. Use aliases to improve the readability of the query.

-- Example of improvement suggested by Copilot:
SELECT first_name, last_name, annual_salary FROM employees WHERE annual_salary > 50000;
```

### **Explanation**
- **Copilot as "Navigator":** Suggests optimizations and best practices to improve the efficiency of the SQL query written by the human "Driver", providing specific examples and highlighting important aspects, such as the use of indexes and selecting necessary columns.

---