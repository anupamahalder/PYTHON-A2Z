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

## **Binary Types**

- **bytes**:
    
    The bytes() function returns a bytes object. It convert objects into bytes objects, or create empty bytes object of the specified size. The difference between bytes() and bytearray() is that bytes() returns an object that cannot be modified, and bytearray() returns an object that can me modified.
    
- **bytearray:**
    
    The bytearray type is a mutable sequence of integers in the range between 0 and 255. The ***bytearray***() function returns a ***bytearray*** object. It can convert objects into ***bytearray*** objects, or create empty ***bytearray*** object of the specified size.
    

Byte Arrays are commonly used to **store large amounts of data such as images, audio files, video files, or text files for use in an applications**.

## None Type

The None keyword is used to define a null value, or no value at all. None is not the same as 0, False, or an empty string.

## Sequence Type Data:

### **List Type**

Lists in Python are ordered sequences that can hold any type of data. They are mutable, meaning that their contents can be changed after they are created. Lists are created using square brackets, with the elements of the list separated by commas. For example, the following code creates a list of three elements:

`my_list = [1, 2, 3]`

### **Tuple Type**

A tuple in Python is an ordered collection of elements that cannot be changed. Tuples are similar to lists, but they are immutable, meaning that the elements of a tuple cannot be changed once the tuple is created. Tuples are created using parentheses and commas to separate the elements.

```python
my_tuple = (1, 2, 3)
```

Tuples can be accessed using indexing, just like lists. The first element of a tuple is at index 0, the second element is at index 1, and so on.

```python
print(my_tuple[0]) #1
```

Tuples can also be nested, meaning that a tuple can contain another tuple as one of its elements. For example, the following code creates a nested tuple:

```python
my_nested_tuple = ((1, 2, 3), (4, 5, 6))
```

This tuple contains two tuples, each of which contains three elements. The first tuple in the nested tuple is at index 0, and the second tuple is at index 1.

```python
print(my_nested_tuple[0][0]) #1
```

Tuples are a useful way to store data that needs to be kept in a specific order. They are also useful for passing data around between functions without changing the data.

### **Range type**

Python range is **a function that returns a sequence of numbers**. By default, range returns a sequence that begins at 0 and increments in steps of 1. The range function only works with integers. Other data types like float numbers cannot be used.

The range() function takes one, two, or three arguments.

- If one argument is passed, the range() function returns a sequence of numbers starting from 0 and increments by 1 until it reaches the specified number. For example, range(5) returns 0, 1, 2, 3, and 4.
- If two arguments are passed, the range() function returns a sequence of numbers starting from the specified start number and increments by 1 until it reaches the specified stop number. For example, range(1, 5) returns 1, 2, 3, and 4.
- If three arguments are passed, the range() function returns a sequence of numbers starting from the specified start number and increments by the specified step until it reaches the specified stop number. For example, range(1, 5, 2) returns 1, 3, and 5.
