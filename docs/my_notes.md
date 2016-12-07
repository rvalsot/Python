# Complete Python Masterclass

From the Udemy Course with the same name by: Tim Buchalka, available [here](https://www.udemy.com/python-the-complete-python-developer-course/learn/v4/overview)

## Installation in Ubuntu:

Mostly, Linux distributions come with Python 3.5+ and Python 2.7+, to check it:
``` shell
$ python3 -V
$ 3.5.2
```
The current version is about `3.5.2+`.

## The Basics

Python is an Object-Oriented-Interpreted Language, can run in almost all OS.

Typing:
* It is strictly typed.
* It is dynamically typed.

__Comments__

Comments are done the next way:

``` python
# This is a comment:
```

### Variables

To remember:
* Can start with either letters or underscores, and contain numbers in their names;
* The language is case sensitive

__Types__

* Integers: do not posses floating points;
*

### Arithmetic

Integer operations:

| Operator | Use |
| -------- | --- |
| `a + b`  | Addition |
| `a - b`  | Subtraction |
| `a * b`  | Multiplication |
| `a / b`  | Division, that will return a float number |
| `a // b` | Division, that will return an integer, discarding decimal parts |
| `a % b`  | Modulus |

Operator precedence is the general algebraic order.

### Input / Output

__Printing__

As simple as:
``` python
print("Hi folks!")
```

__Brotips__:

If you have a string, you can slice it using brackets:
``` python
my_string = "Vaquita3"
print(my_string[3:5]) # This will output 'ui'
```
You can repeat printing by multiplying it:
``` python
print(my_string * 2) # This will print: 'Vaquita3 Vaquita3'
```
You can check if there's a substring within another with the keyword `in`
``` python
print("3" in my_string) # This will print 'True'
```

__Console Input__

To log on the console, use `print(what)` and `input("Message: ")` to receive data:
``` python
variable = input("Enter your age: ")
print(variable)
```

Escape characters include: tab (`\t`), new line (`\n`).

To ease multi line printing, use triple quotes:

``` python
aSplitedString = """ This is a multi line, but single string,
it continues here!"""
```
