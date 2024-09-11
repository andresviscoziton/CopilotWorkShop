Here are 3 examples of **poor quality prompting** and 3 examples of **perfect quality prompting** for GitHub Copilot.

### Examples of **Poor Quality Prompting**:
1. **Vague Prompt:**
   ```python
   # Function to calculate
   ```
   - **Issue:** Provides insufficient information about what needs to be calculated.

2. **Generic Prompt:**
   ```python
   # Write Python code
   ```
   - **Issue:** Lacks context and specificity, making it difficult for Copilot to understand what kind of code is needed.

3. **Ambiguous Prompt:**
   ```python
   # Do something with a list
   ```
   - **Issue:** Does not specify what needs to be done with the list. It could mean anything, like sorting, filtering, modifying, etc.

### Examples of **Perfect Quality Prompting**:
1. **Specific Function Prompt:**
   ```python
   # Define a function `calculate_factorial` that takes an integer n as input and returns its factorial.
   # Use recursion for the implementation and handle cases where n is less than 0 by raising a ValueError.
   def calculate_factorial(n):
   ```
   - **Why it's good:** Clearly describes the purpose, parameters, the method to use (recursion), and exceptions to handle.

2. **Descriptive Data Manipulation Prompt:**
   ```python
   # Given a list of integers, write a function `find_top_three_largest` that returns the three largest unique numbers in descending order.
   def find_top_three_largest(numbers):
   ```
   - **Why it's good:** Provides a detailed and specific description of the input, output, and the order of the expected results.

3. **Solution-Oriented Prompt with Clear Rules:**
   ```python
   # Write a Python function `is_valid_email` that takes a string as input and returns True if it is a valid email address.
   # An email is considered valid if it contains exactly one "@" symbol, has a non-empty local part, a non-empty domain part,
   # and the domain contains at least one "." after the "@".
   def is_valid_email(email):
   ```
   - **Why it's good:** Clearly defines the purpose, validation criteria, and the type of input and output expected.

### **Summary:**
- **Poor quality prompts** are vague, ambiguous, or too generic.
- **Perfect quality prompts** are clear, specific, and provide enough context for Copilot to understand exactly what is required.