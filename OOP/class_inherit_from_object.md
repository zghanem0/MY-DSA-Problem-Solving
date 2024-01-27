Why do Python classes inherit object?
- In Python 3, all classes automatically inherit from the object class. The object class is the base class for all objects in Python, so it provides a set of basic methods and attributes that all objects can use. For example, the __init__ method, which is called when an object is created, is defined in the object class. By inheriting from object, your class gets all of these basic methods for free.
- In Python 2, classes do not automatically inherit from object, so you have to specify it explicitly if you want your class to inherit from object. This is done by including object as the first base class in the class definition, like this:
```
class MyClass(object):
    # class definition goes here
```
