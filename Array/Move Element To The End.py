# O(N) time | O(N) Space
def Move_Element_to_TheEnd(array, element):
    i = 0
    j = len(array) - 1
    while i < j:
        print(i,j)
        while i<j and array[j]==element:
            j-=1
        if  array[i]==element:
            array[i],array[j]=array[j],array[i]

        i+=1
    return array


array = [2, 1, 55, 1, 2, 2, 566, 1, 562, 2, 2]
element = 2
print(Move_Element_to_TheEnd(array, element))
'''

def Move_Element_to_TheEnd(array,element):
    i=0
    j=len(array)-1
    while i<j:
        print(i,j)
        if array[i]==element and array[j]==element:  # that solution will not work because of that case ?!!
            i += 1
            j -= 1
        elif array[i]==element:
            array[i], array[j] = array[j], array[i]
            i+=1
        elif array[j]==element:
            j-=1
        else:
            i += 1
            j -= 1
    return array

'''
