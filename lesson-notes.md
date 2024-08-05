# Lesson Notes
## Checking for Membership in Python Lists

### Directions
- Read these notes and check out the related resources before you start writing any code for this lesson


### Related Resources
- [Python Operators](https://www.w3schools.com/python/python_operators.asp)
- [Markdown Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)


### Notes

- Essentially, an **operator** is a symbol you can use to modify/change a variable or its value in some way
- For example, the assignment operator (=) allows you to *assign* a value to a Python variable
  - Example: `age = 21` (You're storing or assigning the numeric value (number) 21 to a variable named `age`)
  - EXample: `hair_color = 'brown'` (You're assigning the value 'brown' to the variable named `hair_color`)
- Python (and other programming languages) offer programmers different families of operators, including:
  - arithmetic operators (for doing math)
  - assignment operators
  - comparison operators
  - logical operators
  - membership operators
    - The **in** operator is an example of a membership operator
    - It is often used to check whether a specific item/element is contained in a Python list
    - In other words, **is the item/element contained in the list or not?**
- You can -- and often will -- use various operators from different families of operators in your code
- See the list of operators above in **Related Resources**
- When using multiple operators together, remember to keep the *order of operations* (PEMDAS) your math teacher told you about in mind

```
print(100 + 5 * 3)

# Multiplication has a higher precedence than addition, and needs to be evaluated first
# The calculation above works out to be: 100 + 15 = 115
```
[Interactive order of operations example](https://www.w3schools.com/python/trypython.asp?filename=demo_precedence_multiplication)
