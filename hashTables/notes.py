'''
>>hash tables has many different names : hash maps , an ordered maps , dictionaries
** the Order of Hash Table is O(1) that is the Average ,but in the worest cas will be O(N)
>> when the hash table Order becoming O(N): (in case of Collision)
1- If too many elements were hashed into the same key: looking inside this key may take O(n) time.

2- Once a hash table has passed its load factor  - it has to rehash [create a new bigger table, and re-insert each element to the table].

>>  Collision resolution
Open hashing (chaining)
There are two main ideas for how to deal with collisions. The best way is usually chaining:
each array entry corresponds to a bucket containing a mutable set of elements. (Confusingly, this approach is also known as closed addressing or open hashing.)
 Typically, the bucket is implemented as a linked list, so each array entry (if nonempty) contains a pointer to the head of the linked list.

To check whether an element is in the hash table, the key is first hashed to find the correct bucket to look in.
 Then, the linked list is scanned to see if the desired element is present. If the linked list is short, this scan is very quick.

An element is added or removed by hashing it to find the correct bucket.
 Then, the bucket is checked to see if the element is there, and finally the element is added or removed appropriately from the bucket in the usual way for linked lists.



'''