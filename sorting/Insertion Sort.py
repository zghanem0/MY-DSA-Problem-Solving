arr = [-500, -1, 0, 3, 10, 55, 4, 99,-5, 50, 6, 7, 60, 20, 77, 88]


def insertion_sort(arr):
    for i in range(len(arr)):
        for j in range(i):
            if arr[j] > arr[j+1]:
                swap_pos(arr, j, j + 1)
    return arr

def swap_pos(array, i, j):
    array[i], arr[j] = arr[j], arr[i]


print(insertion_sort(arr))
