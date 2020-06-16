
# time complexity  O(N) , Space Complexity O(1)
'''
def is_subseq(main_arr, sub_arr):
    main_idx = 0
    sub_idx = 0
    while main_idx < len(main_arr) and sub_idx < len(sub_arr):
        if main_arr[main_idx] == sub_arr[sub_idx]:
            print(main_arr[main_idx] , sub_arr[sub_idx])
            sub_idx += 1
        main_idx += 1
    print(len(sub_arr),sub_idx)
    return sub_idx == len(sub_arr)
'''

# time complexity  O(N) , Space Complexity O(1)
def is_subseq(main_arr, sub_arr):
    sub_idx = 0
    for value in main_arr:  # main array end case                          who is reached first the loop will break
        if sub_idx== len(sub_arr):  # # Subsequance array end case
            break
        if value == sub_arr[sub_idx]:
            sub_idx +=1
    return sub_idx == len(sub_arr)

main_arr = [5, 1, 22, 25, 6, -1, 8, 10]
sub_arr = [1, 8, -1, 10]
print(is_subseq(main_arr, sub_arr))
