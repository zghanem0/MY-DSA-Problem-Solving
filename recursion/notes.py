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







# how to solve any recursive problem or dp: is all about f(each-cell/sub-problem)=
0- will move through the pproblem normally untill u reach to the point in which there are many possibilities, when u feel that u are confused, and don't know where should u move or u have many posibilities or directions start from which direction use recursion in both and either get the max or concatenate the results or both max and concatenate, depends on the nature of the problem
1- base case
2- return result
3- the smallest problem; think if the input as if it is just 1 or 2 inputs
4- don't forget to add the i,j as an args in your func to
NOTE!: if u want to make it continue after return, recursive again for example; return 1 + lcs(s1, s2, i + 1, j + 1) << in the result not the last return, the last return id for the possibilities
- the last return when u fork because u confused because u don't know the right way, and use min or max if he need the smallest/minimum or longest/maximum + value if needed. e.g;  1 + min(scs(i + 1, j), scs (i, j + 1)) which value 1+ represends the number of ways for xxxxx and so on
- u small/ the problem by chaning the value of the parameters untill u reach to the smallest problem.
- is it make u confused about take it or leave it, it mean u will do sth like this , subsets(arr, k-arr[i], i+1)+ subsets(arr, k, i+1), as u see he take the first and leave it to the second and the second will putted into the same descion eaither take it oe leave it and so on.


'''
