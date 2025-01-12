# Challenge: Palindrome Detector

## Description

The "Palindrome Detector" challenge involves determining if a given string
or bytes is a palindrome.
A palindrome is a word, phrase, or sequence that reads the same backward as
forward, ignoring spaces, punctuation, and case.

Write a function that takes a string or bytes as input and returns `True` if
it is a palindrome, and `False` otherwise.

For example:

- The string `A man, a plan, a canal, Panama` is a palindrome.
- The string `hello` is not a palindrome.
- The bytes `b"racecar"` is a palindrome.
- The bytes `b"hello"` is not a palindrome.

## Example

```python
is_palindrome("A man, a plan, a canal, Panama")
# Output: True (ignoring spaces, punctuation, and case)

is_palindrome("hello")
# Output: False (not a palindrome)

is_palindrome(b"racecar")
# Output: True (ignoring spaces, punctuation, and case)

is_palindrome(b"hello")
# Output: False (not a palindrome)
