# in place sorting which the space complexity is O(1) and the time complexity is O(N)
arr = [-500, -1,0, 3,10,55, 4, -5,50, 6, 7,60,20,77, 88]

def bubble(arr):
    counter=0
    while True:  # as long as False
        therange=(len(arr)-1)-counter # care about that pattern very well
        if therange==0: # if the range arrived to be 1 item break,because there is no need for swap one item !!
            break
        for i in range(therange): # the range becoming more smaller and smaller
            print(therange,i)
            if arr[i]>arr[i+1]:
                swap_pos(arr,i,i+1)
        counter+=1
    return arr

def swap_pos(array,i,j):
    array[i],arr[j]=arr[j],arr[i]

print(bubble(arr))