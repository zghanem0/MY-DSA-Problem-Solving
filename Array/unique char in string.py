'''

if the characters aren't unique  return False otherwise return True
'''


str = "abcdf"

letters = set()  # or list not differs


def uni_char(s):
    for let in s:
        if let in letters:
            return False
        else:
            letters.add(let)

    return True


print("solution 1 manually way :", uni_char(str))

'''
from collections import defaultdict

str = "abcdfgf"


def uniq_char(s):
    dict = defaultdict(int)
    redundant_chars = []
    uniq_chars = []
    for char in s:
        dict[char] += 1
    for char in dict:
        if dict[char] != 1:
            redundant_chars.append(char)
            return False
    return True


print("solution 2 manually way :", uniq_char(str))

'''
# ***************** using set() advantage *********************
# just learn the interviewer about that solution only not not do it but use the manually solution instade
# set() give u the unique number of element even if the number is duplicated , for example
# print(set(str))
'''
def uni_char(s):
    return bool(len(set(str)) == len(str))


print("Solution 2 using set trick ", uni_char(str))
'''
