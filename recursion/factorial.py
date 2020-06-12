'''
>> there are differences between tailed and normal recursion :
- tailed is better than normal recursion

'''
'''
#-------------------- Solution (1) -------------------
# Factorial iteratively 
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

'''

# -------------- Solution (1) -----------------
# Factorial recursively

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
#-------------------- Solution (3) -------------------
# better
# tailed recursion is better than normal recursion
def fact(n,val=1):
    if n<=0:
        return n
    print(val)
    return fact(n-1,val+1)

#arr=''
fact(5)
#print(sorted(arr))
