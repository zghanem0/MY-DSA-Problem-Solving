def smallest_diff(arr1, arr2):
    itr1 = 0
    itr2 = 0
    value1 = float("inf")
    value2 = float("inf")
    len_arr1=len(arr1)-1
    len_arr2=len(arr2)-1
    # Soting both arrays first
    arr1.sort()
    arr2.sort()
    main_abs = temp_abs = abs(arr1[0] - arr2[0])

    while itr1!=len_arr1 and itr2!=len_arr2:
        print(itr1,itr2)
        firstnum=arr1[itr1]
        secnum=arr2[itr2]

        if firstnum > secnum:
            temp_abs = abs(firstnum - secnum)
            itr2 += 1
        elif firstnum < secnum:
            temp_abs = abs(firstnum - secnum)
            itr1 += 1
        else:
            value1 = firstnum
            value2 = secnum
            break
        if temp_abs <main_abs :
            main_abs = temp_abs
            value1 = firstnum
            value2 = secnum

    return value1, value2


arr1 = [129, 111, 130, 37, 126, 121]
arr2 = [5, 185, 123, 155, 34, 165]
print(smallest_diff(arr1, arr2))
