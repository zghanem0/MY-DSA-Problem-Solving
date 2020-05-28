# ---------------- way 1 (iteratively )------------------
'''
def fibiter(n):
    f1=1
    f2=1
    for i in range(1,int(n)-1):
        sum = f1+f2
        f1=f2
        f2=sum
    return f2
print(fibiter(6))

'''


'''
def fn(n):
    # single line to find factorial
    if (n == 1 or n == 0):

        return 1
    else:
        S=S+n
        return n + fn(n - 1)  # >> fn(fn(n) >> fn(n) * fn(fn) which the loop end until {return (n) * } &
        # the function is fn(n)= n * >>that is the func

# Driver Code
num = 4

print("sum from 0 to ", num, "is", fn(num))
'''

# fibonacci recursively
# -------------- way1 -----------------
'''
def fn(n):
    # single line to find factorial
    if (n == 1 or n == 0):

        return 1
    else:
        print(n)
        return (n) * fn(n - 1) # >> fn(fn(n) >> fn(n) * fn(fn) which the loop end until {return (n) * } &
        # the function is fn(n)= n * >>that is the func


# Driver Code
num = 4
print("Factorial of", num, "is", fn(num))
'''
#  *-------------------- way 2  , o(2^n)---------------------*
'''
>> if the n=5 
recursive(4) + recursive(3)
(recursive(3) + recursive(2)) + (recursive(2) + recursive(1))
((recursive(2) + recursive(1)) + 1) + (1 + 1)
((1 + 1) + 1) + (1 + 1)
= 5
the main of this trick of fibonacci approach is the numbers of (1) that is returned from the base case is =n 


def fib(n):
    if (n <2):

        return n
    else:
        print(n)
        return fib(n - 1) + fib(n - 2)


print("fib num : ", fib(5))
# whar if i didn't know that the numbers of (1) that is returned from the base case is =n ?? definitely there is a way

'''
# ---------------the best solution (Dynamic programming ) using memoization technique O(n) ----------------------------


# Instantiate Cache information
n = 10
cache = [None] * (n + 1)


def fib_dyn(n):
    # Base Case
    if n == 0 or n == 1:
        return n

    # Check cache
    if cache[n] != None:  # when u need the recursion of value n hit the cache of [n] first
        return cache[n]

    # Keep setting cache
    cache[n] = fib_dyn(n - 1) + fib_dyn(n - 2)

    return cache[n]

print(fib_dyn(n))
