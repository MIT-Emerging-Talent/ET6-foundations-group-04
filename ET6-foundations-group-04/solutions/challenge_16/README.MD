# **Challenge: Hide a Credit Card Number**
<!-- markdownlint-disable MD036 -->
**Description**
<!-- markdownlint-disable MD013 -->
The "Hide a Credit Card Number" challenge involves writing a function to mask all but the last four digits of a credit card number. This is useful for displaying sensitive information in a secure manner. The masked digits should be replaced with the `*` character.

Write a function that takes a credit card number as a string and returns the masked version of the number, with only the last four digits visible.

**For example:**
<!-- markdownlint-disable MD040 -->
```
Input: '1234567812345678'
Output: '************5678'
```

**Requirements:**

The input will always be a valid credit card number as a string.
The function should preserve the last four digits.
It should handle inputs of varying lengths (e.g., short card numbers).

**Example**

```
hide_credit_card('1234567812345678')
# Output: '************5678'

hide_credit_card('9876543210987654')
# Output: '************7654'

hide_credit_card('1234')
# Output: '1234' (no masking needed if the number has only 4 or fewer digits)
```

**Testing**

Develop unit tests to validate the function's correctness. Include cases for:

- Regular 16-digit credit card numbers.
- Short numbers (e.g., fewer than 8 digits).
- Edge case: Exactly 4 digits (no masking needed).

**Helpful Links**

- [String Slicing in Python](https://www.geeksforgeeks.org/string-slicing-in-python/)
- [GeeksforGeeks: Python String Methods](https://www.geeksforgeeks.org/python-string-methods/)
