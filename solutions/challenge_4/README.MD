# **Challenge: Use of Operators**

## **Instructions:**

1. Create a loop to go through each element in the list called `lista_de_elementos`.
2. Check the type of each element:
   - If the element is a number (integer or float), check if it is below the
     defined threshold (`umbral`).
     - Print **"Approved"** if the value is below the threshold.
     - Print **"Rejected"** otherwise.
   - If the element is a string (`str`), skip the comparison with the threshold.
3. Implement two counters:
   - One to count the number of approved elements.
   - One to count the number of rejected elements.
4. Count the elements that are of type string (`str`) and print the total
   at the end of the loop.
5. Print the total of approved and rejected elements at the end of the code.

## **Initial Parameters:**

```python
threshold = -10
elements_list = [
    10, 3.14, "7", -5, "2.718", 42, "Python", -8.9, "Hello", 100.5,
    "World", -15, "GPT-3", 5.5, "AI", -20, "2023", 123, "OpenAI",
    -2.5, "Example"
]

# Development of the main code loop.
# In this space, you must write the code following the
# instructions from the previous cell.



print("Total approved: ", approved)
print("Total rejected: ", rejected)
print("Total strings: ", string_count)

```

### **Expected Output:**

At the end of the loop, the program should print:

- The total number of approved elements.
- The total number of rejected elements.
- The total number of strings (`str`).

### Helpful Links

1. **`for` loop in Python**
   Documentación oficial sobre cómo usar los bucles `for` en Python:
   [for statement - Python Docs](https://docs.python.org/3/reference/simple_stmts.html#for)

2. **`if` statement in Python**
   Documentación oficial sobre cómo usar las sentencias `if` en Python:
   [if statement - Python Docs](https://docs.python.org/3/reference/compound_stmts.html#if)

[Github issue](https://github.com/MIT-Emerging-Talent/ET6-foundations-group-04/issues/04)
