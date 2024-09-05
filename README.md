```markdown
# Guide to Testing `.py` Files and Good Prompting Practices

## Introduction

This document explains how to test `.py` files and provides examples of good and bad prompting practices for GitHub Copilot.

## How to Test `.py` Files

To test `.py` files, follow these steps:

1. Open a terminal in the directory where the files are located.
2. Run the file you want to test using the command `python filename.py`.

For example, to test `m_p_1.py`, use the following command:

```sh
python m_p_1.py
```

## Good Prompting Practices

### Example of Good Prompting ([`b_p_1.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fandy%2FPYTHON%2FZITON%2FWorkShop%2FCopilotWorkShop%2Fb_p_1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%229d9bd4fb-cf38-453e-9ba4-cecb4cc3c059%22%5D "/home/andy/PYTHON/ZITON/WorkShop/CopilotWorkShop/b_p_1.py"))

Good prompting is clear and specific, providing enough context for GitHub Copilot to understand what is needed.

```python
# b_p_1.py

def count_words(text):
    """
    Counts the number of words in a given text.

    Args:
    text (str): The text to analyze.

    Returns:
    int: The number of words in the text.
    """
    words = text.split()
    return len(words)

# Usage example
text = "Hello, welcome to the GitHub Copilot workshop."
number_of_words = count_words(text)
print(f"Number of words: {number_of_words}")
```

### Example of Bad Prompting ([`m_p_1.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fhome%2Fandy%2FPYTHON%2FZITON%2FWorkShop%2FCopilotWorkShop%2Fm_p_1.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%2C%229d9bd4fb-cf38-453e-9ba4-cecb4cc3c059%22%5D "/home/andy/PYTHON/ZITON/WorkShop/CopilotWorkShop/m_p_1.py"))

Bad prompting is vague and lacks context, which can lead to incorrect or unexpected results.

```python
# m_p_1.py

def count_words(text):
    words = text.split()
    return len(words)

# Usage example
text = "Hello, welcome to the GitHub Copilot workshop."
number_of_words = count_words(text)
print(f"Number of words: {number_of_words}")
```

In the bad prompting example, the lack of documentation and context can make it difficult for GitHub Copilot to provide accurate suggestions.

