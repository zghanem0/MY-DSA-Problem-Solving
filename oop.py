'''
object is an instance of a class
>> there are to 2 types of attributtes:
  - class attribute (shared) : which is used inside the class and every object as well
  - instance attribute (instance-specific): so differs from instance orjects to another, every new created object of instance of a class will gonna use it and the it as an instance specific, in conterary of the class attribute will be shared with all instances
   
'''

class Dog:
  number_of_dogs=0      # class attribute
  def __init__(self, name, age):
      self.name = name      # instance attribute   that is way self exist, to replace each object or instance name so u can access is by instance_name.attribute_name
      self.age = age        # instance attribute
      number_of_dog+=1      # class attribute

a=Dog(dog_a,2)
# u can access the instance attribute by the instance only
print(a.name)  # access instance attribute

# u can access it by the instance or the class 
print(Dog.numbers)  # acceess class_attribute
print (a.numbers)   # acceess class_attribute


# summary:
>> attributes:
  with self. >> instance attribute
  withut self. >> calss attribute

