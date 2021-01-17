#A = [1,2,3,2]
A=[4,2,2,4,2,6,8]
#A=[1,2,3,2,5,6]
#A=[2,2]
def BiValued(A):
    dic = {}
    LongestBiValued = 0
    temp_LongestBiValued=0
    for a in A:
        if a in dic:
            dic[a]=1
        else:
            dic[a]=0
    for a in A:
        if temp_LongestBiValued>=1:
            temp_LongestBiValued+=1
        if dic[a]==1 :
            if LongestBiValued ==0:
                temp_LongestBiValued=LongestBiValued=1
            else:
                LongestBiValued= temp_LongestBiValued
    return LongestBiValued


print(BiValued(A))

# --------------------------- other prety awsome solution ------------------------

# A = [1,2,3,2]
#A = [4, 2, 2, 4, 2, 6, 8]
A=[1,2,3,2,5,6]
#A=[2,2]
def BiValued(A):
    dic = {}
    i = 0
    j = len(A) - 1

    for a in A:
        if a in dic:
            dic[a] = 1
        else:
            dic[a] = 0
    while i < j:
        print(i,j)
        if dic[A[i]] == 1 and dic[A[j]] == 1 :
            break

        elif dic[A[i]] == 1:
            j -= 1
            continue

        elif dic[A[j]] == 1:
            i += 1
            continue
        else:
            i+=1
            j-=1
    size = (j-i+1)
    return size
print(BiValued(A))
