# ---------------- way 1 (iteratively ) (The Best) ------------------
# Time Complexity is O(n) and Space Complexity is O(1) >>> So (it is the best )
'''
def fibiter(n):
    first = 0
    sec = 1
    for i in range(1, n ):
        sum = first + sec
        first = sec
        sec = sum
    return sum


print(fibiter(6))

'''
# --------------- (Dynamic programming ) using memoization technique O(n) ----------------------------
# Time Complexity is O(n) and Space Complexity is O(N)

'''
n = 5
cache = [None] * (n + 1)  # why (n+1) because of searching in array start from (0)


def fib_dyn(n):
    # Base Case
    if n == 1 or n == 2:
        return 1

    # Check cache
    if cache[n] != None:  # (get the computation results)when u need the recursion of value n hit the cache of [n] first
        # !=None means the cache[n] feild is busy or have the value/results of cache[n] computation
        return cache[n]

    # Keep setting cache (storing computation results)
    cache[n] = fib_dyn(n - 1) + fib_dyn(n - 2)

    return cache[n]


print(fib_dyn(n))
print(cache)

# solution B for dynamic Programming 
def fib_dyn_hash(n, memoize=0):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = fib_dyn_hash(n - 1, memoize) + fib_dyn_hash(n - 2, memoize)
        return memoize[n]

n=5
memoize={1: 0, 2: 1}  # the base case values, which 0,1 is the the results of computing results 
print(fib_dyn_hash(n+1))



'''
#  *-------------------- way 3  , O(2^n)---------------------*

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
