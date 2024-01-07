# Python

## What do you use Python for?

- **Data analysis**
- Web Development
- **Machine learning**
- System administrator / writing automation scripts/infrastructure configuration
- Programming of web parsers/scrapers/crawlers
- Software testing /writing automated tests
- Software prototyping
- Educational purposes
- Desktop development
- Network programming
- Embedded development
- Game development
- Computer graphics
- Mobile development
- Other


## Python Comments

To ignore compiling a text/description we use comments

using # we comment in python

Comment is used to increase the readability of the code to other developers.

There are two types of comment

1. Single line comment:
    ```python
    #hello
    ```
3. Multi line comment: 
    
    ```python
    ‘’’ Hi
    
    udfus dsnsnvfds ‘’’
    ```
    

## Module & PIP

**Module:**

A module is a file consisting of Python code. A module can define functions, classes and variables. A module can also include runnable code.

**Pip:**

Pip is **a package manager for Python that allows users to install and manage software packages**.Note: If you have Python version 3.4 or later, ***PIP*** is included by default.

For example, to install the NumPy package, you can type **`pip install numpy`** in the command prompt.

## Types of Module

1. Built-in Modules ( https://docs.python.org/3/py-modindex.html )
2. User-defined Modules ( https://data-flair.training/blogs/python-libraries/ )

Built-in modules are modules that come preinstalled with Python, while user-defined modules are modules that you create yourself.

**Built-in** modules are modules that come preinstalled with Python. They are part of the Python interpreter and cannot be modified by the user. Some of the commonly used built-in modules are **math**, random, datetime, and os.

**User-defined** modules are modules that you create yourself. They are Python files that contain code, such as functions, classes, and variables. User-defined modules can be imported into other Python programs to be used.

## Python Variables

A Python variable is **a reserved memory location to store values**. In other words, a variable in a python program gives data to the computer for processing. Every value in Python has a datatype. Different data types in Python are Numbers, List, Tuple, Strings, Dictionary, etc.

## Data types

**Built-in Data Types**

In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:

| Text Type: | str |
| --- | --- |
| Numeric Types: | int, float, complex |
| Sequence Types: | list, tuple, range |
| Mapping Type: | dict |
| Set Types: | set, frozenset |
| Boolean Type: | bool |
| Binary Types: | bytes, bytearray, memoryview |
| None Type: | NoneType |

**Getting the Data Type**

You can get the data type of any object by using the `type()` function:

```python
x = 5
print(type(x))
```

**NOTE:**

By default input in python is in the form of string
