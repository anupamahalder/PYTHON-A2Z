# OOP (Object Oriented Programming):
## What is Inheritance ?  
  => Inheritance is a fundamental concept in Object-oriented programming (OOP) that allows a new class (subclass or derived class) to inherit <b>properties and 
  behavior(methods)</b> from an existing class (superclass or base class). This enables code re-use and facilitates the creation of hierarchies of classes with shared
  characteristics.

  Inheritance is depicted using an "is-a" relationship, where a subclass "is-a" type of its superclass. The subclass inherits all the attributes and methods of its 
  superclass and can also define its own attributes and methods.
  

## What is Encapsulation?
=> Encapsulation is the building of data (attributes) and methods (functions) that operate on the data into a single
unit, called a class. It is one of the four fundamental principles of object-oriented programming (OOP), along with
inheritance, polymorphism, and abstraction. Encapsulation helps to hide the internal state of an object and only expose the necessary functionality, thus providing better control over access to the data.


## What are Access Modifiers?
=> Access Modifiers are keywords in programming languages that specify the accessibility of classes, attributes, methods, and other members of a class. They control how these members can be accessed and modifies from outside the class. Common access modifiers include public, private, and protected.


## What is Operator Overloading?
=> Operator overloading is a feature in object-oriented programming languages that allows a class to define the behavior of its operators such as +, -, *, /, etc. This means that operators can have different meanings depending on the context in which they are used. In Python, operator overloading is achieved by defining special methods within a class, often referred to as magic or dunder methods (due to their double underscore prefix and suffix).

<li>For example:</li>
You can define the __add__ method to overload the + operator for your custom class. This allows instances of the class to use the + operator to perform custom operations.

### Dunder/Magic methods:
Python Magic methods are the methods starting and ending with double underscores '__'. They are defined by built-in classes in Python and commonly used for operator overloading. 
They are also called Dunder methods, Dunder here means "Double Under (Underscores)".
Built in classes define many magic methods, dir() function can show you magic methods inherited by a class.

Below are the lists of Python magic methods and their uses.

#### 1. Initialization and Construction
<li>__new__: To get called in an object’s instantiation</li>
<li>__init__: To get called by the __new__ method</li>
<li>__del__: It is the destructor</li>

#### 2. Numeric magic methods
<li>__trunc__(self): Implements behavior for math.trunc()</li>
<li>__ceil__(self): Implements behavior for math.ceil()</li>
<li>__floor__(self): Implements behavior for math.floor()</li>
<li>__round__(self,n): Implements behavior for the built-in round()</li>
<li>__invert__(self): Implements behavior for inversion using the ~ operator</li>
<li>__abs__(self): Implements behavior for the built-in abs()</li>
<li>__neg__(self): Implements behavior for negation</li>
<li>__pos__(self): Implements behavior for unary positive </li>

#### 3. Arithmetic operators
<li>__add__(self, other): Implements behavior for math.trunc()</li>
<li>__sub__(self, other): Implements behavior for math.ceil()</li>
<li>__mul__(self, other): Implements behavior for math.floor()</li>
<li>__floordiv__(self, other): Implements behavior for the built-in round()</li>
<li>__div__(self, other): Implements behavior for inversion using the ~ operator.</li>
<li>__truediv__(self, other): Implements behavior for the built-in abs()</li>
<li>__mod__(self, other): Implements behavior for negation</li>
<li>__divmod__(self, other): Implements behavior for unary positive</li>
<li>__pow__: Implements behavior for exponents using the ** operator</li>
<li>__lshift__(self, other): Implements left bitwise shift using the << operator</li>
<li>__rshift__(self, other): Implements right bitwise shift using the >> operator</li>
<li>__and__(self, other): Implements bitwise and using the & operator</li>
<li>__or__(self, other): Implements bitwise or using the | operator</li>
<li>__xor__(self, other): Implements bitwise xor using the ^ operator</li>

#### 4. String Magic Methods
<li>__str__(self): Defines behavior for when str() is called on an instance of your class</li>
<li>__repr__(self): To get called by built-int repr() method to return a machine readable representation of a type</li>
<li>__unicode__(self): This method to return an unicode string of a type</li>
<li>__format__(self, formatstr): return a new style of string</li>
<li>__hash__(self): It has to return an integer, and its result is used for quick key comparison in dictionaries</li>
<li>__nonzero__(self): Defines behavior for when bool() is called on an instance of your class</li>
<li>__dir__(self): This method to return a list of attributes of a class</li>
<li>__sizeof__(self): It return the size of the object</li>

#### 5. Comparison magic methods
<li>__eq__(self, other): Defines behavior for the equality operator, ==</li>
<li>__ne__(self, other): Defines behavior for the inequality operator, !=</li>
<li>__lt__(self, other): Defines behavior for the less-than operator, <</li>
<li>__gt__(self, other): Defines behavior for the greater-than operator, ></li>
<li>__le__(self, other): Defines behavior for the less-than-or-equal-to operator, <=</li>
<li>__ge__(self, other): Defines behavior for the greater-than-or-equal-to operator, >=</li>

