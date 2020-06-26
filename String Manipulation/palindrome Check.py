# the Space Complexity is O(1) and the Time Complexity is O(N) (the best)
def palindrome_check(str):
    left=0
    right=len(str)-1
    while left<right:
        if str[left] !=str[right]:
            return False
        left+=1
        right-=1
    return True

string = "abcdsdcba"
print(palindrome_check(string))


'''
# the Space Complexity is O(N) and the Time Complexity is O(N) 
def palindrome_check(str):
    counter = 0
    for i in range(len(str) - 1):
        end = len(str) - 1 - counter
        mid=(len(str) - 1)//2
        if i == end:
            if str[i] == str[end] and i==end==mid :
                return True
        if str[i] != str[end]:
            return False
        counter += 1

string = "abcdcba"
print(palindrome_check(string))
'''
'''
# the Space Complexity is O(N) and the Time Complexity is O(n^2) How?! >>
#because of the nature of the concatination in python (concatination in python is go through the entire list or array then concatinate)
# worest Solution
def palindrome_check(str):
    new_str = ""
    for i in range(len(str) - 1, -1, -1):
        new_str+=str[i]
    return str==new_str

string = "abcdcba"
print(palindrome_check(string))
'''

