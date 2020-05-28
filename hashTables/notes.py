'''
>>hash tables has many different names : hash maps , an ordered maps , dictionaries
** the Order of Hash Table is O(1) that is the Average ,but in the worest cas will be O(N)
>> when the hash table Order becoming O(N):
1- If too many elements were hashed into the same key: looking inside this key may take O(n) time.

2- Once a hash table has passed its load balance - it has to rehash [create a new bigger table, and re-insert each element to the table].


'''