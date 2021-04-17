'''
object is an instance of a class
>> there are to 2 types of attributtes:
  - class attribute : which is used inside the class and every object will not gonna use this kind of attribute 
  - instance attribute: every new created object of instance of a class will gonna use it 
   
'''

class Dog:
  number_of_dogs=0      # class attribute
  def __init__(self, name, age):
      self.name = name      # instance attribute
      self.age = age        # instance attribute
      number_of_dog+=1      # class attribute
