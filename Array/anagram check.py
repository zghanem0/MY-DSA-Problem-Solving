'''
*************** keys *************
in dictionaries u compaire the vlaue of the keys by using their keys for example:
if u used that condition: count[letter] == 0 >>> count[letter] is a key so u compare it's value if it is != 0 or not
 ********** the needed information **********
# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Adding elements one at a time
Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)

#Output:
Dictionary after adding 3 elements:
{0: 'Geeks', 2: 'For', 3: 1}
'''

def anagram(s1,s2):
    s1 = s1.replace(" ", "").lower()
    s2 = s2.replace(" ", "").lower()
    if len(s1) != len(s2):
        return False
    count={}
    for letter in s1: # for the value of that key "letter"
        if letter in count:
            count[letter]+=1
        else:
            count[letter]=1

    for letter in s2:
        if letter in count:
            count[letter]-=1
        else :
            count[letter]=1
    for i in count:
        if count[i] != 0: # in dic means: if the value of that key "count[i]" in count dic != 0
            return print("false")

    return print("True")

s1="ghanem ahmed"
s2="ahmed ghanem"
anagram(s1,s2)