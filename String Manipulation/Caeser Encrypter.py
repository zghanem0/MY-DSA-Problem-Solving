'''
# the Space Complexity is O(1) and the Time Complexity is O(N)
def caesar_enc(str, key):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', ' j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z' ] # or say alpha=list("abcdefjhijklmnopqrstuwuxyz")
    HashTable = {}
    string = []
    for i in range(key, key - 26, -1):
        HashTable[alpha[i - key]] = alpha[i]
    for char in str:
        string.append(HashTable[char])
    return "".join(string)


string="abcdab"
print(caesar_enc(string, 2))
'''
# the Space Complexity is O(1) and the Time Complexity is O(N) (more practical than above)
def caesar_enc(str, key):
    newLetter=[]
    for letter in str:
        newLetter.append(getNewLetter(letter,key))
    return "".join(newLetter)
def getNewLetter(letter,key):
    codedletter=ord(letter)+key
    print(codedletter)
    return chr(codedletter) if codedletter<=122 else chr(96+codedletter%122)

string = "abcdab"
print(caesar_enc(string, 2))
