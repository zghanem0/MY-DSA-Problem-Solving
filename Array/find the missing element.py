# i will explain 3 ways  to show u the for in zip hows work

array1 = [1, 2, 3, 4, 5,6]
array2 = [5, 2, 4, 3, 1]

# in case one iterator in zip function

'''
def finder(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)
    for num1 in zip(arr1, arr2):
        print(num1)


finder(array1, array2)
'''
# in case 2 iterator in zip function
'''def finder(arr1, arr2):
    arr1 = sorted(arr1)
    arr2 = sorted(arr2)

    for num1,num2 in zip(arr1, arr2):
        if num1 != num2: # to ensure printing the number if not exist at the middle of array
            print(num1)

        return print(arr1[-1]) # to make sure printing the number if array1 increased 1 number, because they searching in pairs
finder(array1, array2)'''
#            **************** WAY2 Using (HashTable) ******************
# the best solution is to use the HashTable

from collections import defaultdict

count = defaultdict(float) # should be int but did it intentionally to show u that value and keys that add in the dict
print(count)
names_lst1 = "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Smith".split(" ")
names_lst2 = "Mike John Mike Anna Mike John John Mike Mike Britney Smith Anna Mike".split(" ")

def finder(names_list1,names_list2):
    for name in names_list1:
        count[name] +=1

    for name in names_list2:
        count[name] -=1
    for i in count :
        if count[i] !=0: # means : if count[i] it's value != 0 , do ... because of using dictionary "count" the indexing
            # here will  be by using the key not the the element index number for example count[0] will be the
            # element number 0 in the array
            print(i)
    '''
    # this method has a simple problem u have to Compare the part to the whole not vice versa ,so the above solution is more acurate
    for name in names_list2:
        count[name] +=1    
    for name in names_list1:
        if count[name] ==0 : # if the count[name] in names_list1 it's value ==0 , means it doesn't exist in the main array
            print(name)
        else :
            count[name] -=1
    '''
finder(names_lst1,names_lst2)
print(dict(count))
print(list(count))   # when u create a list from the dict is will present the keys only


'''
dic={5:1,1:2,3:3,2:4,4:5,6:6}

print(list(dic))
'''


# ********************* the clever Solution (XOR) ***********************
result=0
for num in array2+array1 :
    result=result^num
    print(result)