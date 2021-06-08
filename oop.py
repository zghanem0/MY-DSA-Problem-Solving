'''
>> object is an instance of a class,  An instance of a class is traditionally known as an object, so object==instance==class instance

>>> OOP Compound from 4 terms:
- encapsulation : is a way to encapsulate or hide your attributes and methods from accessing from the out side for simplicity and security puposes and instead using stters and getters to set and get values
- abstraction: shows only useful data by providing the most necessary details, example, expose x,y so u will not have to know about what will gonna happen and the implementations
- Polymorphism(poly + morphism): i can do single action (do sth) in a different ways, so we can implement it either by overriding the method (overriding) or creating multiple form of the method(overloading)
  - overloading : allows the object to decide which form of the function to implement at compile-time (overloading) as well as run-time (overriding).
  - overriding: the class is the same but i just need a change for a little methods
- Inheritance: is the procedure in which one class inherits the attributes and methods of another class.
Encapsulation:-- Information hiding.
Abstraction:-- Implementation hiding.



>> there are to 2 types of attributtes:
  - class attribute (shared) : which is used inside the class and every object as well
  - instance attribute (instance-specific): so differs from instance orjects to another, every new created object of instance of a class will gonna use it and the it as an instance specific, in conterary of the class attribute will be shared with all instances

'''


class Dog:
    numbers = 0  # class attribute

    def __init__(self, name, age):  # constructor
        self.__name = name  # __ convert the attribute from publicc to private to encapsulcate it and prevent changing it from changing from the outside
        self.age = age  # instance attribute   that is way self exist, to replace each object or instance name so u can access is by instance_name.attribute_name
        Dog.numbers += 1  # class attribute
        self.name = 0

    def get(self):  # instance method because starts with self to use it's attributes
        print(f"the dog name: {self.name} and the dog age: {self.age}")

    @classmethod
    def diff_init_for_this_class(cls, name, age):
        return cls(name, age)
    @staticmethod
    def static_method_to_calc_the_health_of_dog(age,health):
        return ((age.age/10)*100 + health)/100



a = Dog("dog_a", 2)
# u can access the instance attribute by the instance only
# print(a.name)  # access instance attribute, u can't access it from the outside because it is private and will create
# new attribute called name and the __name will be the same and can not see it, so the name will not be the __name

# u can access it by the instance or the class 
print(Dog.numbers)  # acceess class_attribute
print(a.numbers)  # acceess class_attribute

'''
# summary:
>> attributes:
  with self. >> instance attribute
  without self. >> class attribute

>> methods:
  instance method: using self as a parameter, to access it's parameters that start with "self.", logic !
  class methods: use this "@classmethod" annotaion or docerator  above the function, know about class, so can change the class behaviour 
  static method (ordinary method): used for static purposes and know nothing about classes and instances 

>> What is a static method?
Static methods, much like class methods, are methods that are bound to a class rather than its object.

They do not require a class instance creation. So, they are not dependent on the state of the object.

The difference between a static method and a class method is:

Static method knows nothing about the class and just deals with the parameters.
Class method works with the class since its parameter is always the class itself.
They can be called both by the class and its object.

Class.staticmethodFunc()
or even
Class().staticmethodFunc()

'''
dog_b = Dog.diff_init_for_this_class("dog-b", 3)
print(dog_b.name)
