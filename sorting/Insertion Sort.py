arr = [-500, -1, 0, 3, 10, 55, 4, 99,-5, 50, 6, 7, 60, 22, 77, 88]


def insertion_sort(arr):
    for i in range(1,len(arr)):
        key_item = arr[i]
        j=i-1
        while j>=0 and arr[j] > key_item:
                arr[j + 1] = arr[j]
                j-=1
        arr[j + 1] = key_item

    return arr

print(insertion_sort(arr))
