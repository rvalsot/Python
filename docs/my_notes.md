# Complete Python Masterclass

From the Udemy Course with the same name by: Tim Buchalka, available [here](https://www.udemy.com/python-the-complete-python-developer-course/learn/v4/overview)

##  Installation

Mostly, Linux distributions, Ubuntu and Fedora our concernts, come with Python 3.5+ and Python 2.7+, to check it:
``` shell
$ python3 -V
$ 3.5.2
```
The current version is about `3.5.2+`.

## The Basics

Python is an Object-Oriented-Interpreted Language, can run in almost all OS.

Typing:
* It is strictly typed;
* It is dynamically typed;

__Comments__

Comments are done the next way:

``` python
# This is a comment:
```

## Variables

To remember:
* Can start with either letters or underscores, and contain numbers in their names;
* The language is case sensitive

__Types__

* Integers: do not posses floating points;
*

## Arithmetic

Integer operations:

| Operator | Use |
| -------- | --- |
| `a + b`  | Addition |
| `a - b`  | Subtraction |
| `a * b`  | Multiplication |
| `a / b`  | Division, that will return a float number |
| `a // b` | Division, that will return an integer, discarding decimal parts |
| `a % b`  | Modulus |
| `a ** b` | Power |

Operator precedence is the general algebraic order.

## Input / Output

__Printing__

As simple as:
``` python
print("Hi folks!")
```

Printing several can be easier with replacer `{n}` and `.format` method:

``` python
print("This is a moth sequence: {0}, {1}, {2}.".format("Jan", "Feb", "Mar"))
# This will output:
# This is a month sequence: Jan, Fe, March.
```
The replacer can be called several times, given the `.format` sequence.

_Ranged Printing_ can be done using the `for`:
``` python
for i in range(1,3)
print("Number: %d" %(i))
# This will print:
# Number: 1
# Number: 2
# Number: 3
```

Brotips

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

* When using `%` for ranged formatted printing, `n%` will leave n-spaces, so we avoid columns mess.

__Console Input__

To log on the console, use `print(what)` and `input("Message: ")` to receive data:
``` python
variable = input("Enter your age: ")
print(variable)
```

To cast into a number, surround the input by:
``` python
number = int(input("Please, enter a number: ")) # This will cast input to an integer
```

__Extras__

* Escape characters include: tab (`\t`), new line (`\n`).

* To ease multi line printing, use triple quotes:

``` python
aSplitedString = """ This is a multi line, but single string,
it continues here!"""
```



## Flow Control

First brotip: do not forget well-done indentation in your program.

__If Group__

The If structure is the following:
``` python  
if condition:
  # Do something
elif condition:
  # Do some other thing
else:
  # Well, do this
```

Tests for not emptiness are:
``` python
x
if x:
  # do something
```
This will evaluate to `False` as `x` is not filled.

Conditions for existence check if `s` exists within some context:
``` python
if letter in word:
  #do something
else:
  #do otherwise
```

Tests Operators include:

| Operator | Use |
| -------- | --- |
| `==` | Equals |
| `!=` | Not Equal |
| `>`, `>=` | Greater than, Greater or Equal to |
| `<`, `<=` | Lesser than, Lesser or Equal to |

__For Loops__


There are several forms of the `for` loops, covering:

* Standard `for` in a range.
* For-each iteration
* Stepped for loop, with a step different that 1

``` python
for i in range (your_range):
  # do something

for i in list_of_stuff:
  # for each approximation

for i in range(begin, end, step):
  # stepped iteration
```

Brotips
* `len(some)` is a good help to set a range.
