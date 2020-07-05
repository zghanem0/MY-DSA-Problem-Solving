#  time=O(N) | Space=O(1)
def monotonic_array(array):
    length = len(array) - 2
    increasing = 0
    decreasing = 0
    for i in range(length):
        if array[i] > array[i + 1]:
            increasing +=1
        if array[i] < array[i + 1]:
            decreasing +=1

    return increasing == length or decreasing == length

arr = [-1, -2, -100, -200, -500, -40000]
print(monotonic_array(arr))
arr = [-1, -2, -100, 5, -500, -40000]
print(monotonic_array(arr))


# pretty simple and nice solution : time=O(N) | Space=O(1)
def monotonic_array(array):
    length = len(array) - 2
    increasing =True
    decreasing = True
    for i in range(length):
        if array[i] > array[i + 1]:
            increasing = False
        if array[i] < array[i + 1]:
            decreasing = False

    return increasing or decreasing

arr = [-1, -2, -100, -200, -500, -40000]
print(monotonic_array(arr))
