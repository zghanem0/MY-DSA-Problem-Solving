# -------------- problem 1 (Python code to reverse a string) -------------
# using loop
'''
def reverse(s):
    str = ""
    for i in s:
        str = i+str # this the algorithm
    return str

s = "Geek"

print ("The original string is : ",end="")
print (s)

print ("The reversed string(using loops) is : ",end="")
print (reverse(s))
'''

# Note
# he used s[0] for the base case to getout from the recursive loop

def reverse(s):
    if len(s) == 0:  # s[0] is trick to reach to the base case
        return s
    else:
        return reverse(s[1:]) + s[
            0]  # trick here,will pop the stack s[1:] then + s[0](g),the pop by nature is reversely


s = "ghanem"

print("The original string is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))

# ------------------ Problem 2 (get sum of strings of digits) --------------------
'''

#  using iteritive approach
def getSum(n):
    sum = 0
    while (n != 0):

        sum = sum + int(n % 10)  #to get the last digit  one by one 
        n = int(n / 10)  # for looping from the end

    return sum


n = 687
print(getSum(n))
'''
'''
#  using recursive approach
def sum_func(n):
    # Base case
    if len(str(n)) == 1:
        return n

    # Recursion Case
    else:
        return n % 10 + sum_func(n / 10)
'''


#  ------------------------------- Problem 3  (String Permutation) ------------------------------
'''

Fill Out Your Solution Below
Let's think about what the steps we need to take here are:

Iterate through the initial string – e.g., ‘abc’.
For each character in the initial string, set aside that character and get a list of all permutations of the string that’s left. So, for example, if the current iteration is on 'b', we’d want to find all the permutations of the string 'ac'.

Once you have the list from step 2, add each element from that list to the character from the initial string, and append the result to our list of final results. So if we’re on 'b' and we’ve gotten the list ['ac', 'ca'], we’d add 'b' to those, resulting in 'bac' and 'bca', each of which we’d add to our final results.

Return the list of final results.

Let's go ahead and see this implemented:

'''


def permute(s):
    out = []

    # Base Case
    if len(s) == 1:
        out = [s]

    else:
        # For every letter in string
        for i, let in enumerate(s):

            # For every permutation resulting from Step 2 and 3 described above
            st=permute(s[:i] + s[i + 1:])
            for perm in st:
                # Add it to output
                out = out + [let + perm]  # as if u merging to lists ,which [let+perm] list combined of 2 strings

    return out

str="abc"
print(permute(str))

def recursive_print(s):
    if s:
       print(s[0])
       recursive_print(s[1:])

st='Quora'
print(recursive_print(st))
