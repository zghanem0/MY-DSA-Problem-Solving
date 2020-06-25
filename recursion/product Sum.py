# The time Complexity is O(N) and the Space Complexity is O(Depth)
def sum_prod(arr, depth=1):
    sum = 0
    for element in arr:
        if type(element) is list:
            sum += sum_prod(element, depth + 1)  # the returned value from the recursion will be added to the sum variable
        else:
            sum += element
    return sum * depth

arr = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
print(sum_prod(arr))
