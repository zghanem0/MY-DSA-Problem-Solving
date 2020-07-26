def MaxCounter(N, A):
    array = [None] * (N )
    maxcounter = 0
    minimun = 0
    for a in A:
        i=a-1
        if a > N:
            minimun = maxcounter
            continue
        elif array[i] == None:
            array[i] = minimun + 1
        else:
            if array[i] < minimun:
                array[i] = minimun + 1
            else:
                array[i] += 1
        maxcounter=max(maxcounter,array[i])
        print(minimun)
    for i in range(len(array)):
        if array[i]==None:
            array[i]=minimun
        elif array[i]<minimun:
            array[i]=minimun

    return array


print(MaxCounter(5, [3, 4, 4, 6, 1, 4, 4]))
