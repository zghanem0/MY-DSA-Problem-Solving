n = 10
cache = [None] * (n+1) # predictable memory used



def fib_dyn(n):
    # Base Case
    if n <=1:
        return n

    # Check cache
    if cache[n] != None:
        return cache[n]

    # Keep setting cache
    cache[n] = fib_dyn(n - 1) + fib_dyn(n - 2)
    return cache[n]



print(fib_dyn(n))
print(cache)
'''
## Example 1: Using looping technique


## Example 2: Using recursion
def fibR(n):
if n==1 or n==2:
return 1
return fibR(n-1)+fibR(n-2)
print fibR(5)

## Example 3: Using generators
a,b = 0,1
def fibI():
global a,b
while True:
a,b = b, a+b
yield a
f=fibI()
f.next()
f.next()
f.next()
f.next()
print f.next()

## Example 4: Using memoization
def memoize(fn, arg):
memo = {}
if arg not in memo:
memo[arg] = fn(arg)
return memo[arg]

## fib() as written in example 1.
fibm = memoize(fib,5)
print fibm

## Example 5: Using memoization as decorator
class Memoize:
def __init__(self, fn):
self.fn = fn
self.memo = {}
def __call__(self, arg):
if arg not in self.memo:
self.memo[arg] = self.fn(arg)
return self.memo[arg]

@Memoize
def fib(n):
a,b = 1,1
for i in range(n-1):
a,b = b,a+b
return a
print fib(5)'''
