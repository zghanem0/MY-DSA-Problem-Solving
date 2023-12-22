New is one of special staticmethods like __init__.
at instantiation, __new__ run first before __init__ 
both __init__ and __new__ methods are called when trying to create an instance of a class. According to the official Python documentation, __new__ is used when you need to control the creation of a new instance while __init__ is used to control the initialization of a new instance. Under the hood when creating Python objects, the __new__ is the first method called and is solely responsible for returning a new instance of the class.




Rreferences
====
[1] https://www.pythontutorial.net/python-oop/python-__new__/