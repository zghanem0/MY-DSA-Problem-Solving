arr = [1, -1,2, 3,10,55, 4, -5,50, 6, 7,60,20,77, 88]

def ThreeLargest(arr):
    largest=[float('-inf'),float('-inf'),float('-inf')]
    for element in arr:
        if element>largest[2]:
            largest[0]=largest[1]
            largest[1]=largest[2]
            largest[2]=element
        elif element>largest[1]:
            largest[0]=largest[1]
            largest[1]=element
        elif element>largest[0]:
            largest[0] = element
        else:
            pass

    return largest
print(ThreeLargest(arr))