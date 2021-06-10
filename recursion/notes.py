'''

recursion has a problem is : the stack overflow , stack overflow happened when the infinite loop happened ,
so every recursive function need to have sth called a base case(stop point)
>> u have to the base case and the recursive case :
    - so usually u have 2 returns
>> there are 2 instances of recursion:
- The first is when recursion is used as a technique in which a function makes one or more calls to itself.
- The second is when a data structure uses smaller instances of the exact same type of data structure when it represents itself.

>> there are 2 types of stacks: either using my own stack, or call stack (return function_name) again

>> 
a,b=b,a+b  means :
    a=b
    b=old (a) + old (b)
or
    c=a+b
    a=b
    b=c
'''
