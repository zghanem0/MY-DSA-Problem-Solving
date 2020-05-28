array = [2, 6, 4, -3, 1, 5, -9, 10]


def largst_cont_sum(arr):
    max_sum = curent_sum = 0
    for num in arr:
        curent_sum = max((curent_sum + num), num)
        max_sum = max(max_sum, curent_sum)
        print( ",  the curent is ", curent_sum,"the max : ", max_sum)
    print(max_sum)


largst_cont_sum(array)
