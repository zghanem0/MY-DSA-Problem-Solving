```
**************** What U Should Learn **************************
********* when using tuples over lists *********
    - when need print thing in pair ex : {(1,2),(0,5)} and so on
Functional differences:
Tuples are fixed size in nature whereas lists are dynamic.
In other words, a tuple is immutable whereas a list is mutable.
You can't add elements to a tuple. Tuples have no append or extend method.
You can't remove elements from a tuple. Tuples have no remove or pop method.
You can find elements in a tuple, since this doesn’t change the tuple.
You can also use the in operator to check if an element exists in the tuple.
Tuples are faster than lists. If you're defining a constant set of values and all you're ever going to do with it is iterate through it, use a tuple instead of a list.
It makes your code safer if you “write-protect” data that does not need to be changed. Using a tuple instead of a
list is like having an implied assert statement that this data is constant, and that special thought (and a specific
function) is required to override that.
Some tuples can be used as dictionary keys (specifically, tuples that contain immutable values like strings, numbers, and other tuples). Lists can never be used as dictionary keys, because lists are not immutable.
>> Tubles has 2 Methods only
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
**** what is the diff between lists and Sets
List:
the order of elements is well defined,
duplicates are possible,
any object can participate.
Set:
the order of the elements is unknown,
elements are unique,
only hashable objects can be inserted (tuples, and numbers, but not lists).
Can be user defined objects that define __hash__() and __eq__() methods, and never change.
Performance differences:
List: x in lst works in O(len(lst)). Longer lists are slower.
Set: x in a_set works in O(1). List length does not affect this query.
Example for order changing in sets:
print(set([1,-10,34]))
print([1,-10,34])
Gives on my machine (set order changes, list does not)
set([1, 34, -10])
[1, -10, 34]
Example for uniqueness of sets:
print(set([1, 2, 1]))
print([1, 2, 1])
Gives on my machine (sets give unique values, list keeps all)
set([1, 2])
[1, 2, 1]
Example: Set does not allow unhashable types:
>> lst=[1,2,3]
>> s= set()
>> s.add(lst)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
But it is no problem to add a list to a list.
But it is still possible to add user defined object objects to a list if __eq__ and __hash__ are defined:
class foo(object):
    def __init__(self, x):
      self.x= x
    def __hash__(self):
      return self.x
    def __eq__(self, other):
      return self.x == other.x
    def __repr__(self):
      """This function is just for nice printing"""
      return "foo(%s)" % self.x
lst = [foo(54), foo(54), foo(3)]
print(lst)
print(set(lst))
Gives
[foo(54), foo(54), foo(3)]
set([foo(3), foo(54)])
****** learn more sbout sets *********
Initialize a Set
Sets are a mutable collection of distinct (unique) immutable values that are unordered.
You can initialize an empty set by using set().
emptySet = set()
To intialize a set with values, you can pass in a list to set().
dataScientist = set(['Python', 'R', 'SQL', 'Git', 'Tableau', 'SAS'])
# Most common sets methods :
>> Add Values to a Set
You can use the method add to add a value to a set.
dataScientist.add(['Powerpoint', 'Blender'])
>> Remove Values from a Set
There are a couple ways to remove a value from a set.
Option 1: You can use the remove/discard method to remove a value from a set.
graphicDesigner.remove('Illustrator')
>> union()	Return a set containing the union of sets
```
>> update()	Update the set with the union of this set and others
