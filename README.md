# Python
Refereneces : (https://www.w3schools.com/python)

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

## Operators in Python

Operators are used to perform operations on variables and values.

Python divides the operators in the following groups:

- Arithmetic operators
- Assignment operators
- Comparison operators
- Logical operators
- Identity operators
- Membership operators
- Bitwise operators

### Python Arithmetic Operators

Arithmetic operators are used with numeric values to perform common mathematical operations:

| Operator | Name | Example |
| --- | --- | --- |
| + | Addition | x + y |
| - | Subtraction | x - y |
| * | Multiplication | x * y |
| / | Division | x / y |
| % | Modulus | x % y |
| ** | Exponentiation | x ** y |
| // | Floor division | x // y |

### Python Assignment Operators

Assignment operators are used to assign values to variables:

| Operator | Example | Same As |
| --- | --- | --- |
| = | x = 5 | x = 5 |
| += | x += 3 | x = x + 3 |
| -= | x -= 3 | x = x - 3 |
| *= | x *= 3 | x = x * 3 |
| /= | x /= 3 | x = x / 3 |
| %= | x %= 3 | x = x % 3 |
| //= | x //= 3 | x = x // 3 |
| **= | x **= 3 | x = x ** 3 |
| &= | x &= 3 | x = x & 3 |
| |= | x |= 3 | x = x | 3 |
| ^= | x ^= 3 | x = x ^ 3 |
| >>= | x >>= 3 | x = x >> 3 |
| <<= | x <<= 3 | x = x << 3 |

### Python Comparison Operators

Comparison operators are used to compare two values:

| Operator | Name | Example |
| --- | --- | --- |
| == | Equal | x == y |
| != | Not equal | x != y |
| > | Greater than | x > y |
| < | Less than | x < y |
| >= | Greater than or equal to | x >= y |
| <= | Less than or equal to | x <= y |

### Python Logical Operators

Logical operators are used to combine conditional statements:

| Operator | Description | Example |
| --- | --- | --- |
| and | Returns True if both statements are true | x < 5 and  x < 10 |
| or | Returns True if one of the statements is true | x < 5 or x < 4 |
| not | Reverse the result, returns False if the result is true | not(x < 5 and x < 10) |

### Python Identity Operators

Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

| Operator | Description | Example |
| --- | --- | --- |
| is | Returns True if both variables are the same object | x is y |
| is not | Returns True if both variables are not the same object | x is not y |

### Python Membership Operators

Membership operators are used to test if a sequence is presented in an object:

| Operator | Description | Example |
| --- | --- | --- |
| in | Returns True if a sequence with the specified value is present in the object | x in y |
| not in | Returns True if a sequence with the specified value is not present in the object | x not in y |

### Python Bitwise Operators

Bitwise operators are used to compare (binary) numbers:

| Operator | Name | Description | Example |
| --- | --- | --- | --- |
| & | AND | Sets each bit to 1 if both bits are 1 | x & y |
| | | OR | Sets each bit to 1 if one of two bits is 1 | x | y |
| ^ | XOR | Sets each bit to 1 if only one of two bits is 1 | x ^ y |
| ~ | NOT | Inverts all the bits | ~x |
| << | Zero fill left shift | Shift left by pushing zeros in from the right and let the leftmost bits fall off | x << 2 |
| >> | Signed right shift | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off | x >> 2 |

## **Operator Precedence**

The precedence order is described in the table below, starting with the highest precedence at the top:

| Operator | Description |
| --- | --- |
| () | Parentheses |
| ** | Exponentiation |
| +x  -x  ~x | Unary plus, unary minus, and bitwise NOT |
| *  /  //  % | Multiplication, division, floor division, and modulus |
| +  - | Addition and subtraction |
| <<  >> | Bitwise left and right shifts |
| & | Bitwise AND |
| ^ | Bitwise XOR |
| | | Bitwise OR |
| ==  !=  >  >=  <  <=  is  is not  in  not in | Comparisons, identity, and membership operators |
| not | Logical NOT |
| and | AND |
| or | OR |

**NOTE**: If two operators have the same precedence, the expression is evaluated from left to right.

## Swapping

In programming, a swap function is **a useful tool that allows the values of two variables to be exchanged with each other**.

```python
a = 5
b = 7
#swapping
a,b = b,a
#after swapping
a = 7
b = 5
```

## User Input

Using input() method, we can take input from user in Python.

```python
username = input("Enter your name:")
print(username)
```
## Type Casting

Type casting, also known as type conversion, is the process of converting a variable's data type into another data type. These conversions can be implicit (automatically interpreted) or explicit (using built-in functions).

**There are two types of type casting in Python:**

- Implicit type casting: This is when Python automatically converts a data type to another data type. For example, if you add a string and an integer, Python will automatically convert the string to an integer.
- Explicit type casting: This is when you use a built-in function to convert a data type to another data type. For example, you can use the **`int()`** function to convert a string to an integer.

We cannot convert string directly into integer if string contains non-digit as character.

```python
name = "hello"
print(int(name)) # Error will come as name doesn't contain digits
num = "1244"
print(int(num)) # 1244 (As num contains digit as character"
```

To convert string to integer or float the string should have valid integer or float inside string, otherwise error will come to convert data type.

## Python Lists

Lists are used to store multiple items in a single variable.

List items can be of any data type:

```python
list1 = ["apple", "banana", "cherry"]
list2 = [1,2,3,4,5]
list3 = [True, False, False, True]
```

List items will be inside square bracket. To add multiple values in a list we have to add comma after each item. We will not add any comma after the last item in the list. Index is required to get a particular item from the list. Index starts with 0.

The list is changeable/mutable, meaning that we can change, add, and remove items in a list after it has been created.

**Update list item:** 

```python
list1[0] = “orange”
```

**Insert Items in list:** 

1. **Append:** 
    
    To add an item to the end of the list, use the `append()` method.
    
    ```python
    list1.append(”Watermelon”)
    ```
    
2. To insert a list item at a specific index, use the `insert()` method. Where we have to give index number then items inside this function.
    
    ```python
    list1.insert(2, “Grape”)
    ```
**Remove List Items:**

1. **Remove Specified Item:**
    
    The `remove()` method removes the specified item. We have to write the element inside remove method.
    
    ```python
    list1.remove(”banana”)
    ```
    

 **2. Remove Specified Index:**

1. The `pop()` method removes the specified index. If you do not specify the index, the pop() method removes the last item.
    
    ```python
    list1.pop(2) #here 2 is the index number
    ```
    
2. The `del` keyword also removes the specified index. We have to use square bracket.
    
    ```python
    del list1[1] #here 1 is the index number
    ```
    
1. **Clear the list:**
    
    The `clear()` method empties the list. The list still remains, but it has no content.
    
    ```python
    list2.clear()
    ```
## Function in Python

A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

**Creating a function:**

In Python a function is defined using the def keyword. 

```python
def func(num1, num2):
	return num1+num2
```

**Calling a Function:**

To call a function, use the function name followed by parenthesis. And passing arguments if the function requires any parameter.

```python
res = func(4, 7)
print(res) # 11
```
**Parameters or Arguments?**

The terms *parameter* and *argument* can be used for the same thing: information that are passed into a function.

From a function's perspective:

A parameter is the variable listed inside the parentheses in the function definition.

An argument is the value that is sent to the function when it is called.

**Arguments:**

Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

**Example:**

```python
def my_func(fname): #here fname is the parameter
	print(fname + " Hello, how are you?")
	
my_func("Anupama")
my_func("Tom")
```

The following example has a function with one argument (fname). When the function is called, we pass along a first name, which print the name with a question.
